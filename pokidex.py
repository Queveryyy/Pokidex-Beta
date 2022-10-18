from tkinter import *

quev=Tk()


#def statements


def p1():
    print('\nWhat is it?: Pikachu is a electric type pokemon.\n \nMoveset?: It has many moves ranging from Thunderbolts to iron tales! \n \nWhere can i find it?: Pikachu can be found near the mountains in the Kanto Region!')

def p2():
    print('\nWhat is it?: Charmander is a fire type pokemon. \n \nMoveset: It has a span of different types of moves ranging from embers to flamethrowers! \n \nWhere can i fint it?: Charmander can be found in the Sandsear Cave, Typhlo Cavern, and Volcanic Cave areas!')

def p3():
    print('\nWhat is it?: Squirtle is a water type pokemon, \n \nMoveset: it has a stretch of different types of moves that vary from Bubble to Aqua Tail! \n \nWhere can i find it?: Squirtle can be found in the Seafoam Islands making it thhe best natuarl catch!')

def p4():
    print('\nWhat is it!: Bulbasaur is a leaf type pokemon, \n \nMoveset: it has a span of different types of moves that vary from leaf blows to sun beams! \n \nWhere can  i find it?: Bulbasaur can also be found in the forests!')

def c1():
    print('testing')
    
def c2():
    print('testing')

def c3():
    print('testing')

def c4():
    print('tesing')


#variables!

#or colors!


yellow = '#FFFF00'
blue = '#008080'
red = '#DC143C'



#buttons!

pokemon1 = Button(quev, text='Pikachu!', command=p1, bg='yellow', fg='black')
pokemon1.grid(row=0, column=0)

pokemon2 = Button(quev, text='Charmander!', bg=red, fg='yellow', command=p2)
pokemon2.grid(row=1, column=2)

pokemon3 = Button(quev, text='Squirtle!', bg='blue', command=p3, fg='yellow')
pokemon3.grid(row=0, column=3)

pokemon4 = Button(quev, text='Bulbasaur!' , bg='green', command=p4, fg='lime')
pokemon4.grid(row=1, column=4)


c1 = Checkbutton(quev, text='What is it?', bg='orange', command=c1)
c1.grid(row=10, column=0)

c2 = Checkbutton(quev, text='Moveset?', bg='orange', command=c2)
c2.grid(row=55, column=3)

c3 = Checkbutton(quev, text='Where can i find it?', bg='orange', command=c3)
c3.grid(row=100, column=4)

c4 = Checkbutton(quev, text='Fun Facts!', bg='orange', command=c4)
c4.grid(row=50, column=2)


#quevs!


quev.title("Pokidex By quev")
quev.minsize(width=250, height=300)
quev.configure(background='orange')


quev.mainloop()