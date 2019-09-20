from models.Usuario import Usuario


class Servidor:
    def __init__(self, umax, ttask):
        assert (1 <= ttask <= 10)
        assert (1 <= umax <= 10)

        self._umax = umax
        self._ttask = ttask
        self._users = []
        self._consumo = 0

    def tick(self):
        for user in self._users:
            user.tick()
        self._consumo += 1
        self._users = [user for user in self._users if user.ativo]

    def add_user(self):
        if self.space_in_server > 0:
            self._users.append(Usuario(self._ttask))
        else:
            raise(AttributeError('Maximum number of users exceeded.'))

    @property
    def ativo(self):
        return len(self._users) > 0

    @property
    def space_in_server(self):
        return self._umax - len(self._users)

    @property
    def users(self):
        return self._users

    @property
    def qtd_users(self):
        return len(self._users)

    @property
    def consumo(self):
        return self._consumo

    def __repr__(self):
        return f'<Servidor(ativo={self.ativo}, space_in_server={self.space_in_server}, consumo={self.consumo}, qtd_users={self.qtd_users})>'
