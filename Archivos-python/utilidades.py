def calcular_media(lista):
     if not lista:
         return 0
     
     hola= sum(lista)/ len(lista)
     return hola
 
 
def calcular_resta(a,b):
  if not isinstance(a, (int, float)):
    raise ValueError("Los valores deben ser numéricos")
  if not isinstance(b, (int, float)):
    raise ValueError("Los valores deben ser numéricos")
  return a-b
