import unittest
import re
"""
https://www.1point3acres.com/bbs/thread-451074-1-1.html
"""

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

def part_2(input_string):
    input = part_one(input_string)
    if len(input) == 0:
        return ''
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

def analyze_dna(strands, codon_mapping):
    string = part_2(strands)
    i = 0
    result = {}
    s_list = []
    while i < len(string):
        if len(string[i:i+3]) < 3:
            break
        dna = codon_mapping[string[i:i+3]]
        if dna not in result:
            result[dna] = 1
        else:
            result[dna] += 1
        i += 3
    for item in sorted(result.items()):
        s_list.append(item[0]+': '+str(item[1])+'\n')

    return  ''.join(s_list)

if __name__ =='__main__':
    print(part_one(['AATTGGCCAATTG','TTGAATTGGCCAAAA','AAATTTGGGCCC','AAAEEERRRTTT','NEWUSER123']))
    print(part_2(['AATTGGCCAATTG', 'TTGAATTGGCCAAAA', 'AAATTTGGGCCC']))
    print(part_3(['AATTGGCCAATTG','TTGAATTGGCCAAAA','AAATTTGGGCCC','AAAEEERRRTTT','NEWUSER123'], {}))