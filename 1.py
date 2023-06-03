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

# 1.3.1 산술 연산

1-2

4*5

7/5

3**2

# 1.3.2 자료형

type(10)

type(2.718)

type("hello")

# 1.3.3 변수

x=10

print(x)

x=100

print(x)

y=3.14

x*y

# 1.3.4 리스트

a=[1,2,3,4,5]

print(a)

len(a)

a[0]

a[4]

a[4]=99

print(a)

a[0:2]

a[1:]

a[:3]

a[:-1]

a[:-2]

# 1.3.5 딕셔너리

me={'height':100}

me['height']

me['weight']=70

print(me)

# 1.3.6 bool

hungry=True

sleepy=False

type(hungry)

not hungry

hungry and sleepy

hungry or sleepy

# 1.3.7 if문

hungry=True

if hungry:
    print(("I'm hungry"))

hungry=False

if hungry:
    print("I'm hungry")
else:
    print("I'm not hungry")
    print("I'm sleepy")

# 1.3.8 for문

for i in[1,2,3]:
    print(i)


# 1.3.9 함수

def hello():
    print("Hello World!")


hello()


def hello(object):
    print("Hello "+object+"!")


hello("cat")


