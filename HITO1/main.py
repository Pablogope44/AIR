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
            return None
    except requests.RequestException:
        print("Error en la solicitud")
    
    



    


def filtrarPost(datos):
    resultado=[]
    for valores in datos:
        if valores["userId"]==1:
            resultado.append(valores["title"])
            'return[valores["title"] for valores in datos if valores["userId"] ==1]
    return resultado
    
            
        
            
datos=obtener_datos()            
final=filtrarPost(datos)
print(final)            