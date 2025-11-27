
print('Bem-vindo ao Gerenciador de Contatos Comerciais Misael GOnçalves de Lima')

#  Lista de contatos e id_global inicializado.
#  A lista irá conter dicionários.
lista_contatos = []
id_global = 5538798 # Número de RU (Registro Único) .

# Função para cadastrar um novo contato.
def cadastrar_contato(id):

    print(f'\n--- Cadastrando Contato com ID: {id} ---')
    nome = input('Digite o nome do contato: ')
    atividade = input('Digite a atividade do contato: ')
    telefone = input('Digite o telefone do contato: ')

    # Armazena os dados em um dicionário.
    contato = {
        'id': id,
        'nome': nome,
        'atividade': atividade,
        'telefone': telefone
    }

    # Adiciona uma cópia do dicionário à lista global de contatos.
    lista_contatos.append(contato.copy())
    print('Contato cadastrado com sucesso!')

# Função para consultar contatos existentes.
def consultar_contatos():

    while True:
        print('\n--- Menu de Consulta de Contatos ---')
        print('1. Consultar Todos')
        print('2. Consultar por Id')
        print('3. Consultar por Atividade')
        print('4. Retornar ao menu')

        try:
            opcao = int(input('Escolha uma opção: '))

            # Opção 1: Consultar Todos
            if opcao == 1:
                print('\n--- Todos os Contatos ---')
                if not lista_contatos:
                    print('Nenhum contato cadastrado.')
                else:
                    for contato in lista_contatos:
                        print(f"ID: {contato['id']} | Nome: {contato['nome']} | Atividade: {contato['atividade']} | Telefone: {contato['telefone']}")

            # Opção 2: Consultar por Id
            elif opcao == 2:
                print('\n--- Consulta por ID ---')
                id_busca = int(input('Digite o ID do contato: '))
                encontrado = False
                for contato in lista_contatos:
                    if contato['id'] == id_busca:
                        print(f"ID: {contato['id']} | Nome: {contato['nome']} | Atividade: {contato['atividade']} | Telefone: {contato['telefone']}")
                        encontrado = True
                        break
                if not encontrado:
                    print('Contato com o ID especificado não encontrado.')

            # Opção 3: Consultar por Atividade
            elif opcao == 3:
                print('\n--- Consulta por Atividade ---')
                atividade_busca = input('Digite a atividade: ')
                encontrados = []
                for contato in lista_contatos:
                    if contato['atividade'].lower() == atividade_busca.lower():
                        encontrados.append(contato)

                if not encontrados:
                    print('Nenhum contato encontrado para esta atividade.')
                else:
                    for contato in encontrados:
                        print(f"ID: {contato['id']} | Nome: {contato['nome']} | Atividade: {contato['atividade']} | Telefone: {contato['telefone']}")

            # Opção 4: Retornar ao menu principal
            elif opcao == 4:
                print('Retornando ao menu principal...')
                return

            # Opção Inválida
            else:
                print('Opção inválida. Tente novamente.')

        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')

# Função para remover um contato.
def remover_contato():
    while True:
        print('\n--- Remoção de Contato ---')
        try:
            id_remover = int(input('Digite o ID do contato a ser removido: '))
            contato_encontrado = None

            # Procura o contato na lista
            for contato in lista_contatos:
                if contato['id'] == id_remover:
                    contato_encontrado = contato
                    break

            # Se encontrou, remove e encerra o loop
            if contato_encontrado:
                lista_contatos.remove(contato_encontrado)
                print('Contato removido com sucesso!')
                return
            else:
                print('Id inválido. Nenhum contato encontrado com este ID.')
                # Oferece a opção de tentar novamente ou sair
                continuar = input('Deseja tentar outro ID? (s/n): ').lower()
                if continuar != 's':
                    break
        except ValueError:
            print('Entrada inválida. Por favor, digite um número para o ID.')
            continuar = input('Deseja tentar novamente? (s/n): ').lower()
            if continuar != 's':
                break

# Estrutura de menu principal no código.
if __name__ == "__main__":
    while True:
        print('\n--- MENU PRINCIPAL ---')
        print('1. Cadastrar Contato')
        print('2. Consultar Contato(s)')
        print('3. Remover Contato')
        print('4. Encerrar Programa')

        try:
            opcao_principal = int(input('Escolha uma opção: '))

            # Opção 1: Cadastrar
            if opcao_principal == 1:
                cadastrar_contato(id_global)
                id_global += 1 # Incrementa o ID para o próximo cadastro.

            # Opção 2: Consultar
            elif opcao_principal == 2:
                consultar_contatos()

            # Opção 3: Remover
            elif opcao_principal == 3:
                remover_contato()

            # Opção 4: Encerrar
            elif opcao_principal == 4:
                print('Encerrando o programa...')

                break

            # Opção Inválida
            else:
                print('Opção inválida. Por favor, escolha uma opção de 1 a 4.')

        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')
