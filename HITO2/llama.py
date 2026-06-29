import requests

def llamar_llama(prompt):
    respuesta = requests.post("http://localhost:11434/api/generate", json={
        "model":"llama3.2", "prompt": f"Tienes que resumir el siguiente texto:{prompt}","stream":False
    })
    return respuesta.json()["response"]


def clasificar_texto(texto):
    try:
        respuesta= requests.post("http://localhost:11434/api/generate",json={
        "model":"llama3.2", "prompt":f"Clasificame el texto segun tu criterio en positivo negativo o neutro{texto}", "stream":False
  
    })
        return respuesta.json()["response"]
    except Exception:
        print("Error al procesar la solicitud")

   


if __name__ == "__main__":
    print(llamar_llama("hola me gustan las patatas, jugar al futbol y videojuegos como el RDR2"))
    print(clasificar_texto("hola me gustan las patatas, jugar al futbol y videojuegos como el RDR2"))
    
