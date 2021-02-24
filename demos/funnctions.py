def hello(*petsNames):
    print("my pet names are " + petsNames[2])
    #option return


hello("Meg", "Pepper", "Lex")


def hello(pet1,pet2="Teal",pet3):
    print("my pet names are " + petsNames[2])
    return pet2


hello(pet3="Meg",  pet1="Lex")



addItem = lambda itemone : itemone  +  45
print(addItem(5))

