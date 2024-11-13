
def calcular_media(nota1, nota2, nota3):
    # Calculando a média simples
    media = (nota1 + nota2 + nota3) / 3
    return media

def verificar_aprovacao(media):
    # Verificando se o aluno foi aprovado ou reprovado
    if media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"

# Recebendo as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calculando a média
media = calcular_media(nota1, nota2, nota3)

# Verificando a aprovação
status = verificar_aprovacao(media)

# Exibindo o resultado
print(f"A média das notas é: {media:.2f}")
print(f"O aluno está: {status}")

