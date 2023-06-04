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


# 1.4.1 파일로 저장하기

# 1.4.2 클래스

class 클래스 이름:
    def __init__(self, 인수, ...): #생성자
        ...
    def 메서드 이름 1(self, 인수, ...): #메서드1
        ...
    def 메서드 이름 2(self, 인수, ...): #메서드2
        ...


class Man:
    def __init__(self, name):
        self.name=name
        print("Initialized!")
    def hello(self):
        print("Hello "+self.name+"!")
    def goodbye(self):
        print("Good-bye "+self.name+"!")
m=Man("예빈")
m.hello()
m.goodbye()

# 1.5 넘파이

# 1.5.1 넘파이 가져오기

import numpy as np

# 1.5.2 넘파이 배열 생성하기

x=np.array([1.0,2.0,3.0])

print(x)

type(x)

# 1.5.3 넘파이의 산술연산

x=np.array([1.0,2.0,3.0])

y=np.array([2.0,4.0,6.0])

x+y

x-y

x*y

x/y

x=np.array([1.0,2.0,3.0])

x/2.0

# 1.5.4 넘파이의 N차원 배열

A=np.array([[1,2],[3,4]])

print(A)

A.shape

A.dtype

B=np.array([[3,0],[0,6]])

A+B

A*B

print(A)

A*10

# 1.5.5 브로드캐스트

A=np.array([[1,2],[3,4]])

B=np.array([[10,20]])

A*B

# 1.5.6 원소 접근

X=np.array([[51,55],[14,19],[0,4]])

print(X)

X[0]

X[0][1]

for row in X:
    print(row)

for row in X:
    for col in row:
        print(col)

X=X.flatten()

print(X)

X[np.array([0,2,4])]

X>15

X[X>15]

# 1.6 matplotlib

# 1.6.1 단순한 그래프 그리기

import matplotlib.pyplot as plt

x=np.arange(0,6,0.1)

y=np.sin(x)

plt.plot(x,y)
plt.show()

# 1.6.2 pyplot의 기능

x=np.arange(0,6,0.1)

y1=np.sin(x)

y2=np.cos(x)

plt.plot(x,y1, label="sin")
plt.plot(x,y2,linestyle="--",label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin&cos')
plt.legend()
plt.show()

# 1.6.3 이미지 표시하기

import matplotlib.pyplot as plt
from matplotlib.image import imread

img=imread('vr과제4.png')

plt.imshow(img)
plt.show()


