import json

class ContactList:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = {}

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, number):
        if name not in self.contacts:
            self.contacts[name] = number
            self.save_contacts()
            print(f"'{name}' foi adicionado!")
        else:
            print(f"'{name}' já cadastrado")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"'{name}' foi removido!")
        else:
            print(f"Contato '{name}' não foi encontrado.")

    def find_by_name(self, name):
        if name in self.contacts:
            print(f"{name} - {self.contacts[name]}")
        else:
            print(f"'{name}' não foi encontrado.")

    def show_all_contacts(self):
        if self.contacts:
            print("Lista de Contatos:")
            for name, number in self.contacts.items():
                print(f"- {name}: {number}")
        else:
            print("Nada aqui.")

def main():
    contact_list = ContactList()

    while True:
        print("\Lista de Contatos")
        print("1 - Adicionar contato")
        print("2 - Remover contato")
        print("3 - Buscar contato pelo nome")
        print("4 - Mostrar todos os contatos")
        print("5 - Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Informe o nome: ")
            number = input("Informe o número: ")
            contact_list.add_contact(name, number)
        elif choice == "2":
            name = input("Informe o nome do contato para remover: ")
            contact_list.remove_contact(name)
        elif choice == "3":
            name = input("Informe o nome do contato: ")
            contact_list.find_by_name(name)
        elif choice == "4":
            contact_list.show_all_contacts()
        elif choice == "5":
            print("Feito o Brique.")
            break
        else:
            print("Desligando o computador, por exesso de burrice")

if __name__ == "__main__":
    main()
