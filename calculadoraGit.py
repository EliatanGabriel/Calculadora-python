# Calculadora CLI Profissional

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b


def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")


def executar():
    while True:
        mostrar_menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue

        if opcao == 0:
            print("Encerrando calculadora...")
            break

        if opcao not in [1, 2, 3, 4]:
            print("Opção inválida.")
            continue

        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Use números.")
            continue

        if opcao == 1:
            resultado = somar(a, b)
        elif opcao == 2:
            resultado = subtrair(a, b)
        elif opcao == 3:
            resultado = multiplicar(a, b)
        elif opcao == 4:
            resultado = dividir(a, b)

        print(f"Resultado: {resultado}")


if __name__ == "__main__":
    executar()