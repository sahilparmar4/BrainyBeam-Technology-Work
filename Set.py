#Set: Store multiple data in single variable, in {} brackets are unordered, unchanged, not allowed duplocates. Not supoort key: value frm.

s1 = {"a", "b", "c", "d"}
s2 = {"a", "x", "y", "c"}
s1.update(s2)
s1.union(s2)
s3=s1.intersection(s2)
print(s3)
s1.intersection_update(s2)
print(s1)
print(s2)
print(s1)
print(len(s1))
print(type(s1))
for i in s1:
    print(i, end=" ")
print("\n")
if "c" in s1:
    print("True")
else:
    print("False")
s1.add("New Element")
print(s1)
s1.update(s2)
print(s2)
print(s1)
s1.remove(1) #after removing, will generate error
print(s1)
s1.discard(2) #after removing, will not generate error
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)
del s1
print(s1)
s3 = s1.symmetric_difference(s2)
print(s1)
print(s2)
print(s3)
s1.symmetric_difference_update(s2)
print(s1)
print(s2)

