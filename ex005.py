'''5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;'''

def inverter_string(s):
    # Inicializa uma string vazia para armazenar o resultado
    resultado = ""
    # Itera sobre a string original de trás para frente
    for char in s:
        resultado = char + resultado
    return resultado

# Solicita ao usuário que informe a string
string_original = input("Informe a string a ser invertida: ")

# Chama a função para inverter a string
string_invertida = inverter_string(string_original)

# Exibe o resultado
print("String invertida:", string_invertida)