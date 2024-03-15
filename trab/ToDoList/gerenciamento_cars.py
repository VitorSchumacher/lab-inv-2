from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo, ano, placa, preco_por_dia):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.preco_por_dia = preco_por_dia
    
    @abstractmethod
    def calcular_aluguel(self, dias):
        pass

    def __str__(self):
        return f"Modelo: {self.modelo}, Ano: {self.ano}, Placa: {self.placa}, Preço por Dia: {self.preco_por_dia}"

class Carro(Veiculo):
    def calcular_aluguel(self, dias):
        return dias * self.preco_por_dia

class Moto(Veiculo):
    def calcular_aluguel(self, dias):
        return dias * self.preco_por_dia

class Caminhao(Veiculo):
    def calcular_aluguel(self, dias):
        return dias * self.preco_por_dia

class SistemaAluguel:
    veiculos = []
    
    @staticmethod
    def adicionar_veiculo(veiculo):
        SistemaAluguel.veiculos.append(veiculo)
    
    @staticmethod
    def listar_veiculos():
        for veiculo in SistemaAluguel.veiculos:
            print(veiculo)
    
    @staticmethod
    def calcular_aluguel(placa, dias):
        for veiculo in SistemaAluguel.veiculos:
            if veiculo.placa == placa:
                return veiculo.calcular_aluguel(dias)
        return "Veículo não encontrado"

def main():
    while True:
        print("\nGerenciamento de Veículos")
        print("1. Adicionar veículo")
        print("2. Listar veículos")
        print("3. Calcular aluguel de veículo")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            tipo = input("Tipo de veículo (Carro/Moto/Caminhao): ")
            modelo = input("Modelo: ")
            ano = input("Ano: ")
            placa = input("Placa: ")
            preco_por_dia = float(input("Preço por dia: "))
            
            if tipo.lower() == 'carro':
                veiculo = Carro(modelo, ano, placa, preco_por_dia)
            elif tipo.lower() == 'moto':
                veiculo = Moto(modelo, ano, placa, preco_por_dia)
            elif tipo.lower() == 'caminhao':
                veiculo = Caminhao(modelo, ano, placa, preco_por_dia)
            else:
                print("Tipo de veículo inválido.")
                continue
            
            SistemaAluguel.adicionar_veiculo(veiculo)
            print("veículo adicionado")
        
        elif opcao == '2':
            SistemaAluguel.listar_veiculos()
        
        elif opcao == '3':
            placa = input("placa do veículo: ")
            dias = int(input("Dias de aluguel: "))
            custo = SistemaAluguel.calcular_aluguel(placa, dias)
            print(f"Custo do aluguel: {custo}")
        
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")
            
if __name__ == "__main__":
    main()
