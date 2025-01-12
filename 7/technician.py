from employee import Employee

import time


class Technician(Employee):
    def __init__(self, name: str, id: int, *, specialization: str, **kwargs) -> None:
        super().__init__(name, id, **kwargs)

        self.specialization = specialization
        self.maintenance_history = []

    def get_info(self) -> str:
        return f"Technician: name='{self.name}' id={self.id} specialization='{self.specialization}'"

    def perform_maintenance(self) -> None:
        self.maintenance_history.append(time.time())
