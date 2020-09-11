#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum_product = (sum(map((lambda tupla: tupla[0] * tupla[1]), my_list)))
        sum_weight = (sum(map((lambda tupla: tupla[1]), my_list)))
        return sum_product / sum_weight
    return 0
