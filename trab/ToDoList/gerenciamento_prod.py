import csv

class ProductManager:
    def __init__(self, filename='produtos.csv'):
        self.filename = filename
        self.initialize_csv()

    def initialize_csv(self):
        try:
            with open(self.filename, 'x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["nome", "preço", "quantidade"])
        except FileExistsError:
            pass

    def add_product(self, name, price, quantity):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, price, quantity])
            print("adicionado")

    def update_product(self, name, price=None, quantity=None):
        products = []
        updated = False
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == name:
                    if price is not None:
                        row[1] = price
                    if quantity is not None:
                        row[2] = quantity
                    updated = True
                products.append(row)
        if updated:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(products)
            print("atualizado")
        else:
            print("não encontrado.")

    def remove_product(self, name):
        products = []
        removed = False
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != name:
                    products.append(row)
                else:
                    removed = True
        if removed:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(products)
            print("removido")
        else:
            print("não encontrado.")

    def show_products(self):
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                print(row)

def main():
    product_manager = ProductManager()

    while True:
        print("\nGerenciamento de Produtos")
        print("1 - Adicionar produto")
        print("2 - Atualizar produto")
        print("3 - Remover produto")
        print("4 - Mostrar produtos")
        print("5 - Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("nome:")
            price = input("preço:")
            quantity = input("quantidade:")
            product_manager.add_product(name, price, quantity)
        elif choice == "2":
            name = input("nome do produto:")
            price = input("novo preco (deixe em branco para não alterar): ")
            quantity = input("nova quantidade (deixe em branco para não alterar): ")
            product_manager.update_product(name, price if price else None, quantity if quantity else None)
        elif choice == "3":
            name = input("nome do produto: ")
            product_manager.remove_product(name)
        elif choice == "4":
            product_manager.show_products()
        elif choice == "5":
            print("Até logo meu chapa")
            break
        else:
            print("Iso não existe")

if __name__ == "__main__":
    main()
