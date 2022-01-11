"""
Created by SungMin Yoon on 2020/03/02..
Copyright (c) 2020 year SungMin Yoon. All rights reserved.
"""

import numpy as np


def arumi(_list):

    _list.insert(0, 0)
    _list.append(0)
    diff_array = np.diff(np.sign(np.diff(_list)))
    diff_list = []
    for i in diff_array:
        diff_list.append(i)

    print('signal_list = ', _list)
    print('diff_list =   ', diff_list)

    count = 0
    zero_index_list = []
    value_index_list = []

    print('signal_count', len(_list))
    print('diff_count  ', len(diff_list))

    for j in diff_list:
        if j == 0:
            zero_index_list.append(count)
            value_index_list.append(_list[count])
        count = count + 1

    max_value = max(value_index_list)
    max_index = value_index_list.index(max_value)
    angle_index = zero_index_list[max_index]

    # signal 리스트 에서 미분 2번하여 diff_list 에서 완만한 0을 찾고 그중에서 가장 높은 값을 가진 인덱스를 찾는다.
    print('zero_index_list ', zero_index_list)
    print('value_index_list', value_index_list)
    print('max_value = ', max_value)
    print('max_index = ', max_index)

    return angle_index


if __name__ == "__main__":
    signal_list = [11, 22, 32, 12, 34, 34, 21, 10, 22, 22, 30, 40, 60, 40, 40, 30, 21, 55, 45, 12, 21, 44, 30, 21]
    result = arumi(signal_list)
    print('------------------------------')
    print('result = ', result)
