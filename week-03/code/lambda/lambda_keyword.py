#!/usr/bin/env python

"""
example code for using lambda, keywords, and keyword scope

The challenge:

Write a function that returns a list of n functions,
such that each one, when called, will return the input value,
incremented by an increaseing number.

you should use a for loop, lambda, and a keyword argument

Not clear? here's what you should get:

In [96]: the_list = function_builder(4)

In [97]: the_list[0](2)
Out[97]: 2

In [98]: the_list[1](2)
Out[98]: 3

In [100]: for f in the_list:
    print f(5)
   .....:     
5
6
7
8

extra credit: do it with a list comprhension, instead of a for loop

"""


# Write a function that returns a list of n functions,
# such that each one, when called, will return the input value,
# incremented by an increaseing number.

def function_builder(howmany):
    return [lambda n, i=i: n + i for i in range(howmany)]


# def function_builder(howmany):
#     ret = []

#     for x in range(howmany):
#         ret.append(lambda n, x=x: n + x)

#     return ret


if __name__ == '__main__':
    the_list = function_builder(4)
    print the_list[0](2)
    print the_list[1](2)
