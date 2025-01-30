import pytest
from main import *
# Teste para a função saudacao
@pytest.mark.parametrize("nome, saudacao_esperada", [("Alice", "Olá, Alice!"), ("Bob", "Olá, Bob!")])
def test_saudacao(nome, saudacao_esperada):
    assert saudacao(nome) == saudacao_esperada

# Teste para a função dobro
@pytest.mark.parametrize("numero, resultado_esperado", [(2, 4), (0, 0), (-2, -4)])
def test_dobro(numero, resultado_esperado):
    assert dobro(numero) == resultado_esperado

# Teste para a função saudacao_personalizada
@pytest.mark.parametrize("nome, idioma, saudacao_esperada", [("Alice", "inglês", "Hello, Alice!"), ("Bob", "espanhol", "Hola, Bob!"), ("Charlie", "francês", "Bonjour, Charlie!")])
def test_saudacao_personalizada(nome, idioma, saudacao_esperada):
    assert saudacao_personalizada(nome, idioma) == saudacao_esperada

# Teste para a função potencia
@pytest.mark.parametrize("base, expoente, resultado_esperado", [(2, 3, 8), (5, 2, 25), (3, 0, 1)])
def test_potencia(base, expoente, resultado_esperado):
    assert potencia(base, expoente) == resultado_esperado


# Teste para a função calcular_pagamento
@pytest.mark.parametrize("horas_trabalhadas, taxa_hora, resultado_esperado", [(40, 10, 400), (0, 15, 0), (45, 12.5, 562.5)])
def test_calcular_pagamento(horas_trabalhadas, taxa_hora, resultado_esperado):
    assert calcular_pagamento(horas_trabalhadas=horas_trabalhadas, taxa_hora=taxa_hora) == resultado_esperado