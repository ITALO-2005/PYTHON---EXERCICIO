#QUESTÃO 1
def saudacao(nome):
    print(f"Olá, {nome}!")
saudacao('Ítalo')


#QUESTÃO 2
def dobro(numero):
    return numero * 2
resultado = dobro(7)
print(resultado)


#QUESTÃO 3
def saudacao_personalizada(nome, idioma = "inglês"):
    if idioma == "inglês":
        return f"Hello, {nome}"
    elif idioma == "espanhol":
        return f"Hola, {nome}"
    elif idioma == "frânces":
        return f"Bonjour, {nome}"



#QUESTÃO 4
def potencia(base, expoente = 2):
    return base ** expoente
print(potencia(5), potencia(6, 3), potencia(10, 4))       


#QUESTÃO 9
def calcular_pagamento(horastrabalhadas, taxa_hora):
    pagamento_total = horastrabalhadas * taxa_hora
    return pagamento_total
hora = 40
taxa = 20
total = calcular_pagamento(hora, taxa)
print(total)



