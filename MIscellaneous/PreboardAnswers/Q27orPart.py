#Write a function CountVowels() in python, which should read each character 
# of a file story.txt. It shoudl then count and display the occurance of 
# vowels (both uppercase and lowercase)

def CountVowels():
    counter= 0
    H = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    F = open("Story.txt", 'r')
    G = F.read()
    for i in G:
        if i in H:
            counter += 1
        else:
            continue