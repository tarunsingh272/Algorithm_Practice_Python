import unittest
import re


def part_one(string_list):
    result_list = []
    pattern = re.compile(r'[ATGC]*')
    for string in string_list:
        if len(string) <= 10:
            continue
        if len(string) >= 100:
            continue
        if pattern.match(string).span() == (0, len(string)):
            result_list.append(string)
    if len(result_list) < 3:
        return ''
    else:
        return result_list

def part_2(input):
    res = ''
    dict1 = {}

    predix = [i[-3:] for i in input]
    for word in input:
        dict1[word[0:3]] = word[3:]
        if word[0:3] not in predix:
            res = word

    while dict1.get(res[-3:]) != None:
        res += dict1[res[-3:]]
    return res

def part_3(string, mapping):
    i = 0
    result = {}
    s_list = []
    while i < len(string):
        dna = mapping[string[i:i+3]]
        if dna not in result:
            result[dna] = 1
        else:
            result[dna] += 1
        i += 3
    for item in sorted(result.items()):
        s_list.append(item[0]+': '+str(item[1])+'\n')

    return ''.join(s_list)

if __name__ =='__main__':
    test_1 = ['ATGCATGCATGCATGC', 'ATGCBATGCATGC', 'ATGCatgcatgc']
    print(part_one(test_1))
    test_2 = ['AGTGGGGGGGGG', 'AAACCCAATTT', 'TTTACACAGCT', 'GCTGGGCCCAGT']
    print(part_2(test_2))
    print(part_3('AAATTTGGGAAA', {'AAA': 'Lysine', 'GGG': 'Glycine', 'TTT': 'Phenylalanine'}))

