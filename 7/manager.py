from employee import Employee


class Manager(Employee):
    def __init__(self, name: str, id: int, *, department: str, **kwargs) -> None:
        super().__init__(name, id, **kwargs)

        self.department = department
        self.managed_projects = []
    
    def get_info(self) -> str:
        return f"Manager: name='{self.name}' id={self.id} department={self.department}"
    
    def manage_project(self, project: object) -> None:
        self.managed_projects.append(project)
