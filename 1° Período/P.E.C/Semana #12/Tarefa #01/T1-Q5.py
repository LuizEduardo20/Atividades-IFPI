def main():
    populacaoInicial = int(input())
    populacaoAtual = populacaoInicial
    ano = 1599
    
    while populacaoAtual >= 0.1 * populacaoInicial:
        nascimento = 0.01 * populacaoAtual
        mortes = 0.06 * populacaoAtual
        
        populacaoAtual = populacaoAtual + nascimento - mortes
        ano += 1
        
        print(f'{ano},{nascimento:.0f},{mortes:.0f},{populacaoAtual:.0f}')

if __name__ == '__main__':
    main()
