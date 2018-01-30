# -*- coding: utf-8 -*-
from random import randint as ri
sayi1 = 3
sayi2 = 5

print("Eşit eşitse")
print(sayi1 == sayi2) # False
print("Eşit değilse")
print(sayi1 != sayi2) # True

ben = "Flask"
o = "Django"
# Stringler için is ve == aynı görevi görüyor.
print("is ve ==")
print(ben is o)
o = "Flask"
print(ben is o)
print(ben == o)

'''
is_true = False
if 3 < 4:
    is_true = True
'''
print("3 küçük müdür 4")
print(3 < 4)

# is_true = 3 < 4
print("3 büyük müdür 4")
print(3 > 4)
print("3 küçük eşit büyük eşit 4")
print (3 <= 4)
print(3 >= 4)

# || -> or in java, c etc..
# && -> and in ''
# and
print(True and True)
# or
print (False or True or 3/0)

x = ri(0,9)
y = ri(0,9)

if x < y:
    print("X sayısı: {}".format(x),
    "küçüktür",
    "Y sayısı: {}".format(y))
elif x == y:
    print("X sayısı: {}".format(x),
    "eşittir",
    "Y sayısı: {}".format(y))
else:
    print("X sayısı: {}".format(x),
    "büyüktür",
    "Y sayısı: {}".format(y))

# loop
primes = [2, 3, 5, 7]
for prime_number in primes:
    print(prime_number)

print("-----------------")


for index in range(len(primes)):
    print(primes[index])

print("-----------------")

for index in range(8,3,-2):
    print(index)

count = 0
print("-------------")
while count < 5:
    print(count)
    count += 1


print("-------------")
# my_list = [3,4,5]
my_list = list(range(3,6))
print(my_list)
print("-------------")


print("-------------")



print("-------------")

#functions
def toplama(sayi1, sayi2):
    sayi1 += sayi2


x = 5
y = 6
# pass by value reference
toplama(x, y)

def toplama2(sayi1, sayi2):
    return sayi1 + sayi2

x = toplama2(sayi1=x, sayi2=y)

print(x)


toplam = 0


def toplama3():
    toplam += 1
    if toplam < 10:
        toplama3()
    else:
        print(toplam)































'''
if __name__ == '__main__':
    my_function()
'''
