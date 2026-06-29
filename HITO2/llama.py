import requests

def llamar_llama(prompt):
    respuesta= requests.post("http://localhost:11434/api/generate", json={ "model":"llama3.2", 
                                                                          "prompt":prompt,
                                                                           "stream": False})
    
    return respuesta.json()["response"]

print(llamar_llama("dime cual es la capital de francia"))