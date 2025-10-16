# Verificação de Senhas Fortes
# Permita que o usuário insira senhas até digitar uma com pelo menos 8 caracteres.
# Quando isso ocorrer, exiba “Senha válida, cadastro permitido.”

while True:
    senha = input("Digite a senha: ")
    if len(senha) >= 8:
        print("Senha válida, cadastro permitido.")
        break
