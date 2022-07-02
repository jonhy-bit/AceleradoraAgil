import json

# Checar se o arquivo existe

try:
    f = open("livros.json", "r")
    livros = json.load(f)
    f.close()

except ValueError:
    f = open("livros.json", "w")
    f.close()

except FileNotFoundError:
    f = open("livros.json", "w")
    json.dump([{"titulo": "Como fazer sentido e bater o martelo", "autor": "Alexandro Aolchique", "ano": "2017", "status": "Disponivel", "emprestado para": ""}, {"titulo": "Sejamos todos feministas", "autor": "Chimamanda Ngozi Adichie", "ano": "2015", "status": "Disponivel", "emprestado para": ""}, {"titulo": "Basquete 101", "autor": "Hort\u00eancia Marcari", "ano": "2010", "status": "Disponivel", "emprestado para": ""}], f)
    f = open("livros.json", "r")
    livros = json.load(f)
    f.close()


class Biblioteca:
    def __init__(self):
        self.livros = livros
        # Loop principal
        self.running = True

    def change_menu(self):
        # Trocar entre as funções
        opcoes = {'1': self.show_livro, '2': self.add_livro, '3': self.edit_livro, '4': self.quit}
        print('==-==' * 15)
        print('|Opções|\n[1] Mostrar Livros | [2] Adicionar Livro(s) | [3] Editar Livro(s) | [4] Sair')
        opc = str(input("Digite uma opção: "))
        print('--=--' * 15)
        opc_atual = opcoes[opc]
        opc_atual()

    def home(self):
        while self.running:
            # Menu vazio inicial
            self.change_menu()

    def show_livro(self):
        while self.running:
            # Mostrar livros
            print('=-= Livros =-=')
            for livro in self.livros:
                for info in livro.items():
                    print(f'{info[0]}: {info[1]}')
                print('=-=-=-=-=-=-=-=')

            self.change_menu()

    def add_livro(self):
        while self.running:
            # Acrescentar um livro
            creating = 'S'
            while creating == 'S':
                print('=-= Adicionando Livro: =-=')
                titulo = str(input('Titulo: '))
                autor = str(input('Autor: '))
                ano = int(input('Ano: '))
                final = {'titulo': titulo, 'autor': autor, 'ano': ano, 'status': 'Disponivel', 'emprestado para': ''}
                self.livros.append(final)
                creating = str(input('Adicionar Outro? [S/N]')).upper()

            print('=-= Livro Adicionado Com Sucesso! =-=')

            self.change_menu()

    def edit_livro(self):
        while self.running:
            # Mostrar Livros
            print('=-= Livros =-=')
            for num, livro in enumerate(self.livros):
                print(f'[{num+1}] - Livro')
                for info in livro.items():
                    print(f'{info[0]}: {info[1]}')
                print('=-=-=-=-=-=-=-=')
            # Escolher Livro
            opc = int(input("Digite o número do livro para editar: "))
            opc -= 1
            print(self.livros[opc])
            # Escolha de Edicao
            opc2 = int(input("[1] Alterar Disponibilidade | [2] Remover Livro | [3] Cancelar: "))
            if opc2 == 1:
                disp = str(input('Disponiblidade: '))
                self.livros[opc]['status'] = disp
                disp = str(input('Emprestado para: '))
                self.livros[opc]['emprestado para'] = disp
            elif opc2 == 2:
                del self.livros[opc]
            else:
                pass

            self.change_menu()

    def quit(self):
        # Salvar em um arquivo Json
        f = open("livros.json", "w")
        json.dump(self.livros, f)
        f.close()

        self.running = False


if __name__ == '__main__':
    biblioteca = Biblioteca()
    biblioteca.home()
