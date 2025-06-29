# ChatGPTBridge.py
# Módulo Python para integración con la API de ChatGPT (OpenAI)
# REGLA #1: No modificar este archivo desde el código Kotlin/Java
import requests

def chatgpt_query(prompt, api_key):
    """Envía un prompt a la API de ChatGPT y retorna la respuesta."""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

def test_connection():
    try:
        print("Intentando conectar a Google...")
        r = requests.get("https://www.google.com")
        print("Status Google:", r.status_code)
        print("Intentando conectar a OpenAI...")
        r2 = requests.get("https://api.openai.com")
        print("Status OpenAI:", r2.status_code)
        return f"Google: {r.status_code}, OpenAI: {r2.status_code}"
    except Exception as e:
        print("Error de conexión:", e)
        return f"Error: {e}"

# Instrucciones:
# Llama a chatgpt_query(prompt, api_key) desde Kotlin usando EcoAriasPythonBridge
# Ejemplo: chatgpt_query("¿Quién eres?", "sk-...tu_api_key...") 