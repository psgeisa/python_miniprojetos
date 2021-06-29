# ############
# por: Geisa Pereira Souza
#######################################

from time import sleep

#Foguete
def sete_seg(d):
    print()

    if d==0: print(' _\n| |\n|_|')
    elif d==1: print(' \n |\n |')
    elif d==2: print(' _\n _|\n|_ ')
    elif d==3: print(' _\n _|\n _|')
    elif d==4: print(' \n|_|\n |')
    elif d==5: print(' _\n|_ \n _|')
    elif d==6: print(' _\n|_ \n|_|')
    elif d==7: print(' _\n |\n |')
    elif d==8: print(' _\n|_|\n|_|')
    elif d==9: print(' _\n|_|\n _|')
    return

cont = 9
while cont >= 0:
 sete_seg(cont)
 cont -= 1
 sleep(1)
print("FOGO!")
