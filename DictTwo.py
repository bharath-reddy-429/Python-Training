d={1:'One', 2:"Two", 3:"Three", 4:"Four"}
for i in d.values():
    print(i)
for i in d.keys():
    print(i)
del d[1]
print(d)