def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade grau 1"
    elif imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"
    
def main():
    print("=== Calculadora de IMC ===")
    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    imc = calcular_imc(peso, altura)
    categoria = classificar_imc(imc)

    print(f"\n{nome}, seu IMC é {imc:.2f}.")
    print(f"Classificação: {categoria}")

if __name__ == "__main__":
    main()