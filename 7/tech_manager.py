from employee import Employee
from manager import Manager
from technician import Technician


class TechManager(Manager, Technician):
    def __init__(self, name: str, id: int, *, department: str, specialization: str) -> None:
        super().__init__(name, id, department=department, specialization=specialization)

        self.managed_employees: list[Employee] = []

    def get_info(self) -> str:
        return f"TechManager: name='{self.name}' id={self.id} specialization='{self.specialization}'"

    def add_employee(self) -> None:
        self.managed_employees.append(Employee("Joe", len(self.managed_employees)))

    def get_team_info(self) -> str:
        employees_info = [employee.get_info() for employee in self.managed_employees]

        return "\n".join(
            ["-----"] + [f"{self.name}'s Team:"] + employees_info + ["-----"]
        )


tech_manager = TechManager("John", 666, department="A", specialization="---")
tech_manager.add_employee()
tech_manager.add_employee()
tech_manager.add_employee()
tech_manager.add_employee()
tech_manager.add_employee()
print(tech_manager.get_team_info())
print(tech_manager.get_info())
