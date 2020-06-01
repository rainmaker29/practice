# Hackerrank Interview Kit arrays #4
def swap(arr):
    n = len(arr)
    pos = [0]*(n+1)
    for i,x in enumerate(arr):
        pos[x]=i
    for i in range(n):
        if arr[i]!=i+1:
            swaps+=1
            t = arr[i]
            arr[i]=i+1
            arr[pos[i+1]] = t
            pos[t] = pos[i+1]
    return swaps
