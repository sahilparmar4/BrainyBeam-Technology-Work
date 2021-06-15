#upacked tuple
#assigned value in single var called packing
#unpacking is vice versa of packing
t1=(10, 20, 30, 40, 50)
t2=('abc', 'def', 'xyz')
t3=t1+t2 # concatenate
print(t3)
print(t1*2) # * operator
print(t1.count(10)) # count
print(t1)

(a, *c, b, d) = t1
print(a)
print(c)
print(b)
print(d)

for x in (t1):
   print(x)

print('----------List-----------')

#List is mutable, while tuples are immutable means we can't change anything in tuples.

# l1=['a', 'b', 'c', 1, 2, 3.5, True]
# print(l1[2:4]) # slicing
# l2=['SSR'] # updating
# print(l1)
# print(len(l1)) # length
# print(type(l1)) # type
# print(l1[2:4])
#
# if 'a' in l1: # membership operator
#    print('present')
# else:
#    print('absent')
#
# l1[0]="Sahil"
# l1[1:3]=['Kamleshbhai', 'Parmar']
# print(len(l1))
# l1[1:3]=['Kamleshbhai']
# print(len(l1))
# l1.insert(2,"Parmar") # insert
# l1.extend(l2) # extend
# l1.remove(3.5) # remove
# l1.pop(3) # pop
# print(l1)



