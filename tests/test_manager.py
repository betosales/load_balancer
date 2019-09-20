from unittest import TestCase

import os

from manager import ler_arquivo, cria_parametros, executa_rotina


class TestManager(TestCase):
    def test_exists_input_file(self):
        self.assertTrue(os.path.exists('../input.txt'))

    def test_ler_arquivo_input(self):
        arquivo = ler_arquivo('../input.txt')
        modelo=[4, 2, 1, 3, 0, 1, 0, 1]
        self.assertEqual(modelo, arquivo)

    def test_cria_parametros(self):
        arquivo = [4, 2, 1, 3, 0, 1, 0, 1]
        modelo_parametros = (4, 2, [1, 3, 0, 1, 0, 1])

        parametros = cria_parametros(arquivo)
        self.assertEqual(modelo_parametros, parametros)

    def test_executa_rotina(self):
        ttask, umax, usuarios = (4, 2, [1, 3, 0, 1, 0, 1])
        executa_rotina(ttask, umax, usuarios, 'output.txt')
        modelo_saida = ['1\n', '2,2\n', '2,2\n', '2,2,1\n', '1,2,1\n', '2\n', '1\n', '1\n', '0\n', '15\n']
        with open('output.txt', 'r') as arq:
            saida = [linha for linha in arq]

        self.assertEqual(modelo_saida, saida)
        os.remove('output.txt')
