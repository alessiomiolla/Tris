import random

'''STRUTTURA DATI DEL TRIS (corrisponde alla 'memoria')'''
tabella = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
mossa_pc = 'X'
mossa_utente = 'O'

'''FUNZIONI'''

#chiedi di inserire un numero
def chiedi_index(nome):
    print("dimmi la " + nome + " (0-1-2): ", end="")
    val = input()
    if (val not in ['0', '1', '2']):
        print("...valore non corretto...")
        return chiedi_index(nome)
    return int(val)

#chiedi la mossa utente e aggiorna tabella
def muovi_utente():

    #chiedi utente di fare mossa
    print("che mossa vuoi fare?")    
    
    #registra mossa utente
    x = chiedi_index("riga")
    y = chiedi_index("colonna")
    
    if tabella[x][y] == '-':
        #salva mossa utente sulla tabella
        ''' #per referenza tentativo tenuto XD
        for i in range(len(tabella)):
            if i == x:
                for j in range(tabella[i]):
                    if j == y:
                        tabella[i][j] ='O'
        '''
        tabella[x][y] = mossa_utente
    else:
        print("cella già occupata!")
        muovi_utente()
        
    return
        

#trova la mossa libera e aggiorna tabella
def muovi_computer_prima_libera():
    '''
    # !!! ERRORE! OPERA SU DELLE COPIE
    # DELLE CELLE E NON SULLE CELLE
    for riga in tabella:
        for cella in riga:
            if cella == '-':
                cella = mossa_pc
    '''    
    coord = (-1, -1)
    for i in range(len(tabella)): #for corretto
        for j in range(len(tabella[i])):
            if tabella[i][j] == '-':
                coord = (i, j)
                break
        if(coord != (-1, -1)):
            break

    #salvo sulla tebella
    tabella[coord[0]][coord[1]] = mossa_pc

    return


def muovi_computer_random():

    while True: #fai questa cosa all'infinito mentre while false non esegue niente
        i= random.randrange(0, 3)
        j= random.randrange(0, 3)

        if (tabella[i][j] == '-'):
            tabella[i][j] = 'X'
            break

def muovi_computer_random_due():
    coord = []
    for i in range(len(tabella)):
        for j in range(3):
            if tabella[i][j] == '-':
                coord.append((i,j))

    n = random.randrange(0, len(coord))         #numero a caso nella lista di tuple
    tabella[coord[n][0]][coord[n][1]] = 'X'     #prendo la tupla n e inserisco coordinata 0 e 1


def muovi_computer_mossa_migliore():
    #
    return

def print_tabella():
    print(".........")
    for i in range(len(tabella)):
        print('| ' + tabella[i][0] + " " + tabella[i][1] + " " + tabella[i][2] + ' |')
    print("'''''''''")
        
    return

# per controllare se e chi ha vinto la partita questa funzione
#avrà i seguenti valori di ritorno:
# 'X' -> vinto la X
# 'O' -> vinto la O
# 'p' -> patta
# 'ic' -> partita in corso
def partita_terminata():
    #controllare in qualche modo
    #se la partita è stata vinta
    #e ritornare in forma comprensibile CHI ha vinto,
    # 'O' o 'X', altrimenti '-' per non finita, 'p' per patta
    for char in [mossa_pc, mossa_utente]: #diagonali
        if (   (tabella[0][0] == char
            and tabella[1][1] == char
            and tabella[2][2] == char)
            or (tabella[0][2] == char
            and tabella[1][1] == char
            and tabella[2][0] == char) ):
            return char
        
        for i in range(len(tabella)): #row e col
            if ( tabella[i][0] == char #row
                and tabella[i][1] == char
                and tabella[i][2] == char):
                return char
            if ( tabella[0][i] == char #col
                and tabella[1][i] == char
                and tabella[2][i] == char):
                return char
    
    for x in range(len(tabella)): # in corso
        for y in range(len(tabella)):
            if tabella[x][y] == '-': 
                return 'ic'


    return 'p'