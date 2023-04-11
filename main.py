def inchideri(stare):
    global M,inc
    for X in M:
        if X[0]==stare and X[1]=='l':
            for y in X[2]:
                if y not in inc:
                    inc.append(y)
                    inchideri(y)
def mutari(stare,litera):
    global mut,Inchideri,M
    lit=[]
    for x in Inchideri:
        if x[0]==stare:
            for y in x[1]:
                for z in M:
                    if y==z[0] and z[1]==litera:
                        for k in z[2]:
                            if k not in lit:
                                lit.append(k)
                                for m in Inchideri:
                                    if m[0]==k:
                                        for h in m[1]:
                                            if h not in mut:
                                                mut.append(h)
    mut.sort()

f=open("tastatura.txt")
s=f.readline()
noduri=s.split()
print(noduri)
s=f.readline()
M=[]
while s!="":
    s=s.split()
    M.append(s)
    s=f.readline()
F=M[len(M)-1]
M=M[:-1]
N=[M[0]]
i=0
for x in range(len(M)):
    M[x][2]=[M[x][2]]
for x in range(len(M)):
    for y in range(1,len(M)):
        if M[y][0]==M[x][0] and M[y][1]==M[x][1] and M[y][2][0] not in M[x][2]:
                M[x][2].append(M[y][2][0])

for x in M[1:]:
    if x[0]==N[i][0] and x[1]==N[i][1] and len(x[2])<=len(N[i][2]):
        i+=1
        i-=1
    else:
        N.append(x)
        i+=1
M=N
for x in M:
    print(*x)
Inchideri=[]
for L in M:
    if L[1]=='l'and L[0] not in [Inchideri[i][0] for i in range(len(Inchideri))]:
        inc = [L[0]]
        inchideri(L[0])
        Inchideri.append([L[0],inc])
for L in noduri:
    if L not in [Inchideri[i][0] for i in range(len(Inchideri))]:
        Inchideri.append([L,[L]])
Inchideri.sort(key=lambda x:int(x[0][1:]))
for x in Inchideri:
    print(*x)
litere=[]
for x in M[1:]:
    if x[1] not in litere and x[1]!='l':
        litere.append(x[1])
litere.sort()
print(litere)
T=[]
for x in Inchideri:
    for y in litere:
        mut=[]
        mutari(x[0],y)
        T.append([x[0],y,mut])
init=Inchideri[0][1]
init.sort()
print("init",init)
for x in T:
    print(*x)
AFD=[]
for y in litere:
    k=[]
    for x in init:
        for z in T:
            if z[0]==x and z[1]==y:
                for q in z[2]:
                    if q not in k:
                        k.append(q)
    k.sort()
    T.append([init,y,k])
k=[]
i=len(litere)
while i!=0:
    print(i)
    if T[-i][2] not in [T[j][0] for j in range(len(T))] and T[-i][2]!=[]:
        for y in litere:
            k=[]
            for x in T[-i][2]:
                for z in T:
                    if z[0] == x and z[1] == y:
                        for q in z[2]:
                            if q not in k:
                                k.append(q)
            k.sort()
            T[-i][2].sort()
            T.append([T[-i][2], y, k])
            i+=1
            print(i)

    i=i-1

for i in range(len(Inchideri)*len(litere),len(T)):
    AFD.append(T[i])
print("AFD:")
for x in AFD:
    print(*x)
Fafd=[]
for x in AFD:
    for y in x[0]:
        if y in F and x[0] not in Fafd:
            Fafd.append(x[0])
print("Finale AFD:")
for x in Fafd:
    print(*x)
