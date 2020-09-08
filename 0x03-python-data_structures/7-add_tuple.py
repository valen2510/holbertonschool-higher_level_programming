#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = (0, 0)
    tuple_ac = tuple_a + tuple_c
    tuple_bc = tuple_b + tuple_c
    return (tuple_ac[0] + tuple_bc[0], tuple_ac[1] + tuple_bc[1])
