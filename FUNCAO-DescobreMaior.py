def maior(* num):
    print('-='*20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end=' ',flush=True)
    print(f'Foram informados {len(num)} valores ao todo.')
    maior = 0
    for c in range(0,len(num)):
        if num[c] > maior:
            maior = num[c]
    print(f'O maior valor informado foi {maior}')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)