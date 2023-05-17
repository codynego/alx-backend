#!/usr/bin/python3

dic = {}

dic["a"] = 1
dic["b"] = 2
dic["c"] = 3

print(dic)

las = list(dic.items())
lass = las.pop(0)
print("==========")
dic = dict(las)
print(dic)
