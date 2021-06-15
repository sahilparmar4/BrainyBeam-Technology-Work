#2.	Write a Python program to enter marks of five subjects and calculate total, average and percentage.

wt = int(input("Enter marks of Web Technology: "))
cn = int(input("Enter marks of Computer Networks: "))
cg = int(input("Enter marks of Computer Graphics: "))
ds = int(input("Enter marks of Data Science: "))
daa = int(input("Enter marks of Design & Ananlysis of Algorithm: "))
total = wt + cn + cg + ds + daa
# avg = total/5
# percentage = total/9
print("Total of 5 subjects:", total)
# print("Average: ", avg)
# print("Percentage: ", percentage)