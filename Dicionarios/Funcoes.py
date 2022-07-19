def perguntar():
    return input("O que deseja realizar?\n" +
              "<I> - Para inserir um usuário\n" +
              "<P> - Para pesquisar um usuário\n" +
              "<E> - Para excluir um usuário\n"+
              "<L> - Para listar um usuário: ").upper()
def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                      input("Digite a ultima data de acesso: "),
                                                      input("Qual a última estação acessada? ").upper()]
    salvar(dicionario)

def salvar(dicionario):
    with open("../Manipulacao_Arquivos/bd.json", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave+ ":" + str(valor))
