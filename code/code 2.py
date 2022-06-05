import random
import copy


def read_fasta(name):
    fastaFile = open(str(name) + ".fasta", 'r')
    fastaFile.readline()
    sequence_ = ""
    for line in fastaFile.readlines():
        sequence_ += line[:-1]
    return sequence_


def get_subseq_k(seq, k):
    subsequences_ = []
    for i in range(len(seq)-k+1):
        subsequences_.append(seq[i:i+k])
    for i in range(k-1):
        subsequences_.append((seq[-k+i+1:] + seq[:i+1]))
    return subsequences_


def swap_vertices_edges(subseq_):
    test=[]
    relations_=[]
    for subsequence in subseq_:
        suff = subsequence[-K+1:]
        pref = subsequence[:K-1]

        if not test.count(suff):
            test.append(suff)
        if not test.count(pref):
            test.append(pref)
        suff_index = test.index(suff)
        pref_index = test.index(pref)
        first = True
        for relation_ in relations_:
            if relation_[0] == [pref_index, suff_index]:
                relation_[1] += 1

                first = False
        if first:
            relations_.append([[pref_index, suff_index], 1])
    return relations_, test

NAME = 's'
K = 100


sequence = read_fasta(NAME)
print("Исходная последовательность \n %s" % sequence)
subseq = get_subseq_k(sequence, K)
print("Разбиение последовательности: \n", subseq)

output = open('out.txt', 'w', encoding="utf-8")  # открытие файла для записи результатов
output.write('Разбиение на последовательности \n' + str(subseq))
# subseq - массив к-меров
# Перемешиваем К-меры, чтобы они не шли в правильном порядке
len_subseq = len(subseq)
for i in range(len_subseq):
    j = random.randint(0, len_subseq-1)
    subseq[i], subseq[j] = subseq[j], subseq[i]
print("Перемешанный набор: \n", subseq)
# relations_ - массив к-меров (связей суффиксов и префиксов, рёбер графа)
# test - массив префиксов и суффиксов (вершины графа)
relations_, test = swap_vertices_edges(subseq)
print('Массив префиксов и суффиксов: \n', test)
output.write('Массив префиксов и суффиксов: \n' + str(test))
cycles = []     # массив полученных циклов


def find_all_cycles(v, relations_least_, cycle=None):   # функция поиска циклов (№ вершины, список ребер, цикл)

    if cycle is None:
        cycle = []
    relations_least = copy.deepcopy(relations_least_)
    # print(cycle)
 for i in range(len(relations_least)):
        if relations_least[i][0][0] == v and relations_least[i][1] > 0:
            n = i
            relations_least_new = relations_least.copy()
            start = relations_least_new[i][0]
            relations_least_new[i][1] -= 1
            if relations_least_new[i][1] == 0:
                k = relations_least_new.pop(i)


            new_cycle = cycle.copy()
            new_cycle.append(start)
            # print(start, v)
            find_all_cycles(start[1], relations_least_new, new_cycle)

    if not relations_least:
        cycles.append(cycle)


class cycle_class:
    def __init__(self, relations, cycle, last_suff):
        self.relations = relations.copy()
        self.cycle = cycle.copy()
        self.last_suff = last_suff


def find_all_cycles_(relations_least):
    pref_i = relations_least[0][0][0]
    cycle = [pref_i]
    suff_i = relations_least[0][0][1]
    relations_least[0][1] -= 1
    if not relations_least [0][1]:
        relations_least.pop(0)

    relations_list_new = []
    relation_cycle = cycle_class(relations_least, cycle, suff_i)
    relations_list_new.append(relation_cycle)

    del relation_cycle
                                      

    relations_list = []
    cycles_exists = True
    while cycles_exists:
        relations_list = relations_list_new.copy()
        del relations_list_new
        relations_list_new = []
        cycles_exists = False
        relations_to_remove = []
        for relation_cycle in relations_list:
            if not relation_cycle.relations:
                continue
            cycles_exists = True
            for i in range(len(relation_cycle.relations)):
                if relation_cycle.relations[i][0][0] == relation_cycle.last_suff:
                    relations_list_sub_new = []
                    relations_list_sub_new = copy.deepcopy(relation_cycle.relations)
                    relations_list_sub_new[i][1] -= 1
                    if relations_list_sub_new[i][1] < 1:
                        vartice_i = relations_list_sub_new.pop(i)
                        vartice_i = vartice_i[0]
                    else:
                        vartice_i = relations_list_sub_new[i][0]
                    cycle_list_sub_new = copy.deepcopy(relation_cycle.cycle)
                    cycle_list_sub_new.append(vartice_i[0])
                    relations_list_new.append(cycle_class(relations_list_sub_new, cycle_list_sub_new, vartice_i[1]))

            relations_to_remove.append(relation_cycle)


    found_cycles = []
    for rel in relations_list:
        found_cycles.append(rel.cycle)
    return found_cycles


relations__ = copy.deepcopy(relations_)
cycles__ = find_all_cycles_(relations__)
def print__(cycle):
    str = ''
    for num in cycle:
        str += test[num][0]
    print(str)


def unique(cycles_):
    unique_cycles = []
    for cycl_1 in cycles_:
        len_ = len(cycl_1)
        unique_ = True
        for cycl_2 in unique_cycles:
            for i in range(-len_, 0):
                if cycl_1[i:] + cycl_1[:len_+i] == cycl_2:
                    unique_ = False
        if unique_:
            unique_cycles.append(cycl_1)
    return unique_cycles


print('\n\n'+'-'*25)
print('Все полученные кольца')
output.write('Все полученные кольца: \n')
for cycle_ in cycles__:
    print__(cycle_)
    output.write(str(cycle_))
print('-'*25)
print('Все уникальные кольца')
un_cycles__ = unique(cycles__)

for cycle_ in un_cycles__:
    print__(cycle_)
    output.write(str(cycle_))