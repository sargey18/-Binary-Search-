import random
import time


# implementation of binary search algorithm!!

# we will prove that binary search is faster than naive search
# naive search: scan entire list and ask if its equal to the target 
# if yes, return the index 
# if no, then return -1 

def naive_search(l, target):    # we are going to give this function a list and a target 
    for i in range(len(l)):     # so for i(the variable) in range ...in the length of the list
        if l[i] == target:
            return i            # if there is an index of l that == target return the i
        return -1               # if there is nothing then return minues 1
    
    
# binary search use divide and conquer 
# we will leverage the fact that out list is sorted 

def binary_search(l, target, low=None, high=None):   #IMPORTANT we could add low and high into our binary search, which will be the loweest indices to the highest indices that we search
    #example l = [1,3,5,10,12]
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
        
    if high < low:
        return -1 # this should only happen if you cannot find it 
    #first we need to find the mid point, so this woulbe the length of the list (l) divided by 2 but rounded down 
    midpoint = (low + high) // 2  
    # if the list midpoint == the target we can then return midpoint 
    if l[midpoint] == target:
        return midpoint 
    # however if the target is less than the midpoint 
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)    # at this point we have to divide this some how IMPORTANT  at this ponit the low = to current low but the high = midpoint
    else: 
        return binary_search(l, target, midpoint + 1, high)   # we could theoretically pass in half of the array on the right ... (l[midpoint + 1:])... then we would have to add the index back in 
    
if __name__=='__main__':
    # l = [1, 3, 5, 10, 12]
    # target = 7
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start), "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start), "seconds")
