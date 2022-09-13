def two_sum(arr, K):
    arr.sort()

    for i in range(len(arr)):
        target = K - arr[i]
        l, r = i+1 , len(arr)-1
        while l < r:
            mid = (l+r)//2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                r = mid-1
            else:
                l = mid+1
    return False



