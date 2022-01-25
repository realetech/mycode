#!/usr/bin/env python3

def main():
    #setup star wars dictionary
    episode = {"1": "The Phantom Menance", "2": "Attack of the Clones", "3": "Revenge of the Sith", "4": "A New Hope", "5": "The Empire Strikes Back", "6": "Return of the Jedi", "7": "The Force Awakens", "8": "The Last Jedi", "9": "The Rise of Skywalker"}
    
    #set variable to user input
    favorite = input("Tell me the episode number(1-9) of Star Wars and I will tell you the name of the movie: ")

    #print favorite varialbe for debug
    print(favorite)

    if favorite > 9:
        message = 'you aren\'t a star wars fan!'
    else:
        print(episode[favorite])

main()


