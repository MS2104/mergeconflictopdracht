import newgreeting
import random
print("merge oefening leuk!")

newgreeting.greet()




def basicHaiku():
    return ["Toward those short trees.","Dit is een verandering","On a day in spring."]

#zet hier je haiku functie neer, zie https://github.com/progsen/haikugitopdracht voor ideeen

haikus = [
    basicHaiku()
]

def randomHaiku():
    return random.choice(haikus)

def start():
    print("starting main")
    
    print(randomHaiku())

    pass


start()