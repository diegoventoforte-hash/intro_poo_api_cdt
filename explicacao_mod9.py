def aula_tratamento_erros():
    print("---desafio 1:divisão---")
try:
        numerador = int(input("Digite o numerador: "))
        denominador = int(input("Digite o denominador: "))
        resultado = numerador / denominador
except ValueError:
  print("Erro: Digitar apenas número inteiros.")
except ZeroDivisionError:
    print("Erro:Não podes dividir por zero.")
except Exception as erro:
    print(f"Erro inesperado: {erro}")
else:
    print(f"Sucesso! Resultado: {resultado}")
finally:
    print("---Fim da divisão---")
    aula_tratamento_erros()
    