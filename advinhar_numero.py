import random

print("Seja muito bem vindo ao advinhador de números")
choice_number = input("Digite um número teto do desafio: ")

if choice_number.isdigit(): 
   choice_number = int(choice_number)
else:
   print("Erro. O valor informado não é numérico.")
   quit()

random_number = random.randint(0, choice_number)

n_choices = 0

while True: 
    answer_user = input("Adivinhe o número: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)

        n_choices +=1 
        if answer_user == random_number:
            print("Acertou!")
            break  
        elif answer_user > random_number:
            print("Chutou alto, o número randomico é menor que isso...")
        else:
            print("Chutou baixo, o número randomico é maior que isso...")

    else: 
        print("Erro. O valor informado não é numérico")
        continue 

print("N de tentativas: "+ str(n_choices))