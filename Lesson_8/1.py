"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

import collections


def haffman_algo(string):
    counter = collections.Counter(string)

    sorted_counter = sorted(counter.items(), key=lambda item: item[1])

    if len(sorted_counter) != 1:
        while len(sorted_counter) > 1:
            value = sorted_counter[0][1] + sorted_counter[1][1]

            new_element = {0: sorted_counter.pop(0)[0],
                           1: sorted_counter.pop(0)[0]}

            for i, element in enumerate(sorted_counter):

                if value > element[1]:
                    continue
                else:
                    sorted_counter.insert(i, (new_element, value))
                    break
            else:

                sorted_counter.append((new_element, value))
    else:
        value = sorted_counter[0][1]
        new_element = {0: sorted_counter.pop(0)[0], 1: None}
        sorted_counter.append((new_element, value))

    return sorted_counter[0][0]


codes = dict()


def haffman_encoding(tree, track=''):
    if not isinstance(tree, dict):
        codes[tree] = track
    else:
        haffman_encoding(tree[0], track=f'{track}0')
        haffman_encoding(tree[1], track=f'{track}1')


string = 'Thank u very much for the "algorithms and data structures!" course!'
tree = haffman_algo(string)
haffman_encoding(tree)


def haffman_output():
    for i in string:
        print(codes[i], end=' ')
    print()


haffman_output()
