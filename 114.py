while True:
    print('-'*30)
    print('       MENU PRINCIPAL       ')
    print('-'*30)
    print('1 - Ver pessoas cadastradas ')
    print('2 - Cadastrar nova Pessoa ')
    print('3 - Sair do Sistema ')
    print('-'*30)

    while True:
        try:
            op = int(input('Sua Opção: '))
            if op in [1, 2, 3]:
                break
            else:
                print('[ERRO] Digite uma das 3 opções! ')
        except:
            print('[ERRO] Digite um opção válida! ')
            break
    
    if op == 3:
        print('-'*30)
        print('Saindo do sistema... Até logo!')
        print('-'*30)
        break

    if op == 1:
        abr = open('cadastrados.txt', 'r')
        print('-'*30)
        print('      PESSOAS CADASTRADAS     ')
        print('-'*30)
        cadastradas = abr.read()
        print(cadastradas)
        abr.close()

    if op == 2:
        abr = open('cadastrados.txt', 'a')
        print('-'*30)
        print('       NOVO CADASTRO         ')
        print('-'*30)
        while True:
            try:
                name = str(input('Nome: ')).strip()
                if name.replace(' ', '').isalpha():
                    break
                else:
                    print('[ERRO] Digite um nome! ')
            except:
                print('[ERRO] Digite corretamente! ')
        nome = name.split()
        nome_formatado = ' '.join(nome)

        while True:
            try:
                yea = int(input('Idade: '))
                if yea < 0:
                    print('[ERRO] A idade não pode ser menor do que 0! ')
            except:
                print('[ERRO] Digite um número válido! ')
            else:
                break
        abr.write(f'{nome_formatado}    {yea} anos\n')
        abr.close()
        print(f'Novo registro de {nome_formatado} adicionado.')