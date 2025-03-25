users=["a","b","c"]
user=str(input("qual o ususario "))
while user not in users:
    user=str(input("insira um nome de usuario valido\n1.sair\n"))
    if user == "1":
        print("saiu")
        break
else :
    print(f"bem vindo {user} o que deseja")

print(user)