'''IMPORTS'''
from _partita_ import *


''''''''''''''''''''''''''''''''''''''''''''''''
'''FUNZIONE PRINCIPALE CHE CHIAMERA' LE ALTRE'''
def partita(preferenza_utente):

    print_tabella()

    while True:
        muovi_utente()
        stato_vittoria = partita_terminata()
        print_tabella()
        if ( stato_vittoria != "ic" ):
            break

        if preferenza_utente == '1':
            muovi_computer_prima_libera()
        elif preferenza_utente == '2':
            muovi_computer_random()
        else:
            muovi_computer_mossa_migliore()

        stato_vittoria = partita_terminata()
        print_tabella()
        if ( stato_vittoria != "ic" ):
            break

    return stato_vittoria


''''''''''''''''''''''''''''''''''''''''''''''''