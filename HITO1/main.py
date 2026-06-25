'SCRIPT HITO 1'
import requests




def obtener_datos():
    
    try: 
        respuesta = requests.get("https://jsonplaceholder.typicode.com/posts")

        estado= respuesta.status_code

        if estado==200:
            print("solicitud exitosa")
            return respuesta.json()  
        else:
            print("Error en la solicitud")
    except requests.RequestException:
        print("Error en la solicitud")
    
    


obtener_datos()