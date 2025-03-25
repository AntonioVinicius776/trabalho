users = []
r0 = input("Deseja adicionar usuário? (y/n): ")

if r0.lower() == "y":
    while r0.lower() == "y":
        user = input("Qual o nome de usuário?\n")
        users.append(user)
        r0 = input("Ainda deseja adicionar usuário? (y/n): ")

    while True:
        user = input("Qual o nome de usuário para login?\n1. Sair\n")
        if user == "1":
            print("Saiu")
            break
        elif user in users:
            print(f"Bem-vindo {user}, o que deseja?")
        else:
            print("Insira um nome de usuário válido.")
else:
    print("Ok")