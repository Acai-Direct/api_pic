from django.core.exceptions import ValidationError

def validate_cpf(value):
    #remover pontuação
    cpf = ''.join([char for char in value if char.isdigit()])

    #verificar se tem 11 dígitos
    if len(cpf) != 11:
        raise ValidationError("CPF inválido")
    
    # verifica se todos os digitos são iguais
    if cpf == cpf[0] * 11:
        raise ValidationError("CPF inválido")
    
    #Função para calcular os digitos verifcadores
    def calcular_digito(cpf,mutiplicadores):
        soma = sum(
            int(cpf[i]) * mutiplicadores[i]
            for i in range(len(mutiplicadores))
        )
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto
    
    #Multiplicadores para o primeiro dígito verificador
    multiplicadores_primario = list(range(10,1,-1))
    primeiro_digito = calcular_digito(cpf, multiplicadores_primario)

    #Multiplicadores para o segundo dígito verificador
    multiplicadores_segundo = list(range(11,1,-1))
    segundo_digito = calcular_digito(cpf, multiplicadores_segundo)

    #verifica se os digitos calculados são iguais aos informados
    if not (cpf[-2] == str(primeiro_digito) and cpf[-1] == str(segundo_digito)):
        raise ValidationError("CPF inválido")