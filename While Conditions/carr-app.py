"""
A car game based on the while loop 
and everything we have learnt yet. 
"""
#Declaring Command Variable 
command = ""
Started = False
#Initiating the loog 
while True: 
    command = input("> ").lower()

    #Testing for various possibilities
    if command.lower() == "start":
        if Started:
            print("The car has already started")
        else:
            Started = True
            print("The care has started successfully........")
    elif command.lower() == "stop":
        if not Started:
            print("The car is already stopped")
        else:
            Started = False
            print("The car has stopped successfully")
    elif command.lower() == "help":
        print("""
        start - To Start the car 
        stop - To stop the car
        quit - to quit 
        """)
    elif command.lower() == "quit":
        break
    else:
        print("We did not understand your command")
