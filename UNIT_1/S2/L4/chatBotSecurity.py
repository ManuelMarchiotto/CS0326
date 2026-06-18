import sys
from google import genai

# Inizializza il client
client = genai.Client()

# Definiamo le istruzioni di sistema
system_instruction = """
Tu sei un esperto analista di Cyber Security e un assistente di sicurezza informatica. 
Il tuo compito è aiutare l'utente a comprendere le minacce, analizzare log, suggerire best practice di hardening e scrivere script di difesa sicuri.
Rispondi in modo professionale, conciso e focalizzato sulla sicurezza. 
Se l'utente ti chiede cose non pertinenti alla Cyber Security, rifiutati gentilmente di rispondere.
"""

# PASSAGGIO CHIAVE: Usiamo types direttamente da client.chats o client.models se necessario,
# oppure passiamo direttamente la configurazione come dizionario, che l'SDK accetta nativamente!
config = {
    "system_instruction": system_instruction,
    "temperature": 0.7
}

print("Security Assistant Chatbot avviato!")
print("(Digita 'exit' o 'quit' per uscire)\n")

# Creiamo una sessione di chat persistente passando la configurazione
chat = client.chats.create(model="gemini-2.5-flash", config=config)

while True:
    try:
        user_input = input("\nTu: ")
        
        if user_input.lower() in ['exit', 'quit']:
            print("Disconnessione dall'assistente di sicurezza. Stay safe!")
            break
            
        if not user_input.strip():
            continue

        print("Assistente:...", end="\r")
        
        # Invia il messaggio nella chat
        response = chat.send_message(user_input)
        
        print(f"Assistente: {response.text}")

    except KeyboardInterrupt:
        print("\nSessione interrotta.")
        sys.exit(0)