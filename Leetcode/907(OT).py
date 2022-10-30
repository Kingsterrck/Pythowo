def sumSubarrayMins(arr) -> int:
    # fuck this shit
    count = 0
    for i in range (1,len(arr)+1):
        for k in range(len(arr)-i+1):
            tempArr = arr[k:k+i]
            count += min(tempArr)
    return count

print(sumSubarrayMins([3,1,2,4]))