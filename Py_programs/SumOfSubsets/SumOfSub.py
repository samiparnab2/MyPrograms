ans=[]
def PrintSub():
    for i in range(0,n):
        if(ans[i]==1):
            print(l[i])
    print()

def SumOfSub(currentSum,remSum,current):
    if currentSum>sum or currentSum+remSum<sum:
        return
    elif currentSum==sum:
        PrintSub()
        return
    ans[current]=1
    SumOfSub(currentSum+l[current],remSum-l[current],current+1)
    ans[current]=0
    SumOfSub(currentSum,remSum-l[current],current+1)
l=[]
n=int(input("enter no of data"))
s=0
for i in range(0,n):
    l.append(int(input("enter "+str(i)+"th element")))
    s+=l[i]
    ans.append(-1)
sum=int(input("enter the sum"))
SumOfSub(0,s,0)