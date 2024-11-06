#Como calcular a média aritmética de 2 notas:
n1=float(input("Insira a sua 1° nota:\n"))
n2=float(input("Insira a sua 2° nota:\n"))
n3=(n1+n2)/2
print(f"A sua média aritmética é:\n{n3}")
if(n3>=7):
    print("Parabéns! Vocẽ é muto esforçado :D")
else:
    if(n3>=5):
        print("Que pena! Você só precisa de um pequeno esforço a mais. :|")
    else:
        print("Eita! Você precisa estudar muito mais para poder passar :(")