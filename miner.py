from hashlib import sha256
import time

ZEROS = 7

def hash(texto):
    return sha256(texto.encode('ascii')).hexdigest()

def minerar(num_bloco, transacoes, hash_ant, ZEROS):
    qtd_zeros = '0' * ZEROS
    nao_achei = True
    nonce = 0
    
    while(nao_achei):
        hash_bloco = str(num_bloco) + transacoes + hash_ant + str(nonce)
        hash_atual = hash(hash_bloco)
        nonce += 1
        
        if hash_atual.startswith(qtd_zeros):
            nao_achei = False
            print(f'Eureka, nonce encontrado: {nonce}')
            return hash_atual
        
transacoes = ''

if __name__ == '__main__':
    inicio = time.time()
    print('Inicio da Mineração')
    hash_atual = minerar(770996, transacoes, '000000000000000000048a38084a820acfecaa46890dad83c4fc13afb1d3cb3c', ZEROS)
    total = str((time.time() - inicio))
    print(f'Fim da Mineração, tempo de processamento: {total}')
    print(hash_atual)