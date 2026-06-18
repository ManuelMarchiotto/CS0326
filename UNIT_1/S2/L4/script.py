import os
from google import genai

# Il client recupera automaticamente la variabile d'ambiente GEMINI_API_KEY
client = genai.Client()

print("Inviando il prompt a Gemini...")

# Chiamata base usando il modello consigliato per task veloci
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Ciao Gemini! Sei pronto ad aiutarmi con la Cyber Security oggi?",
)

print("\n--- Risposta di Gemini ---")
print(response.text)
print("--------------------------")