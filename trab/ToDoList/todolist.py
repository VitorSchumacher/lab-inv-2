class TodoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def remove_task(self, task):
        try:
            self.tasks.remove(task)
            print(f"'{task}' foi removida da lista de tarefas.")
        except ValueError:
            print("A tarefa especificada não foi encontrada.")
    def show_tasks(self):
        print(f"'{self.tasks}' é a lista de tarefas atual.")
    def clear_tasks(self):
        self.tasks.clear()

def main():
    todo_list = TodoList()
    
    while True:
        print("\nMenu da Lista de Tarefas")
        print("1 - Adicionar tarefa")
        print("2 - Remover tarefa")
        print("3 - Mostrar tarefas")
        print("4 - Limpar tarefas")
        print("5 - Sair")
        try:
            choice = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
        if choice == 1:
            task = input("Informe a tarefa a ser adicionada: ")
            todo_list.add_task(task)
        elif choice == 2:
            task = input("Informe a tarefa a ser removida: ")
            todo_list.remove_task(task)
        elif choice == 3:
            todo_list.show_tasks()
        elif choice == 4:
            todo_list.clear_tasks()
        elif choice == 5:
            print("Obrigado por usar o programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()