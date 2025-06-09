peso = float(input("digite seu peso em kg: "))
altura = float(input("digite sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("você esta abaixo do peso.")
elif 18.5 <= imc < 24.9:
     print("peso normal.")
elif 25 <= imc <29.9:
     print("sobrepeso.")
else:
     print("obesidade.")