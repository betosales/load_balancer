from unittest import TestCase

from models.Usuario import Usuario


class TestUsuario(TestCase):
    def test_criar_usuario_com_0_task(self):
        ttask = 0
        u = Usuario(ttask)
        self.assertEqual(u, '<Usuario(ticks_to_live=0, ativo=False)>')
        
    def test_criar_usuario_com_4_tasks(self):
        ttask = 4
        u = Usuario(ttask)
        self.assertEqual(u, '<Usuario(ticks_to_live=4, ativo=True)>')

    def test_criar_usuario_com_4_tasks_executa_1_tick(self):
        ttask = 4
        u = Usuario(ttask)
        u.tick()
        self.assertEqual(u, '<Usuario(ticks_to_live=3, ativo=True)>')


    def test_criar_usuario_com_4_tasks_executa_4_ticks_muda_ativo_para_false(self):
        ttask = 4
        u = Usuario(ttask)
        for i in range(4):
            u.tick()
        self.assertEqual(u, '<Usuario(ticks_to_live=0, ativo=False)>')

