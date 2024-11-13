
def calcular_media_ponderada(nota1, nota2, nota3):
    # Calculando a média ponderada
    peso1, peso2, peso3 = 1, 1, 2
    media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
    return media

def verificar_aprovacao(media):
    # Verificando se o aluno foi aprovado, em recuperação ou reprovado
    if media >= 6.0:
        return "Aprovado"
    elif media > 5.0:
        return "Recuperação"
    else:
        return "Reprovado"

# Recebendo as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calculando a média ponderada
media = calcular_media_ponderada(nota1, nota2, nota3)

# Verificando o status do aluno
status = verificar_aprovacao(media)

# Exibindo o resultado
print(f"A média ponderada das notas é: {media:.2f}")
print(f"O aluno está: {status}")

