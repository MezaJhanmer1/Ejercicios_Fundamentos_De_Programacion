#Ejercicio 05 - Validar correo

def validar_dominio(email):
    
    email_limpio = email.strip().lower()        #quita espacios + minusculas

    if "@" in email_limpio:
        
        partes = email_limpio.split("@")        # corta en 2 partes (usuario + @ + dominio) ["juan.perez", "gmail.com"]
        dominio = partes[1]                     # pedimos q guarde el 2do elemento [1]
        
        if "." in dominio:                      # el DOMINIO tenga un punto (para el .com, .net, etc.)
            return dominio

    return "Email no válido"         # Si falta el '@' o el dominio no tiene ".", no es válido


print(validar_dominio("  Juan.PerEZ@GmaIl.com  "))
print(validar_dominio("  Juan_15_tlv@GmaIl.COM  "))   
print(validar_dominio("juan.perEZ@gmail"))  