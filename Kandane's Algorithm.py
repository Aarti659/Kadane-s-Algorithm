def max_Subarray_Sum(Array, array_size):

    maxTillNow = Array[0]
    maxEnding = 0


    for n in range(0, array_size):
        maxEnding = maxEnding + Array[n]

        if maxEnding < 0:
            maxEnding = 0

        elif (maxTillNow < maxEnding):
            maxTillNow = maxEnding

    return maxTillNow



Array = [-2, -3, 4, -1, -2, 5, -3]

print("Maximum Subarray Sum:", max_Subarray_Sum(Array, len(Array)))
