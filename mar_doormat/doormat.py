# Enter your code here. Read input from STDIN. Print output to STDOUT
m = 3
t = 1
wel = 'WELCOME'
lw = input()
li = lw.split()
l = int(li[0])
w = int(li[1])
q = []
p = []
fi = []
x = '-'
y = '.|.'
for i in range(l):
    q.append(x * w)
# print(q)
for i in range(int((len(q) - 1) / 2)):
    g = list(q[i])
    for k in range(m):
        (g.remove(g[0]))

    m = m + 6
    letter = "".join(g)
    p.append(letter)

# traversing in list p(in exact order)
for item in p:
    ext = int((len(item)) / 2)
    d = list(item)

    d.insert(ext, y * t)
    t = t + 2
    fi.append(d)

for i in range(len(fi)):
    print("".join(fi[i]))

for i in range(l):
    e = list(x * w)
for i in range(7):
    e.remove(e[0])
j = int((w - 7) / 2)
e.insert(j, wel)
print("".join(e))

fi.reverse()
for i in range(len(fi)):
    print("".join(fi[i]))
