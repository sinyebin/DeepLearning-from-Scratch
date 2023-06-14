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


def cross_entropy_error(y,t):
    delta=1e-7
    return -np.sum(t*np.log(y+delta))


t=[0,0,1,0,0,0,0,0,0,0]

y=[0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]

cross_entropy_error(np.array(y),np.array(t))

y=[0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]

cross_entropy_error(np.array(y),np.array(t))


