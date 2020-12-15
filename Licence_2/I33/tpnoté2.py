""" def resolution(A,b):
	x = [b[0]/A[0][0]]
	for i in  range(1,len(A)):
		somme = b[i]
		for j in range(i):
			somme = somme - A[i][j]*x[j]
		x = x + [somme/A[i][i]]
	return x """

def resolution(A,b):
    x=[b[0]/A[0][0]]
    for i in range(len(A)):
        somme=b[i]
        for j in range(i,len(A[i])):
            somme = somme + A[i][j]*x[i]
        x = x + [somme/A[i][i]]
    return x

A=[[2,1,-1],[0,2,2],[0,0,1]]
#A=[[2,0,0],[1,2,0],[-1,2,1]]
b=[1,2,3]
print(resolution(A,b))


def multiplie(x,y,P):
    if (x == 0) or (y == 0):
        return 0
    m = len(bin(P)) - 3
    i = log_table[x]
    j = log_table[y]
    return alpha_table[(i+j) % ((1 << m)-1)]

""" def matmat(A,B,P): #faire avec multiplie(x,y,P)
    l=[]
    for i in range (len(A)):
        tmp = []
        for k in range(len(B[0])):
            s=0
            for j in range(len(A[0])):
                s+=(A[i][j])*(B[j][k])
            tmp.append(s)
        l.append(tmp)
    return l """

def det(A):
    signe = 1
    d = 1
    p = 1
    for j in range(len(A)-1):
        k = j
        while (k < len(A)) and (A[k][j] == 0):
            k = k + 1
        if (k == len(A)):
            return 0
        if (k != j):
            A[k],A[j] = A[j], A[k]
            signe = -signe
        d = d * A[j][j]
        for k in range(j+1,len(A)):
            p = p * A[j][j]
            s = A[k][j]
            for c in range(0,len(A)):
                A[k][c]=A[k][c]*A[j][j]-A[j][c]*s
    d = d * A[len(A)-1][len(A)-1]*signe
    if (abs(d) == 0):
        d = 0
    return((d/p)%26)

""" print(det([[23, 21, 16], [22, 2, 4], [22, 13, 21]]))
print(det([[17, 21, 25], [3, 19, 9], [11, 19, 14]]))
print(det([[9, 20, 12], [7, 4, 18], [24, 10, 13]]))
print(det([[1, 16, 24], [25, 10, 2], [16, 14, 17]]))
print(det([[11, 8, 6, 6], [18, 6, 24, 24], [12, 1, 4, 21], [18, 13, 12, 10]])) """

def elementmedian(M):
    i=0
    l=[]
    while i<len(M):
        j=0
        while j<len(M[i]):
            l+=[M[i][j]]
            j+=1
        i+=1
    l=sorted(l)
    i=(len(l)//2)
    return l[i]

""" M=[[11,7,9],[3,-2,6],[19,6,-9]]
print(elementmedian(M))
print(elementmedian([[6, 9, 1], [8, 6, 5], [0, 6, 2]]))
print(elementmedian([[8, 4, 0], [1, 5, 1], [2, 3, 9]]))
print(elementmedian([[2, 4, 6, 2, 1], [4, 1, 8, 5, 5], [1, 1, 6, 5, 8], [5, 5, 4, 5, 6], [8, 5, 9, 3, 3]]))  """