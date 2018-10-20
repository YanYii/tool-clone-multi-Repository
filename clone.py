# -*- coding:utf-8 -*-
import os

filename = 'repo.txt'

with open(filename) as f:
    for line in f:
        os.system('git clone ' + line)
