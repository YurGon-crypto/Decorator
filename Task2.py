class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Workers must be instances of the Worker class")

    @property
    def workers(self):
        return self._workers


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss  # Using the setter to ensure it's a Boss instance

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value):
        if isinstance(value, Boss):
            self._boss = value
            value.add_worker(self)
        else:
            raise ValueError("Boss must be an instance of the Boss class")
