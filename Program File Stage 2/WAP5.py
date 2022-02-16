#Form a nested list for a 4*4 matrix, accept data and display the entire matrix and also 

#initialising rows and columns 
R = 4
C = 4

#initialising matrix
matrix = []
#input
print("Enter the entries row wise:")
  
#loop for inserting entries into rows and columns
for i in range(R):         
    a =[]
    for j in range(C):      
         a.append(int(input()))
    matrix.append(a)

#loop for printing the matrix 
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()