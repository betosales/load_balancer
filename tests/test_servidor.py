from unittest import TestCase

from models.Servidor import Servidor
from models.Usuario import Usuario


class TestServidor(TestCase):
    def test_criar_servidor(self):
        ttask = 4
        umax = 2
        s = Servidor(ttask=ttask, umax=umax)
        self.assertEqual('<Servidor(ativo=False, space_in_server=2, consumo=0, qtd_users=0)>',
                         str(s))

    def test_criar_servidor_add_1_usuario(self):
        ttask = 4
        umax = 2
        s = Servidor(ttask=ttask, umax=umax)
        s.add_user()
        self.assertEqual('<Servidor(ativo=True, space_in_server=1, consumo=0, qtd_users=1)>',
                         str(s))

    def test_criar_servidor_add_mais_usuarios_que_o_limite(self):
        ttask = 4
        umax = 2
        s = Servidor(ttask=ttask, umax=umax)
        with self.assertRaises(AttributeError) as e:
            for i in range(4):
                s.add_user()

    def test_criar_servidor_add_2_usuarios_verifica_existencia_de_ambos(self):
        ttask = 4
        umax = 2
        s = Servidor(ttask=ttask, umax=umax)
        s.add_user()
        s.add_user()
        self.assertEqual(len(s.users), 2)

    def test_criar_servidor_add_2_usuarios_roda_2_ticks_verifica_consumo(self):
        ttask = 4
        umax = 2
        s = Servidor(ttask=ttask, umax=umax)
        s.add_user()
        s.add_user()
        s.tick()
        s.tick()
        self.assertEqual('<Servidor(ativo=True, space_in_server=0, consumo=2, qtd_users=2)>',
                         str(s))

    def test_criar_servidor_add_1_usuario_roda_4_ticks_verifica_consumo(self):
        ttask = 4
        umax = 2
        s = Servidor(ttask=ttask, umax=umax)
        s.add_user()
        for i in range(4):
            s.tick()
        self.assertEqual('<Servidor(ativo=False, space_in_server=2, consumo=4, qtd_users=0)>',
                         str(s))
