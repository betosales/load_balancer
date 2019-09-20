from models.Servidor import Servidor


class Cluster:
    def __init__(self, ttask, umax):
        assert (1 <= ttask <= 10)
        assert (1 <= umax <= 10)

        self._ttask = ttask
        self._umax = umax

        self._consumo = 0
        self._servidores = []

    def tick(self):
        for server in self._servidores:
            server.tick()
            if not server.ativo:
                self._consumo += server.consumo
                self.desliga_servidores()

    def desliga_servidores(self):
        self._servidores = [server for server in self._servidores if server.ativo]

    def add_server(self):
        self._servidores.append(Servidor(ttask=self._ttask, umax=self._umax))

    def add_usuarios(self, usuarios:int):
        if not isinstance(usuarios, int):
            raise TypeError('usuarios must be integer')
        for usuario in range(usuarios):
            inserido = False
            for server in self._servidores:
                if server.space_in_server:
                    server.add_user()
                    inserido = True
                    break
            if not inserido:
                self.add_server()
                self._servidores[-1].add_user()

    @property
    def consumo(self):
        return str(self._consumo)

    @property
    def resumo(self):
        if len(self._servidores):
            return ','.join([str(server.qtd_users) for server in self._servidores])
        return '0'

    @property
    def servidores(self):
        return len(self._servidores)

    @property
    def ativo(self):
        return len(self._servidores) > 0

    def __repr__(self):
        return f'<Cluster(servidores={self.servidores}, consumo={self.consumo}, ativo={self.ativo})>'
