# Задание

Необходимо было создать несколько классов с разными атрибутами и методами для различных типов сотрудников:

- Класс Employee с общими атрибутами и методами.
- Класс Manager с добавлением атрибутов для управления проектами.
- Класс Technician с атрибутами, связанными с техническим обслуживанием.
- Класс TechManager, который сочетает функциональность и атрибуты обоих предыдущих классов.

Также требовалось реализовать методы для добавления сотрудников в команду и вывода информации о команде.

# Реализация

## Класс Employee

В классе Employee были определены общие атрибуты для всех сотрудников: name (имя), id (идентификационный номер). Метод get_info() возвращает базовую информацию о сотруднике. Этот класс служит базой для всех других классов сотрудников.

```python
class Employee:
    def __init__(self, name: str, id: int) -> None:
        self.name = name
        self.id = id

    def get_info(self) -> str:
        return f"Employee: name='{self.name}' id={self.id}"
```

## Класс Manager

В классе Manager, который наследует от Employee, были добавлены атрибуты, специфичные для менеджера, такие как department (отдел), а также методы для управления проектами (manage_project()), который позволяет добавлять проекты в список управляемых.

```python
class Manager(Employee):
    def __init__(self, name: str, id: int, *, department: str, **kwargs) -> None:
        super().__init__(name, id, **kwargs)
        self.department = department
        self.managed_projects = []
    
    def get_info(self) -> str:
        return f"Manager: name='{self.name}' id={self.id} department={self.department}"
    
    def manage_project(self, project: object) -> None:
        self.managed_projects.append(project)
```

## Класс Technician

Класс Technician также наследует от Employee, но имеет дополнительные атрибуты, такие как specialization (специализация). Метод perform_maintenance() записывает время выполнения обслуживания.

```python
class Technician(Employee):
    def __init__(self, name: str, id: int, *, specialization: str, **kwargs) -> None:
        super().__init__(name, id, **kwargs)
        self.specialization = specialization
        self.maintenance_history = []

    def get_info(self) -> str:
        return f"Technician: name='{self.name}' id={self.id} specialization='{self.specialization}'"

    def perform_maintenance(self) -> None:
        self.maintenance_history.append(time.time())
```

## Класс TechManager

В классе TechManager объединяются атрибуты и методы как от Manager, так и от Technician. Этот класс может управлять проектами и выполнять техническое обслуживание. Метод add_employee() позволяет добавлять сотрудников в команду, а метод get_team_info() выводит информацию о всех подчинённых.

```python
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
```

# Тестирование

В процессе тестирования был создан объект класса TechManager, который добавлял сотрудников в команду и выводил информацию о команде. Пример работы программы:

```python
tech_manager = TechManager("John", 666, department="A", specialization="---")
tech_manager.add_employee()
tech_manager.add_employee()
tech_manager.add_employee()
tech_manager.add_employee()
tech_manager.add_employee()
print(tech_manager.get_team_info())
print(tech_manager.get_info())
```
