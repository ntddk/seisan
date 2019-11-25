# 傾斜配分を支える技術

[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)

傾斜配分とは、飲み会等の精算にあたって、高位の役職ほど金額を高く、低位の役職ほど金額を低く設定することです。とりわけ、年功序列に立脚したJTBC (Japanese Traditional Big Company) において、傾斜配分は欠かすべからざる要素として知られています。本リポジトリは、この傾斜配分を自動化するためのスクリプトを含んでいます。忘年会にどうぞ。

## Quick Start

#### Z3版

![python](https://img.shields.io/badge/Python-2.7-blue?style=flat-square)

```
bash setup.sh
python2 solve_z3.py
```

#### PuLP版

![python](https://img.shields.io/badge/Python-3.6-blue?style=flat-square)

```
pip install -r requirements.txt
python3 solve_pulp.py
```

## Reference

- [mathematical optimization - Use mod function in a constraint using Python Pulp - Stack Overflow](https://stackoverflow.com/questions/47929215/use-mod-function-in-a-constraint-using-python-pulp)
- [Yet Another Math Programming Consultant: Finding all optimal LP solutions](http://yetanothermathprogrammingconsultant.blogspot.com/2016/01/finding-all-optimal-lp-solutions.html)
- [python - (Z3Py) checking all solutions for equation - Stack Overflow](https://stackoverflow.com/questions/11867611/z3py-checking-all-solutions-for-equation)

