import random
import copy

# Исходная последовательность
sequence = 'AGCATGTCCTAGCA'
print("Исходная последовательность \n %s" % (sequence))
subseq = []
for i in range(len(sequence) - 2):
    subseq.append(sequence[i:i + 3])
subseq.append(sequence[-2:] + sequence[0])
subseq.append(sequence[-1:] + sequence[:2])
print("Разбиение последовательности на триплеты \n", subseq)
# subseq - массив к-меров (к=3)
# Перемешиваем К-меры, чтобы они не шли в правильном порядке
for i in range(len(subseq)):
    j = random.randint(0, len(subseq) - 1)
    subseq[i], subseq[j] = subseq[j], subseq[i]
print("Перемешанный набор триплетов\n", subseq)

# relations_ - массив к-меров (связей суффиксов и префиксов, рёбер графа)
# test - массив префиксов и суффиксов (верши графа)
relations_ = []
test = []
for seq in subseq:
    suff = seq[-2:]
    pref = seq[:2]
    if not test.count(suff):
        test.append(suff)
    if not test.count(pref):
        test.append(pref)
    suff_index = test.index(suff)
    pref_index = test.index(pref)
    first = True
    for relation_ in relations

        if relation_[0] == [pref_index, suff_index]:
            relation_[1] += 1
            first = False
    if first:
        relations_.append([[pref_index, suff_index], 1])
print('Массив префиксов и суффиксов \n', test)

cycles = []  # массив полученных циклов


def find_all_cycles(v, relations_least_, cycle=[]):  # функция поиска циклов (№ вершины, список ребер, цикл)

    relations_least = copy.deepcopy(relations_least_)
    for i in range(len(relations_least)):
        if relations_least[i][0] == v and relations_least[i][1] > 0:
            n = i
            relations_least_new = copy.deepcopy(relations_least)
            start = relations_least_new[i][0]
            relations_least_new[i][1] -= 1
            if relations_least_new[i][1] == 0:
                k = relations_least_new.pop(i)
            new_cycle = cycle.copy()
            new_cycle.append(start)
            find_all_cycles(start[1], relations_least_new, new_cycle)

    if not relations_least:
        cycles.append(cycle)


print('-' * 25 + '\n\n')
find_all_cycles(1, relations_)


def print_(cycle):
    str = ''
    for num in cycle:
        str += test[num[0]][0]
    print(str)
                                    

print('-' * 25)
print('Все полученные кольца')
for cycle_ in cycles:
    print_(cycle_)


def unique(cycles_):
    unique_cycles = []
    for cycl_1 in cycles_:
        len_ = len(cycl_1)
        unique_ = True
        for cycl_2 in unique_cycles:
            for i in range(-len_, 0):
                if cycl_1[i:] + cycl_1[:len_ + i] == cycl_2:
                    unique_ = False
        if unique_:
            unique_cycles.append(cycl_1)
    return unique_cycles


un_cycles = unique(cycles)

print('-' * 25)
print('Все уникальные кольца')
for cycle_ in un_cycles:
    print_(cycle_)
