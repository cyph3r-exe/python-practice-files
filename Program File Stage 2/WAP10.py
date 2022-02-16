#Make a menu driven program to accept, delete and display the following data stored in a dictionary.
#Book_Id.........string 
#Book_Name.... string 
#Price......float 
#Discount...int 
#The program should continue as long as the user wishes to. At one point of time, I should be able to view minimum 3 records.
 
class Product:
    def GetProduct(self):
        self.book_id = input("Enter book ID: ")
        self.name_of_book = input("Enter Name : ")
        global price_of_books
        price_of_books = int(input("Enter book Price of books : "))
        disc=0
        if price_of_books >=500:
            disc=100
        else:
            disc=0

    def PutProduct(self):
        print('ID:',self.book_id,'NAME:', self.name_of_book,'COST:', price_of_books,)

    def SearchById(self, id):
        if self.book_id == id:
            return True
        else:
            return False

    def SearchByName(self, name):
        if self.name_of_book == name:
            return True
        else:
            return False

    def Purchase(self):
        print("Purchase....")

q = int(input("enter quantity of particular book you want to purchase:"))
n = int(input("Enter Total products?"))
L = []
for i in range(n):
    P = Product()
    P.GetProduct()
    L.append(P)
    while True:
        print("Main Menu\n1]Show All book\n2]Search By Id\n3]Search By Name\n4")