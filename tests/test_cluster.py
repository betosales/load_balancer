from unittest import TestCase

from models.Cluster import Cluster


class TestCluster(TestCase):

    def test_criar_cluster(self):
        ttask = 6
        umax = 4
        c = Cluster(ttask=ttask, umax=umax)
        self.assertEqual('<Cluster(servidores=0, consumo=0, ativo=False)>',
                         str(c))

    def test_criar_cluster_add_1_servidor(self):
        ttask = 6
        umax = 4
        c = Cluster(ttask=ttask, umax=umax)
        c.add_server()
        self.assertEqual('<Cluster(servidores=1, consumo=0, ativo=True)>',
                         str(c))

    def test_criar_cluster_add_1_usuario(self):
        ttask = 6
        umax = 4
        c = Cluster(ttask=ttask, umax=umax)
        c.add_usuarios(1)
        self.assertEqual('<Cluster(servidores=1, consumo=0, ativo=True)>',
                         str(c))

    def test_criar_cluster_add_none_usuario(self):
        ttask = 6
        umax = 4
        c = Cluster(ttask=ttask, umax=umax)
        with self.assertRaises(TypeError):
            c.add_usuarios(None)

    def test_criar_cluster_add_10_usuarios(self):
        ttask = 6
        umax = 4
        c = Cluster(ttask=ttask, umax=umax)
        c.add_usuarios(10)
        self.assertEqual('<Cluster(servidores=3, consumo=0, ativo=True)>',
                         str(c))

    def test_criar_cluster_add_10_usuarios_roda_5_ticks(self):
        ttask = 6
        umax = 4
        c = Cluster(ttask=ttask, umax=umax)
        c.add_usuarios(10)
        for i in range(5):
            c.tick()
        self.assertEqual('<Cluster(servidores=3, consumo=0, ativo=False)>',
                         str(c))

    def test_criar_cluster_add_10_usuarios_ticks_ate_zerar(self):
        ttask = 6
        umax = 4
        c = Cluster(ttask=ttask, umax=umax)
        c.add_usuarios(10)
        while c.ativo:
            c.tick()
        self.assertEqual('<Cluster(servidores=0, consumo=18, ativo=False)>',
                         str(c))

    def test_gera_resumo_do_tick(self):
        ttask = 4
        umax = 2
        c = Cluster(ttask=ttask, umax=umax)
        self.assertEqual('0', c.resumo)
        c.add_usuarios(10)
        c.tick()
        self.assertEqual('2,2,2,2,2', c.resumo)
        c.add_usuarios(1)
        c.tick()
        self.assertEqual('2,2,2,2,2,1', c.resumo)
        c.tick()
        c.add_usuarios(1)
        c.tick()
        self.assertEqual('2', c.resumo)
        c.add_usuarios(1)
        c.tick()
        self.assertEqual('1,1', c.resumo)

    def test_consumo_apos_todos_os_ticks(self):
        ttask = 4
        umax = 2
        c = Cluster(ttask=ttask, umax=umax)
        c.add_usuarios(10)
        c.tick()
        c.add_usuarios(1)
        c.tick()
        c.tick()
        c.add_usuarios(1)
        c.tick()
        c.add_usuarios(1)
        c.tick()
        self.assertEqual('20', c.consumo)
