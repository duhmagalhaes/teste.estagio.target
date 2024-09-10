'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;'''

import json

# Função para adicionar novos dados ao arquivo JSON
def adicionar_faturamento(dia, valor, filename='faturamento.json'):
    try:
        with open(filename, 'r+') as file:
            # Carregar os dados existentes
            dados = json.load(file)
            # Adicionar novos dados
            dados.append({"dia": dia, "valor": valor})
            # Voltar ao início do arquivo
            file.seek(0)
            # Salvar os dados atualizados
            json.dump(dados, file, indent=4)
    except FileNotFoundError:
        # Se o arquivo não existir, criar um novo
        with open(filename, 'w') as file:
            dados = [{"dia": dia, "valor": valor}]
            json.dump(dados, file, indent=4)

# Função para calcular os resultados
def calcular_faturamento(filename='faturamento.json'):
    with open(filename, 'r') as file:
        dados = json.load(file)
    
    faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_mensal = sum(faturamentos) / len(faturamentos)
    dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

    print(f"Menor valor de faturamento: {menor_faturamento}")
    print(f"Maior valor de faturamento: {maior_faturamento}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

# Função principal para solicitar dados do usuário
def main():
    while True:
        dia = int(input("Informe o dia do mês: "))
        valor = float(input("Informe o valor de faturamento: "))
        adicionar_faturamento(dia, valor)
        
        continuar = input("Deseja adicionar mais dados? (s/n): ").strip().lower()
        if continuar != 's':
            break

    calcular_faturamento()

# Executar a função principal
if __name__ == "__main__":
    main()