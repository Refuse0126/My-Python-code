"""
分割数字每一位，注意不是传统除法/，而是真除//
例子：找水仙花数
Date：2019.5.15
"""
for i in range(100,300):
    a=i//100
    b=i%100//10
    c=i%10
    if a**3+b**3+c**3==i: 
        print(i,end=',')