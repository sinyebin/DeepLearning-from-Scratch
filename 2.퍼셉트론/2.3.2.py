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

x=np.array([0,1]) # 입력

w=np.array([0.5,0.5]) #가중치

b=-0.7

w*x

np.sum(w*x)

np.sum(w*x)+b


