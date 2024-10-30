#- Crea una calcolatrice che chiede due numeri interi e un'operazione (+, -, *, /) come input e stampa il risultato. Gestisci le diverse operazioni e verifica che non ci siano divisioni per zero.
calcola=True

while calcola:
 close_or_not=int(input("Press 1 for run THE CALCULATOR or 0 for close it and skip to the next Program\n"))
 if close_or_not==0:
    calcola=False
 elif close_or_not==1:
  n1=float(input("Inserisci il primo numero: \n"))
  operatore=input("Inserisci il tipo di peratore desiderato: \n")
  n2=float(input("Inserisci il secondo numero: \n"))
  if operatore=="+":
    risultato=n1+n2
  elif operatore=="-":
    risultato=n1-n2
  elif operatore=="/":
    risultato=n1/n2
  elif operatore=="*" or operatore=="x":
    risultato=n1*n2
  else:
    print("Loperatore da te inserito non è corretto, usa +, -, * or x, /")
    continue
  print(f"Il risultato della tua operazione è \"{risultato}\"")  
 if close_or_not <0 or close_or_not > 1:
   print("INSERT ONLY 1 FOR RUN THE CALCULATOR OR 0 TO CLOSE IT!")

# - Chiedi un numero intero e stampa un messaggio che indica se il numero è pari o dispari.
print()
print("------------------- NEXT PROGRAM -----------------")
print()
close_or_not2=None

while close_or_not2!=0:
 close_or_not2=int(input("Press 1 for use FIND EVEN OR ODD or 0 for close it and skip to the next Program\n"))
 if close_or_not2==1:
   uno = int(input("Inserisci un numero intero: \n"))
   if uno%2==0:
    print("Hai inserito un numero pari")
   else:
    print("Hai inseirto un numero dispari")
 elif(close_or_not2<0 or close_or_not2>1):
  print("INSERT ONLY 1 FOR RUN THE PROGRAM OR 0 TO CLOSE IT!")    

# - Chiedi una stringa come input, converti tutto in minuscolo e conta quante vocali (a, e, i, o, u) contiene. 
print()
print("------------------- NEXT PROGRAM -----------------")
print()

calcola3=True
vocali="a,e,i,o,u"


while calcola3:
  close_or_not3=int(input("Press 1 for INSERT STRING, LOWER CONVERT and VOCAL COUNT or 0 for close it and skip to the next Program \n"))
  if close_or_not3==0:
    calcola3=False
  elif close_or_not3==1:
    strin = input("Inserisci una stringa: \n")
    new_str = strin.lower()
    conteggio_vocali = 0
    for carattere in new_str:
      if carattere in vocali:
        conteggio_vocali+=1
        print(f"Nella tua stringa \n{new_str}\n ho trovato la vocale \"{carattere}\", trovate {conteggio_vocali} vocali in totale")
  else:
   print("INSERT ONLY 1 FOR RUN THE PROGRAM OR 0 TO CLOSE IT!")  

# - Chiedi all’utente l'anno di nascita, calcola l'età e stampa un messaggio personalizzato che indica se è minorenne o maggiorenne
print()
print("------------------- NEXT PROGRAM -----------------")
print()
from datetime import datetime
year = datetime.now().year
close_or_not4 = None

while close_or_not4!=0:
  close_or_not4=int(input("Press 1 for INSERT YOUR BIRTHDAY'S YEAR, KNWO YOUR AGE AND IF YOU ARE ADULT or 0 for close it and skip to the next Program \n"))
  if close_or_not4==1:
    anno_nas=int(input("Inserisci il tuo anno di nascita:\n"))
    age = year-anno_nas
    if age>=18:
      print(f"Ciao Amico, tu hai {age} anni quindi SEI maggiorenne ! Negroni anche per te come suggerivano i compagni")
    else:
      print(f"Ciao Amico, tu hai {age} anni, NIENTE MAGGIORE ETà ANCORA PER TE ! Acqua naturale!")
  elif(close_or_not4<0 or close_or_not4>1):
   print("INSERT ONLY 1 FOR RUN THE PROGRAM OR 0 TO CLOSE IT!")  



# - Imposta una password segreta e crea un programma che chiede all'utente di inserire una password. Permetti all'utente di tentare fino a quando non inserisce la password corretta. Stampa un messaggio di accesso riuscito o negato
print()
print("------------------- NEXT PROGRAM -----------------")
print()
correct_psw = "hd23fcorrect_i24ufwfsd943rfj457k749"
psw=None

while correct_psw!=psw:
  psw=input("Ciao caro User, inserisci la pssword segreta per procedere:\n")
  if psw!=correct_psw:
    print("La password da te inserita è errata, riprova")

print("Password convalidata, Accesso in corso!!")
  

'''
Modifica il programma precedente (non tra questi precedenti)..
Ad ogni iterazione,
stampa il numero del tentativo corrente,
as esempio “Tentativo n. 1”
poi, come sempre, richiedi l'inserimento del numero,
e valuta se è corretto.
Se l'utente non indovina entro 5 tentativi,
il gioco termina, stampando un messaggio opportuno.
'''
print()
print("------------------- LAST PROGRAM -----------------")
print()

numero = 5
n_tentativi=0
print("Ora hai 5 tentativi ...")

for indovinato in range(5):
           indovinato = int(input("Qual'è il numero da indovinare?  prova ad inserirne uno da 0 a 9: \n"))
           n_tentativi+=1
           print(f"Tentativo n. {n_tentativi}")
           if numero == indovinato:
            if n_tentativi==1:
             print("Grandissimo complimenti! Al primo colpo")
            elif n_tentativi ==2:
              print("Complimenti!")
            elif n_tentativi==5:
               print("Ti è andata bene! All'ultima possibilità ma ..")   
            print(f"Hai indovinato! il numero è {numero}")
            break
           elif indovinato<0 or indovinato >9:
            print("Bisogna inserire un numero da 0 a 9 !")
           else:
            if n_tentativi==5:
               print("Numero errato ..")
            else:
             print("Numero errato, riprova.")

if numero!=indovinato:
 print("Peccato HAI PERSO! Hai superato il limite massimo di 5 tentativi. Riprova e magari sarai più fortunato")