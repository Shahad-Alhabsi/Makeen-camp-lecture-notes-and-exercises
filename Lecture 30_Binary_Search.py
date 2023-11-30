from math import floor



def binary_search(list_, target):
    LI = 0
    HI = len(list_)-1
    while LI <= HI:
        MI = floor((HI+LI) / 2)
        if list_[MI] == target:
            return "Target found in index ", MI
        elif list_[MI] > target:
            # GO LIFT
            HI = MI-1   
        else:
            # GO RIGHT
            LI = MI+1
            
    return "not found"

list_  = [1,3,5,6,7]
target = 00
print(binary_search(list_, target))