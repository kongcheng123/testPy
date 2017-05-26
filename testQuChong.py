f = open('result1.txt', 'w')
a=f.read()
f.close()
b=a.split(',')
print(len(b))
s=set()
for i in b:
    s.add(i)
print(len(s))