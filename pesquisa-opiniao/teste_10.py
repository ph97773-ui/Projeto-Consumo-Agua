"""Teste simples com 10 entrevistados."""
from unittest.mock import patch
from app import realizar_pesquisa


respostas = []
for numero in range(1, 11):
    respostas.extend([f"Pessoa {numero}", str(18 + numero), "1" if numero <= 4 else "3" if numero <= 6 else "2"])

with patch("builtins.input", side_effect=respostas):
    excelentes, ruins = realizar_pesquisa(10)

assert excelentes == 4
assert ruins == 2
print("\nTeste com 10 entrevistados realizado com sucesso!")
print("Esperado: 4 excelentes e 2 ruins.")
