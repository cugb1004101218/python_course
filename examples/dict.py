#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict_a = {
    "name": "Alan",
    "age": 24,
    1: "level_1"
}

print dict_a["name"]
print dict_a["age"]
print dict_a[1]

print "name" in dict_a
print "xxx" in dict_a
print dict_a.keys()
print dict_a.values()
print dict_a.items()
