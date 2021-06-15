d1={
    "course": "B.Tech",
    "branch": "IT",
    "sem": 6,
    "result": 9.01
    }
print(d1.keys())
d1["Exam"]="ESE"
print(d1.values())
print(d1.items())
d1["Exam"]="CIE"
print(d1)
d1.update({"Exam": "ESE"})
print(d1)
del d1["result"]
print(d1)
d1.pop("Exam")
print(d1)
d1.popitem()
d1.clear()
print(d1)
d2=d1
print(d2)
d2=d1.copy()
d1.pop("result")
print(d1)
print(d2)
d3=dict(d1)
print(d1)
if "course" in d1:
    print('Yes')
else:
    print('No')
for i, j in d1.items():
    print(i, j)
