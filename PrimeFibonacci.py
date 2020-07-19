from random import randint
import itertools
def prime1list(n1,n2):
        number_range = set(range(n1,n2))
        primes_list1 = []
        for num in range(n1,n2):
            if all(num % i != 0 for i in range(2, num)):
                primes_list1.append(num)
        print(primes_list1)
        str2 = ' '.join(str(e) for e in primes_list1)
        primes_list2=[]
        for i in range(2, 3):
            for item in itertools.product((primes_list1), repeat=i):
                str3 = ''.join(map(str, item))
                str3=int(str3)
                primes_list2.append(str3)
        print(primes_list2)
        primes_list3=[]
        for num in primes_list2:
            if all(num % i != 0 for i in range(2, num)):
                primes_list3.append(num)
        print(primes_list3)
        print("Max number is", max(primes_list3))
        print("Min number is", min(primes_list3))
        length=len(primes_list3)
        print("Length is", length)
        a=min(primes_list3)
        b=max(primes_list3)
        while i<length-1:
            c=a+b
            a=b
            b=c
            i+=1
        print(a)
prime1list(2,40)