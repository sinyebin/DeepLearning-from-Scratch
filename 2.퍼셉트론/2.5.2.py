# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import numpy as np

import gate


def XOR(x1,x2):
    s1=gate.NAND(x1,x2)
    s2=gate.OR(x1,x2)
    y=gate.AND(s1,s2)
    return y


XOR(0,0)

XOR(1,0)

XOR(0,1)

XOR(1,1)


