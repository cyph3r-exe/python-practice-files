print("Top movies of all time")
print("What is your genre?")
print("1. Action")
print("2. Romance")
print("3. Fiction")
print("4. Sci-fi")
print("5. Exit") 
while True:
   ch=int(input("Enter your choice: "))
   if ch==1:
      list1=["1. Top Gun", "2. Terminator", "3. Everything Everywhere All at Once"]
      print("We have the following movies in our database: ")
    
      for i in list1:
        print(i)
      
      k=int(input("Enter the movie you want to check the imdb rating of: "))
      if k==1:
         print("IMDb rating is: ")
      elif k==2:
         print("IMDb rating is: ")
      elif k==3:
         print("IMDb rating is: 8.1")

        
   elif ch==2:
      list2=["1. The notebook", "2. la la land"]
      print("We have the following movies in our database: ")
      for i in list2:
        print(i)
        
      k=int(input("Enter the movie you want to check the imdb rating of: "))
      if k==1:
         print("IMDb rating is:  8.1")
      elif k==2:
         print("IMDb rating is:  7.8")

   elif ch==3:
      list3=["1. Percy jackson", "2. Harry potter"]
      print("We have the following movies in our database: ")
      for i in list3:
        print(i)
        
      k=input("Enter the movie you want to check the IMDb rating of: ")
      if k==1:
       print("IMDb rating 8.9")
      elif k==2:
       print("IMDb rating 9.9")
      
   elif ch==4:
      list4=["1. Interstellar", "2. Avengers Endgame"]
      print("We have the following movies in our database: ")
      for i in list4:
        print(i)
      k=input("Enter the movie you want to check the IMDb rating of: ")
      if k==1:
        print("IMDb rating is 9.8")
      elif k==2:
        print("IMDb rating is 9.6")

   elif ch==5:
     list5=["exit"]
     print("you've reached the end")