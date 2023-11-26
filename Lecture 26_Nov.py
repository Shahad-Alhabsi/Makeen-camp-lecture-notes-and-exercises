## USING LISTS WITH FUNCTIONS

"""EXERCISE 1: """
def readFloats():
    while True:
        try:
            user_in = input("Enter floats separated by a space to form a list: " )
            my_list = [float(i) for i in user_in.split()]
            break
        except:
            print("Invalid input!")
            
    while True:    
        try:
            factor = int(input("Enter the factor (ineger): "))
            return my_list, factor # return will break the loop and exit the function
        except:
            print("Error: factor must be an integer. Try again")
                
def multiply(floats_list, factor):
    for i in range(len(floats_list)):
        floats_list[i] = floats_list[i]*factor
    return floats_list
 
def printReversed(List):
    List.reverse()
    return List

def main():
    List, factor = readFloats()
    print(printReversed(multiply(List, factor)))
     
main()



"""EXERCISE 2: """
MARTIX = [[0,5,1],
         [4,9,0],
         [0,6,0]]
         
count = 0        
for row in range(len(MARTIX)):
    for column in range(len(MARTIX[row])):
        if MARTIX[row][column] == 0:
            count +=1
            
print(count)        



"""EXERCISE 3: """
def add_matrices(mat1, mat2):
    res = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])
        res.append(row)
    
    return res

m1 = [[0,5,1],
      [4,9,0],
      [0,6,0]]

m2 = [[5,5,1],
      [2,8,1],
      [9,2,6]]

result = add_matrices(m1, m2)

for row in result :
    for num in row:    
        print(num,end=" ")
    print()


"""EXERCISE 4: """
rows = int(input("Enter numbre of rows: "))
for row in range(rows):
    for column in range(rows):
        if row <= column:
            print(1, end="  ")
        else:
            print(0, end="  ")
    print()



"""EXERCISE 5: """
def count_matrices(mat1):
    count = 0 
    for i in range(len(mat1)):
        for j in range(len(mat1[i])):
            count += mat1[i][j]   
    return count

m1 = [[0,0,1],
      [0,1,0],
      [0,90,0]]

print(count_matrices(m1))


## Ditionaries
"""EXERCISE 1: """

D = {1:{'name':'John' , 'age':27 , 'sex':'Male'} ,
     2:{'name':'Maria', 'age':22 , 'sex':'Female'} ,
     3:{'name':'Slim' , 'age':23 , 'sex':'Female'} ,
        }
for i in D.values():
    if i['age'] > 22:
        print(i['name'])












