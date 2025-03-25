users=[]
r0=str(input("deseja adicionar usuario "))

if r0=="y":
    user=str(input("qual o nome de usuario\n"))
    while r0 == "y" :
        users.append(user)
        r0=str(input("ainda deseja adicionar usuario "))
        if r0=="y":
            user=str(input("qual o nome de usuario\n"))
            continue
        else:
            print("ok")
        user=str(input("qual o usuario "))
        while user not in users:
            user=str(input("insira um nome de usuario valido\n1.sair\n"))
            if user == "1":
                print("saiu")
                break
        else :
            print(f"bem vindo {user} o que deseja")
else:
    print("ok")