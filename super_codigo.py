class Operacoes:

    def __init__(self):
        self.CADEIA_CARACTERES_CADEIA_INVALIDA = 'Cadeia Inválida'
        self.CADEIA_CARACTERES_CARACTERE_INVALIDA = 'Caractere Inválida'
        self.FIBONACCI_MAIOR_QUE_ZERO = 'n deve ser maior que zero'

    def obter_posicao_caractere(self, cadeia: str, caractere: str):
        if len(cadeia) == 0 or len(cadeia) > 20:
            raise Exception(self.CADEIA_CARACTERES_CADEIA_INVALIDA)
        if len(caractere) != 1:
            raise Exception(self.CADEIA_CARACTERES_CARACTERE_INVALIDA)
        for i in range(1, len(cadeia) + 1):
            if cadeia[i-1] == caractere:
                return i
        return -1

    def obter_elemento_fibonacci(self, n: int):
        if n < 1:
            raise Exception(self.FIBONACCI_MAIOR_QUE_ZERO)

        elemento_anterior_1 = 1
        elemento_anterior_2 = 1
        elemento_atual = elemento_anterior_1

        if n == 2:
            elemento_atual = elemento_anterior_1
        else:
            for i in range(3, n + 1):
                elemento_atual = elemento_anterior_1 + elemento_anterior_2
                elemento_anterior_1 = elemento_anterior_2
                elemento_anterior_2 = elemento_atual

        return elemento_atual

    @staticmethod
    def determinar_tipo_triangulo(a: int, b: int, c: int):
        tipo = 'ESCALENO'

        if a <= 0 or b <= 0 or c <= 0:
            tipo = 'INEXISTENTE'
        else:
            if not (a + b > c and a + c > b and b + c > a):
                tipo = 'INEXISTENTE'
            else:
                if a == b:
                    tipo = 'ISÓCELES'
                    if b == c:
                        tipo = 'EQUILÁTERO'
                else:
                    if b == c or a == c:
                        tipo = 'ISÓCELES'

        return tipo


if __name__ == '__main__':
    op = Operacoes()

    posicao_caractere = op.obter_posicao_caractere('abcdefgh', 'a')
    print(f'\n1. Posição caractere: {posicao_caractere}')

    elemento = 6
    fibonnaci = op.obter_elemento_fibonacci(elemento)
    print(f'\n2. Elemento {elemento} de Fibonacci: {fibonnaci}')

    tipo_triangulo = op.determinar_tipo_triangulo(10, 20, 3)
    print(f'\n3. Triângulo tipo {tipo_triangulo}')
