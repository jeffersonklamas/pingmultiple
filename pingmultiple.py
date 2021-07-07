################################################################################
#                                                                              #
# Código simples para verificação de Múltiplos Ping                            #
#                                                                              #
################################################################################
# Importando Bibliotecas
import os
import time                             # irá trabalhar com o tempo de execução.


# Limpa tela ao iniciar a execução.
os.system('clear') or None

# Abrindo arquivo auxiliar com os múltiplos hosts e pings a serem verificados

with open('hosts.txt') as file:
    dump = file.read()         # Lendo o arquivo e jogando as informações dentro do dump.
    dump = dump.splitlines()   # Inserindo em linhas separadas o resultado do dump.
    
    for ip in dump:            # Para cada ip no dump, será printado os valores correspondentes.
        print('=' * 100)       # Decoração.
        print('Verificando o ip: ', ip)
        print('-' * 100)       # Decoração.
        os.system('ping -c 2 {}'.format(ip)) # Irá enviar dois pacotes no n 2.
        print('-' * 100)       # Decoração.
        time.sleep(5)          # Espera de 5 segundos para verificar outro ip.      
