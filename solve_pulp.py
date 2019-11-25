#!/usr/bin/env python3
#coding: utf-8

from pulp import *

amount = 50000

m = LpProblem(sense=LpMinimize)

a = LpVariable('a', cat=LpInteger) # 役職
b = LpVariable('b', cat=LpInteger)
c = LpVariable('c', cat=LpInteger)
d = LpVariable('d', cat=LpInteger)
e = LpVariable('e', cat=LpInteger)
f = LpVariable('f', cat=LpInteger)

positions = [a, b, c, d, e, f]

var = pulp.LpVariable.dicts('var', positions, cat=LpInteger)

m += a + b + (c*2) + (d*2) + (e*2) + (f*5) == amount    # 参加人数

for i in range(len(positions)-1):
    m += positions[i] >= positions[i+1]             # 傾斜
    m += positions[i] - positions[i+1] >= 500       # 差額は500円以上
    m += positions[i] - positions[i+1] <= 1000      # 差額は1000円以下
    m += positions[i] == 500*var[positions[i]]      # 500円の倍数
    m += positions[i+1] == 500*var[positions[i+1]]

status = m.solve()
print(pulp.LpStatus[status])
print([{x: value(x)} for x in positions])

