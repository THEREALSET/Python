def leiaInt(a):
        while True:
            try:
                res = int(input(a)) 
            except KeyboardInterrupt:
                print('O usuário preferiu não informar dados!')
                return 0
                break    
            except:
                print('Erro ')            
            else:
                return res
                break

def leiaFloat(a):
    while True:
        try:
            res = float(input(a))
        except KeyboardInterrupt:
            print('O usuário preferiu não informar dados!')
            return 0
            break
        except:
            print('Erro ')      
        else:
            return res
            break
cod = leiaInt('Digite um Inteiro: ') 
cod2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {cod} e o real foi {cod2}')   