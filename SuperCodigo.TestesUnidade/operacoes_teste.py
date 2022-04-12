import unittest
from SuperCodigo.operacoes import Operacoes


class TesteOperacoes(unittest.TestCase):

    def test_triangulo_inexistente_1(self):
        op = Operacoes()
        tipo_triangulo = op.determinar_tipo_triangulo(0, 0, 0)

        self.assertEqual(tipo_triangulo, 'INEXISTENTE')

    def test_triangulo_inexistente_2(self):
        op = Operacoes()
        tipo_triangulo = op.determinar_tipo_triangulo(10, 3, 3)

        self.assertEqual(tipo_triangulo, 'INEXISTENTE')

    def test_triangulo_equilatero(self):
        op = Operacoes()
        tipo_triangulo = op.determinar_tipo_triangulo(5, 5, 5)

        self.assertEqual(tipo_triangulo, 'EQUILÁTERO')

    def test_triangulo_isoceles_1(self):
        op = Operacoes()
        tipo_triangulo = op.determinar_tipo_triangulo(5, 5, 3)

        self.assertEqual(tipo_triangulo, 'ISÓCELES')

    def test_triangulo_isoceles_2(self):
        op = Operacoes()
        tipo_triangulo = op.determinar_tipo_triangulo(3, 5, 5)

        self.assertEqual(tipo_triangulo, 'ISÓCELES')

    def test_triangulo_escaleno(self):
        op = Operacoes()
        tipo_triangulo = op.determinar_tipo_triangulo(5, 6, 7)

        self.assertEqual(tipo_triangulo, 'ESCALENO')

    def test_fibonacci_failure(self):
        op = Operacoes()
        self.assertRaises(Exception, op.obter_elemento_fibonacci, 0)

    def test_fibonacci_success_equal_2(self):
        op = Operacoes()
        elemento_fibonacci = op.obter_elemento_fibonacci(3)

        self.assertEqual(elemento_fibonacci, 2)

    def test_fibonacci_success_over_2(self):
        op = Operacoes()
        elemento_fibonacci = op.obter_elemento_fibonacci(6)

        self.assertEqual(elemento_fibonacci, 8)


if __name__ == '__main__':
    unittest.main()
