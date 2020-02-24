import json
from pprint import pprint
def pega_dados():
    with open('ano2018.json') as f:
        dados = json.load(f)
    return dados
dados2018 = pega_dados()
dados = dados2018

'''-------------------------'''

def classificacao_do_time_por_id(dados,time_id):
    lista1 = []
    flag = 0
    for x in dados['fases']['2700']['classificacao']["grupo"]["Único"]:
        lista1.append(x)
            
    

    for y in lista1:
        if y == time_id:
            return lista1.index(y) + 1

            

    
        

print(classificacao_do_time_por_id(dados,'18'))