import sys 
sys.stdin = open("./Algorithm_Study/BOJ0305/BOJ9663", "r")
n=int(input())
count=0
 
row,left,right=[0 for _ in range(n)],[0 for _ in range(2*n-1)],[0 for _ in range(2*n-1)]
 
def queenlocation(index):
    global count
    if index==n:   
        count+=1
        return
    for col in range(n): 
        if row[col] + left[index+col] + right[n-1+index-col]==0: 
            row[col]=left[index+col]=right[n-1+index-col]=1
            queenlocation(index+1)
            row[col]= left[index+col]= right[n-1+index-col] = 0
 
queenlocation(0)
print(count)
