def inv(lst):
    count = 0
    for i in range(len(lst)-1):
        for j in range(len(lst)):
            if lst[i]>lst[j] and i<j:
                # print(lst[i],lst[j])
                count +=1
    return count
numbers = [1,7,3,4,5]
print(inv(numbers))