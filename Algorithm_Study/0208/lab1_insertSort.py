N = int(input())
arr = []
for _ in range(N) :
    arr.append(int(input()))

for end in range(1, len(arr)):
    to_insert = arr[end]
    i = end
    while i > 0 and arr[i - 1] > to_insert:
        arr[i] = arr[i - 1]
        i -= 1
    arr[i] = to_insert
    print(arr)
