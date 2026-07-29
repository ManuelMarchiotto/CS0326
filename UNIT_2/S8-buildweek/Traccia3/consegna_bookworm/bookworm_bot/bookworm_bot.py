import sys
from groq import Groq

# ==========================================================
# Inserisci la tua API Key di Groq (gsk_...)
# ==========================================================
API_KEY = "METTI LA API KEY QUì" 
# ==========================================================

client = Groq(api_key=API_KEY)

def bookworm_assistant():
    print("\n📚 BOOKWORM - ASSISTENTE BIBLIOTECARIO")
    print("======================================")
    print("🔍 Test connessione API Groq in corso...")

    # TEST DI CONNESSIONE
    try:
        test = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": "Rispondi solo 'Connesso'"}]
        )
        print(" ✅ Connessione API riuscita!\n")
    except Exception as e:
        print(f"❌ ERRORE: {e}")
        return

    # ==========================================================
    # LA VULNERABILITÀ (LLM01: Prompt Injection) 
    # ==========================================================
    # Il System Prompt viene costruito come una semplice stringa.
    # Se l'utente scrive "Ignora le istruzioni precedenti...", l'LLM obbedirà.
    system_prompt = "Sei un bibliotecario esperto. Devi consigliare libri all'utente."

    while True:
        print("\n----------------------------------")
        user_input = input("📖 Di che genere o argomento vuoi un libro? (scrivi 'esci' per uscire): ").strip()
        
        if user_input.lower() in ['esci', 'quit', 'exit']:
            print("👋 Arrivederci.")
            break
        
        if not user_input:
            continue

        print(f"\n⏳ Sto cercando un libro su '{user_input}'...\n")
        
        try:
            # La vulnerabilità è qui: l'input dell'utente viene messo in un messaggio "user"
            # insieme a un system prompt debole. L'utente può fare "Prompt Injection".
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt}, # Istruzione iniziale
                    {"role": "user", "content": user_input}       # L'utente la sovrascrive
                ]
            )
            
            print("📘 IL MIO CONSIGLIO:")
            print("==================")
            print(response.choices[0].message.content)
            print("==================\n")
            
        except Exception as e:
            print(f"❌ Errore: {e}")

if __name__ == "__main__":
    bookworm_assistant()
