import os
solved=0
mat=[]

def RowErr(val,i,j):
    global mat
    for k in range(0,9):
        if j!=k and val==mat[i][k]:
            return 1
    return 0
def ColErr(val,i,j):
    global mat
    for k in range(0,9):
        if i!=k and val==mat[k][j]:
            return 1
    return 0

def CellErr(val,i,j):
    global mat
    if i<3:
        rs=0
    elif i<6:
        rs=3
    else:
        rs=6
    if j<3:
        cs=0
    elif j<6:
        cs=3
    else:
        cs=6
    for x in range(rs,rs+3):
        for y in range(cs,cs+3):
            if x!=i and y!=j and val==mat[x][y]:
                return 1
    return 0

def IsSolved():
    global mat
    for i in range(0,9):
        for j in range(0,9):
            if(mat[i][j]==0):
                return 0
    return 1


def SolveSudoku(r,c,currentVal):
    global solved,mat
    if solved==1:
        exit()
    if(RowErr(currentVal,r,c)==1 or ColErr(currentVal,r,c)==1 or CellErr(currentVal,r,c)==1):
        return 
    else:
        mat[r][c]=currentVal
        currentVal=0
        while r<9 and mat[r][c]!=0 :
            c+=1
            if c>=9:
                r+=1
                c=0
    solved=IsSolved()
    while currentVal<9 and solved==0:
        SolveSudoku(r,c,currentVal+1)
        currentVal+=1
        if(currentVal==9 and solved==0):
          mat[r][c]=0



ip=input().split()
xxx=0
for i in range(0,9):
    mat.append([])
    for j in range(0,9):
        mat[i].append(int(ip[xxx]))
        xxx+=1
for i in range(0,9):
    for j in range(0,9):
        print(mat[i][j]," ",end='')
    print()
i=0
j=0
while i<9 and mat[i][j]!=0 :
            if mat[i][j+1]==0:
              break
            j+=1
            if j>=9:
                i+=1
                j=0
SolveSudoku(i,j,mat[i][j])
print("solved")
for i in range(0,9):
    for j in range(0,9):
        print(mat[i][j],",",end='')
    print()

'''
for i in range(0,9):
    mat.append([])
    for j in range(0,9):
        os.system("clear")
        print(mat[i])
        ip=int(input())
        mat[i].append(ip)
'''
