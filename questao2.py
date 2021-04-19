#Aluno: Gabriel Custodio de Moura
#Professor: Alexandre Sena

cont = contF = pos = num = 0

while True:
    sexo = input("Qual seu sexo? ")
    idade = input("Qual sua ddade? ")
    covid = input("Resultado exame covid? ")
    cont += 1;

    menor = idade;

    if idade < menor:
        menor = idade;

    if covid == 'P':
        pos += 1;
        if sexo == 'F':
            contF += 1
            num += idade



    op = input("Quer continuar? ")

    if op == "FIM":
        break;

x = pos * 100 / cont;
media = num / contF;


print(f'Porcentagem de resultados positivos : {x} %)
print(f'A idade da pessoa mais nova com o resultado positivo: {menor}')
print(f'A média entre as idades das mulheres : {media}')
    
