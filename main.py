'''
CONSIGLI IMPORTANTI:
 -ogni funzione deve fare poche cose, SOPRATTUTTO IL MAIN()
 -cerca di tenere le cose più separate possibili
 -una cosa alla volta e testa che tutto funzioni con print in giro
 -stai facendo tanti step in fretta, non trascurare di affinare quelli
  precedenti o viene fuori un bordello. ci vuole pratica per ogni punto,
  se passi salti gli step ci riesci inizialmente ma poi esce il bordello XDXD
  tipo i cicli le variabili i def e la logica di base, quelli devono scorrere
  via senza problemi e si ottiene solo testandosi con i loro casi più difficili
  perchè sono gli unici che ti portano a capire la natura di questi oggetti
  poco affini alla vita quotidiana. diventando fluenti in questa grammatica
  puoi attaccare nuove robe molto meglio
'''

'''
TODO list con annotazioni: da tenere aggiornata!


-PARTE I: 
XXX finire la struttura principale e consolidare i requisiti -funzioni muovi_computer_random() 
    
    -muovi_computer_mossa_migliore()
        (muovi_computer_mossa_migliore() opzionale, ma interessante per 
         fare pratica dei diversi concetti e magari provare WHILE,
         è un buon esercizio un pò macchinoso)
         
XXX modificare partita() in modo che con un parametro scelga la funzione    -chiedere all utente quale strategia adottare e usare quella
    
XXX l' utente deve visualizzare chiaramente chi ha vinto  -partita deve comunicare al main chi ha vinto

  -> esercizio da 1-2 ore
     a questo punto suggerisco di fare una tabella a penna con tutta la
     chiamata delle funzioni per 1 caso di esecuzione del programma, ovvero:
       vittoria piu semplice possibile:
       [[O,O,-], [X,X,X], [-,-,-]]
       ottenuto con funzione muovi_prima_libera
        con mosse utente (1,0), (1,1), (1,2) (tris in seconda riga)
       tabella con TUTTE le funzioni chiamate tipo:
       colonne:
       [main|intro|partita|print_tabella|muovi_utente|muovi_prima_libera|
           |chiedi_index|partita_terminata|......]
       righe:
       una singola casella con una x per riga (che rappresenta la funzione
       che viene chiamata in quel momento). Una freccia che porti
       dalla casella segnata a quella della riga dopo, annotando se il
       passaggio avviene per:
        1 la funzione prima chiama quella dopo ( tipo fun2() in qualche riga )
        2 la funzione prima termina e 'ritorna' alla funzione chiamante
        
         ( ...e anche i casi di ricorsione!!
         1b la funzione prima chiama se stessa ( tipo fun() )
         2b la funzione prima termina e 'ritorna' a se stessa
        
        quindi 2(+2) tipi di freccie!
        (noterai che la maggior parte delle
        freccie del tipo 1 puntano verso destra, e del tipo2 verso sinistra
        ma non è detto!)

       questo esercizio serve visualizzare che cazzo è un def per davvero:
       una volta va fatto secondo me, rende molto più facile la parte dopo
       -- poi così si conclude il capitolo I

###########################################################
!congratulazioni hai imparato le basi della programmazione!
###########################################################

-PARTE II: database sql e archiviazione partite giocate
obbiettivo finale:
  -> accendi il programma
  -> ti chiede se 1 vuoi giocare o 2 vuoi vedere una partita passata
  -> se 2, ti dice quante partite ci sono e chi le ha vinte o pareggio
     (tabella partite con 2 colonne, inidice e chi ha vinto)
  -> dice la percentuale di vittoria umano/computer

  (BONUS!!! parte decisamente più difficile
   -> chiede se vuoi visualizzare una partita specifica
   -> printa le N tabelle che fanno vedere la partita
  )
  
propongo intanto di partire dalla parte facile, ovvero:
 -all inizio, il main dovrà chiedere giocare o vedere partite passate
 -NUOVO FILE 'storia.py' con funzioni per il db
 -prima di leggere o scrivere sul db, bisogna creare una variabile db
  che sara quella con cui interagisci col db
  (ti conviene farla globale in main e ogni funzione che userà il db
   gliela passi come primo parametro)

poi iniziamo col db e il file storia.php
 -funzione get_db() che il main chiamera per creare l' oggetto db
  con db = get_db(); qui andarsi a vedere come inizializare un db squlite3
  get_db() dovrà controllare se il db esiste, e altrimenti crearlo e
  aggiungerci la tabella necessaria con CREATE TABLE!
 
 -funzione salva_partita(db, list) che deve prendere la lista 
  ritornata da partita() al main oltre che al db come input, e salvare
  tutta la partita del database
  QUI SERVE DECIDERE COME FARE LA TABELLA: per ora, index + vincitore basta

 -funzione get_partite(db) che ritorna la lista delle partite e chi
  le ha vinte
  (ora per vedere che tutto funziona fai stampare dal main i dati
  grezzi dell partite salvate, fai una nuova partita, e verifica
  che l' abbia aggiunta correttamente la db)
  
 -ora serve far vedere 


(!!PARTE BONUS!!)
 -il main già sa chi ha appena vinto: nella PARTE I abbiamo implementato il
  return della funzione partita con il vincitore. se vogliamo fare la parte
  BONUS, bisognerà comunicare al main non solo chi ha vinto, ma anche
  la sequenza di mosse della partita!

  (POTREBBE ESSERE un array di tabelle in questo caso modifichi solo
  la funzione partita() e nulla in _partita_.py, in modo che a ogni
  mossa si salvi l' intera tabella, e alla fine ritorni un array di
  tabelle al main. Il main dovrà salvare i dati cosi nel db (tramite
  le funzioni di storia.py), come sequenze di tabelle per ogni partita.
  OPPURE, IDEALMENTE:
  modifichi anche le funzione in _partita_.py muovi_utente(), muovi_...()
  affinche ritornino a partita() che mossa è stata fatta, tipo
  una tulpla di una stringa e un altra tulpla? ('X',(1,2)), ('O', (0,2))..
  vedi tu. alla fine serve una lista di sta roba, che è l' informazione minima
  che devi sapere per la storicizzazione.
  anzi, siccome inizia sempre la 'O' in questo caso, e si alternano, si può
  fare anche di meno. tipo una partita si puo descrivere con
  [(1,0), (0,1), (1,1), (2,1), (1,2)] => vittoria seconda riga per la 'O'
  (noterai che se la lista la lunghezza dispari vince la 'O' o pareggio,
   se è pari vince per forza la 'X')
  )
  
  quindi, il main deve ottenere la sua sequenza di mosse.

-ora queste mosse vanno salvate nel db DOPO UNA PARTITA
-devono essere visualizzate quando si chiede l'info di una partita specifica
  quindi vanno prima recuperate dal database come lista, e poi la mia idea
  è quella di aggiungere una seconda funzione in partita.py, che sarà
  partita_simulata(list), che prende come argomento la lista e 
  per ogni elemento esegue la mossa e stampa la tabella aggiornata.

 
################################################################
!congratulazioni hai imparato ad integrare un sistema con un db!
################################################################

-PARTE III: le meraviglie del DB
ora si prova con un db più complesso con multiple tabelle e incroci
tra esse, confronti e paragoni, per capire bene come cambiando il
dato osservato ciò che è 'dato' e ciò che è 'metadato' cambia.
incrociando i 'metadati' tra JOIN, INSERT, SELECT, ecc..
qui serve di vedere un modello di un db tipo quello che ho fatto per
un progetto, capire perche i dati vengono organizzati in quel modo
e com estrarne il dato utile all' occorrenza.

 ((lavori in corso..))

'''



'''IMPORTS'''
import random
from random import randrange
from partita import partita

'''FUNZIONI'''
#quelle che di sicuro ci saranno:
def intro():
    #todo messaggio iniziale
    print("Benvenuto!")

    # chiedere quale livello di difficoltà
    print("Quale livello di difficoltà preferisci?")

    #mostrare opzioni
    print("1  2  3: ", end= "")

    #utente seleziona opzione
    diff = input()
    if diff not in ['1','2','3']:
        print('livello di difficoltà non valido')
        return intro()

    return diff
#...



'''MAIN'''
def main():
    
    pref = intro()

    result = partita(pref)
    print('risultato partita: ' + result)


    #qui salveremo le partite

    exit(0)




'''chiamata del main'''
main()

