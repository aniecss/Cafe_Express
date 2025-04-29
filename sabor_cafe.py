cafeteria = [
    {'nome': 'Café Mania', 'proprietario': 'João Silva', 'Tipo': 'Casual', 'CNPJ': 12233445, 'ativo': True},
    {'nome': 'Cantinho do Café', 'proprietario': 'Carlos Lima', 'Tipo': 'Social', 'CNPJ': 1234567, 'ativo': False},
]

print('=' * 40)
print('CAFÉ EXPRESS'.center(40))
print('=' * 40)

def subtitulo(texto):
    linha = '=' * 20
    print(linha)
    print(texto.center(20))
    print(linha)
    print()

def menu_principal():
    print('Voltar para o Menu Principal')
    main()

def cadastrar_cafe():
    subtitulo('Cadastrar Cafeteria')
    proprietario = input('Digite o nome do proprietário: ')
    nome_cafe = input('Digite o nome da Cafeteria: ')
    cnpj = int(input('Digite o CNPJ da Cafeteria: '))
    tipo = input(f'Digite o Tipo da {nome_cafe}: ')
    ativo = input('Ativo? [S/N] ').strip().lower() == 's'

    cafe = {'nome': nome_cafe, 'proprietario': proprietario, 'Tipo': tipo, 'CNPJ': cnpj, 'ativo': ativo}
    cafeteria.append(cafe)

    print(f'{nome_cafe} cadastrado com sucesso!\n')
    menu_principal()

def listar_cafe():
    subtitulo('Listando as cafeterias\n')
    print(
        f'{"Nome da Cafeteria".ljust(25)} | {"Proprietário".ljust(20)} | {"Tipo".ljust(15)} | {"CNPJ".ljust(18)} | {"Status".ljust(10)}')
    print('-' * 100)

    for cafe in cafeteria:
        nome_cafe = cafe['nome']
        proprietario = cafe['proprietario']
        tipo_cafe = cafe['Tipo']
        cnpj_cafe = str(cafe['CNPJ'])
        ativo_cafe = 'ativado' if cafe['ativo'] else 'desativado'

        print(
            f'{nome_cafe.ljust(25)} | {proprietario.ljust(20)} | {tipo_cafe.ljust(15)} | {cnpj_cafe.ljust(18)} | {ativo_cafe.ljust(10)}')
        print()
    menu_principal()

def status():
    subtitulo('Alterando o status da Cafeteria')
    nome_cafeteria = input('Digite o nome da Cafeteria que deseja alterar o status: ')
    encontrou = False

    for cafe in cafeteria:
        if nome_cafeteria == cafe['nome']:
            cafe['ativo'] = not cafe['ativo']
            encontrou = True
            print(f'A Cafeteria {nome_cafeteria} foi alterada para {"ativada" if cafe["ativo"] else "desativada"}')
            break

    if not encontrou:
        print('A Cafeteria não foi encontrada.')

    menu_principal()

def finalizar():
    print('Finalizando...')

def opcao_invalida():
    print('Opção invalida\n')
    menu_principal()

def main():
    while True:
        print('1. Cadastrar Cafeteria')
        print('2. Listar Cafeteria')
        print('3. Ativar Cafeteria')
        print('4. Sair do programa')

        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            opcao_invalida()
            continue

        if opcao == 1:
            cadastrar_cafe()

        elif opcao == 2:
            listar_cafe()

        elif opcao == 3:
            status()

        elif opcao == 4:
            finalizar()
            break

if __name__ == '__main__':
    main()