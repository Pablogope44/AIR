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
            #return[valores["title"] for valores in datos if valores["userId"] ==1] con list comprehession
    return resultado
    
            
def mostrarResultados(datos):
    for i, titulo in enumerate(datos, 1):
        print(f"{i}. {titulo}")
#en enumerate el prmer parametro lleva la cuenta el segundo lo que se filtra
            

        
def main():
   datos=obtener_datos()            
   final=filtrarPost(datos)
  
   mostrarResultados(final)  
   
   
if __name__ == "__main__":
    main()