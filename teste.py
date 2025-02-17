filmes = [
    {"nome": "Capitão América", "categoria": "Heróis", "preço": 30.00},
    {"nome": "Chico Bento", "categoria": "Infantil", "preço": 20.00},
    {"nome": "Ainda estou aqui", "categoria": "Drama", "preço": 40.00},
    {"nome": "Acompanhante perfeita", "categoria": "Terror", "preço": 10.00}
]

def mostrarTitulo():
    print("Bem-vindo ao CineAraujo\n")

def exibirOpcoes():
    print("1. Capitão América")
    print("2. Chico Bento")
    print("3. Ainda estou aqui")
    print("4. Acompanhante perfeita")
    print("5. Sair\n")

def exibirSubTitulo(texto):
    print(texto)

def finalizarApp():
    exibirSubTitulo('Obrigado por comprar com a CineAraujo! Bom Filme!\n')
    exit()

def opcaoInvalida():
    print('\nOpção inválida!\n')
    escolherFilme()

def mostrarFilme(indice):
    filme = filmes[indice]
    nomeFilme = filme["nome"]
    categoriaFilme = filme["categoria"]
    precoFilme = filme["preço"]
    print(f"\n{nomeFilme} | {categoriaFilme} | {precoFilme:.2f} $\n")
    
    valor = formaIngresso(precoFilme) 

    mostrarFormaDePagamento(valor)
    
    voltar = input("Pressione 'v' para voltar ao menu principal: ").lower()
    if voltar == 'v':
        main()
    else:
        print("Opção inválida!")
        mostrarFilme(indice)

def formaIngresso(precoFilme):
    forma = input("Qual o tipo do ingresso? \n").lower()
    if forma == "inteira":
        valor = precoFilme
    elif forma == "meia":
        valor = precoFilme // 2
    else:
        print("Tipo de ingresso inválido")
        valor = 0
    return valor

def mostrarFormaDePagamento(valor):
    if valor == 0:
        print("Valor inválido. Tente novamente.")
        return
    
    pagamento = input("Selecione agora a forma de pagamento: ")
    if pagamento == "debito".lower():
        divide = input("Débito selecionado, você deseja dividir o pagamento?\n")
        if divide == "sim":
            quantidade = float(input("Em quantas pessoas será dividido o pagamento?\n"))
            valor_por_pessoa = valor / quantidade
            print(f"Cada pessoa vai pagar: {valor_por_pessoa:.2f} $")
            valor = valor_por_pessoa
        else:
            print(f"Total a pagar: {valor:.2f} $")
        senha = input("Insira sua senha: \n")
        confirmacao = input("Confirme sua senha: \n")
        if senha == confirmacao:
            print(f"Pagamento de {valor:.2f} $ realizado com sucesso! Boa sessão!")
            finalizarApp()
    elif pagamento == "credito".lower():
        divide = input("Crédito selecionado, você deseja dividir o pagamento?\n")
        if divide == "sim":
            quantidade = float(input("Em quantas pessoas será dividido o pagamento?\n"))
            valor_por_pessoa = valor / quantidade
            print(f"Cada pessoa vai pagar: {valor_por_pessoa:.2f} $")
            valor = valor_por_pessoa
        else:
            print(f"Total a pagar: {valor:.2f} $")
        senha = input("Insira sua senha: \n")
        confirmacao = input("Confirme sua senha: \n")
        if senha == confirmacao:
            print(f"Pagamento de {valor:.2f} $ realizado com sucesso! Boa sessão!")
            finalizarApp()
    elif pagamento == "pix".lower():
        input('Pix selecionado, informe seu CPF e te enviaremos a chave a ser paga: \n')
        print(f"Sua compra deu {valor:.2f}$ .Pagamento realizado com sucesso! Boa sessão!")
        finalizarApp()
    else:
        opcaoInvalida()

def escolherFilme():
    try:
        escolha = int(input("Escolha uma opção: "))

        if escolha in [1, 2, 3, 4]:
            mostrarFilme(escolha - 1)
        elif escolha == 5:
            finalizarApp()
        else:
            opcaoInvalida()
    except ValueError:
        opcaoInvalida()

def main():
    mostrarTitulo()
    exibirOpcoes()
    escolherFilme()

if __name__ == '__main__':
    main()