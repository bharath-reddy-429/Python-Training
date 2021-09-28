a=10
b=20.5
c=3+5j
d='python'
t=True
l=[1,2,3,4,5]
tup=(1,2,3,4,5)
s={1,2,3,4,5}
fs=frozenset(s)
dc={1: 'c', 2: 'java', 3: 'python'}
print(dc)
print(type(fs))
print(list(range(1,11)))
print(s,fs)
by=bytes(l)
for i in by:
    print(i,end=" ")
bys=bytearray(l)
for i in bys:
    print(i, end=" ")
