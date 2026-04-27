class Celular:
    def __init__(self, marca, modelo):
        self.bateria = 100
        def fazer_chamada(self, duracao):
try:
   gasto = int(duracao) * 2
   if self.bateria >= gasto:
       self.bateria -= gasto
       print(f"Chamada de {duracao} min feita! Bateria: {self.bateria}%")
   else:
       print("Bateria insuficiente.")
except ValueError:
   print("Erro: a duração deve ser um número inteiro!.")
except ZeroDivisionError:
   print("Erro: Não pode dividir por zero.")
except Exception as erro:
   print(f"Erro inesperado: {erro}")
else:
    print("sucesso! resultado:{resultado}")
finally:
    print("---Fim da divisão---")
aula_tratamento_erros()