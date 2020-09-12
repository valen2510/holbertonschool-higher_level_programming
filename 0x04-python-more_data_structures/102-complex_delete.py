#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy_dic = a_dictionary.copy()
    for k, v in copy_dic.items():
        if v == value:
            del a_dictionary[k]
    return a_dictionary
