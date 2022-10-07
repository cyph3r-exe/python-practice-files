import pickle

#trying to input data into a binary file 
L = ["Debangshu Roy", "Name2", 27, 500.0, "good done"]

F = open("random.dat", 'ab')
pickle.dump(L, F)
