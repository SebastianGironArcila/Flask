# valida el codigo si es numerico y de longitud 6
def validar_codigo(codigo: str) -> bool:
    return (codigo.isnumeric() and len(codigo) ==6)


# validar el nombre si es un texto sin espacios en blanco entre 1 y 30 caracteres
def validar_nombre(nombre: str) -> bool:
    nombre = nombre.strip()
    return (len(nombre) > 0 and len(nombre) <=30)

# valida que los credtios esten entre 1 y 9
def validar_creditos(creditos: str) -> bool:
    creditos_texto = str(creditos)
    if creditos_texto.isnumeric():
        return (creditos >=1 and creditos <= 9)
    else:
        return False
