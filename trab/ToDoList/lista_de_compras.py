class ShoppingList:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price
        print(f"Produto '{name}' adicioado, preço: R${price:.2f}")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Produto '{name}' removido com sucesso.")
        else:
            print(f"Produto '{name}' não encontrado na lista de compras.")

    def show_items(self):
        if self.items:
            print("Lista de Compras:")
            print(self.items)
            for name, price in self.items.items():
                print(f"- {name}: R${price:.2f}")
        else:
            print("Sua lista de compras está vazia.")

    def calculate_total(self):
        total = sum(self.items.values())
        print(f"Total de gastos: R${total:.2f}")

def main():
    shopping_list = ShoppingList()

    while True:
        print("\nGerenciador de Lista de Compras")
        print("1 - Adicionar item")
        print("2 - Remover item")
        print("3 - Mostrar itens")
        print("4 - Calcular total de gastos")
        print("5 - Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Informe o nome do produto: ")
            try:
                price = float(input("Informe o preço do produto: "))
                shopping_list.add_item(name, price)
            except ValueError:
                print("Por favor, insira um preço válido.")
        elif choice == "2":
            name = input("Informe o nome do produto a ser removido: ")
            shopping_list.remove_item(name)
        elif choice == "3":
            shopping_list.show_items()
        elif choice == "4":
            shopping_list.calculate_total()
        elif choice == "5":
            print("Fechou o pastel")
            break
        else:
            print("Não trabalho com isso. Por favor, leia as opções.")

if __name__ == "__main__":
    main()
