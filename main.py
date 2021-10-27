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

def binary_search(l, target):
    #example l = [1,3,5,10,12]
    midpoint = (len(l)) // 2