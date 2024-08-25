def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "maestro"
    else:
        adejetivo = "amor"
        
    print( f"Hola {nombre}, mi {adjetivo} como estás")
        
saludar("camila", "mUjeR")