from math import sqrt


def binary_search(x):
    if x == 1 or x ==0:
        return f"the sqare root of {x} is {x}"
    
    list_ = []
    for i in range(x):
        list_.append(i)

    target = sqrt(x)
    LI = 1
    HI = x
    while LI <= HI:
        MI = (HI+LI) // 2
        if list_[MI] == target:
            return f"the sqare root of {x} is {MI}"
        elif list_[MI] > target:
            # GO LIFT
            HI = MI-1   
        else:
            # GO RIGHT
            LI = MI+1
            
    return f"the square root of {x} is not an integer"


print(binary_search(0))
print(binary_search(1))
print(binary_search(27))
print(binary_search(16))
print(binary_search(144))
print(binary_search(25))
print(binary_search(255))

