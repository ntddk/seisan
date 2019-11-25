#!/usr/bin/env python2
#coding: utf-8

from z3 import *

amount = 50000

s = Solver()

a = Int('a') # 役職
b = Int('b')
c = Int('c')
d = Int('d')
e = Int('e')
f = Int('f')

positions = [a, b, c, d, e, f]

s.add(a + b + (c*2) + (d*2) + (e*2) + (f*5) == amount)  # 参加人数

for i in range(len(positions)-1):
    s.add(positions[i] >= positions[i+1])           # 傾斜
    s.add(positions[i] - positions[i+1] >= 500)     # 差額は500円以上
    s.add(positions[i] - positions[i+1] <= 1000)    # 差額は1000円以下
    s.add(positions[i] % 500 == 0)                  # 500円の倍数
    s.add(positions[i+1] % 500 == 0)

while s.check() == sat:
    print(s.check())
    m = s.model()
    print([{x: m[x]} for x in positions])
    s.add(Or([x != m[x] for x in positions]))

