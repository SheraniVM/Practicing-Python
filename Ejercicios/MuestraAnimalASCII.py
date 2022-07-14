
from unicodedata import name


def menuAnimals():

    print("Please select an animal\n1)Dog\n2)Dolphin\n3)Cat\n4)Salir")
    opc= int(input())
    menu(opc)


def showDog():

  ascii_dog= '''
                /^ ^\ \n
               / 0 0 \ \n
               V\ Y /V \n
                / - \ \n
                |    \ \n
                || (__V \n
  '''
  print(ascii_dog)


def showDolphin():

    ascii_dolphin='''
                    ;'-. 
    `;-._        )  '---.._
      >  `-.__.-'          `'.__
     /_.-'-._         _,   ^ ---)
     `       `'------/_.'----```
                     `
    '''
    print(ascii_dolphin)


def showCat():

    ascii_cat='''
      ,-.       _,---._ __  / \
 /  )    .-'       `./ /   \
(  (   ,'            `/    /|
 \  `-"             \'\   / |
  `.              ,  \ \ /  |
   /`.          ,'-`----Y   |
  (            ;        |   '
  |  ,-.    ,-'         |  /
  |  | (   |        hjw | /
  )  |  \  `.___________|/
  `--'   `--' '''
    print(ascii_cat)


def menu(opc):

    if opc==1:
        print("*barks*")
        showDog()
    elif opc==2:
        print("*e ee e eee")
        showDolphin()
    elif opc==3:
        print(" *miau* ")
        showCat()
    else:
        print("See you later, alligator!")
    
  
def menuPrincipal():
    k=False
    while(k==False):
        menuAnimals()
        ans=input("Would you like to select another animal?\n Y/N   ")
        if(ans=='N' or ans=='n' or ans=='4'):
            break
        elif(ans=='Y' or ans=='y'):
            k=False
        else:
            print("Select a valid option, please")
menuPrincipal()        