class Usuario:
    def __init__(self, ttask):
        self._tasks = ttask

    @property
    def ativo(self):
        return self._tasks > 0

    def tick(self):
        self._tasks -= 1

    def __repr__(self):
        return f'<Usuario(ticks_to_live={self._tasks}, ativo={self.ativo})>'
