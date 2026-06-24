import requests  

respuesta = requests.get("https://jsonplaceholder.typicode.com/posts")
datos= respuesta.json()


for post in datos:
    
    if post["userId"] == 1:
        print(post)
