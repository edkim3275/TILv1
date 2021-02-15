arr = [1, 2, 1, 3, 1, 1]
N = len(arr)
triplet = False
run = False
for i1 in range(N):
    for i2 in range(N):
        if i1 != i2:
            for i3 in range(N):
                if i1 != i3 and i2 != i3:
                    for i4 in range(N):
                        if i1 != i4 and i2 != i4 and i3 != i4:
                            for i5 in range(N):
                                if i1 != i5 and i2 != i5 and i3 != i5 and i4 != i5:
                                    for i6 in range(N):
                                        if i1 != i6 and i2 != i6 and i3 != i6 and i4 != i6 and i5 != i6:
                                            # print(arr[i1], arr[i2], arr[i3], arr[i4], arr[i5], arr[i6])
                                            if arr[i1] == arr[i2] and arr[i1] == arr[i3]:
                                                triplet = True
                                            if arr[i2] == arr[i1]+1 and arr[i3] == arr[i1]+2:
                                                run = True
if triplet == True and run == True:
    print("baby-gin")
else:
    print("not-baby-gin")
