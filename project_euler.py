#problem0
"""
square_numbers=[]
odd=[]
for i in range(0,693001):
    i=i**2
    square_numbers.append(i)
print(square_numbers)
for number in square_numbers:
    if number % 2==1:
        odd.append(number)
total=0
for n in odd:
    total+=n
print(total)
"""
#problem1
"""
z=[]
for i in range(0,1000):
    if i % 3==0 or i %5==0:
        z.append(i)
total=0=
for number in z:
    total+=number
print(total)
"""

#problem2
"""
finos=[0,1]
for i in range(1000001):
    z=sum(finos[-2:])
    if z<4000001:
        finos.append(z)
print(finos)
k=[]
for n in finos:
    if n%2==0:
        k.append(n)
print(sum(k))
"""
"""
q=[]
for i in range(1,999):
    for o in range(1,999):
        l=i*o
        if str(l)==str(l)[::-1]:
            q.append(l)
print(max(q))
"""
"""
l=[]
for i in range(1, 101):
    i=i**2
    l.append(i)
print(l)
k=0
g=[]
for s in range(1, 101):
    g.append(s)
print(g)
g=sum(g)
print(g)
g=g**2
l=sum(l)
print(g - l)
"""
s=[]
for i in range(1,10002):
    if i %1==0 and i%i==0:
        s.append(i)
print(s)