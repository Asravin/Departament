from department import Department
from worker import Worker

class DataBase:
    department_table: list[Department]
    worker_table: list[Worker]
    
    
    def __init__(self) -> None:
        self.department_table = []
        self.worker_table = []
    
    
    def append_worker(self, worker: Worker) -> None:
        self.worker_table.append(worker)
    
    
    def append_department(seld, department: Department) -> None:
        seld.department_table.append(department)
    
    
    def select_all_department(self) -> str:
        output: str = ""
        for i in self.department_table:
            output += f'{i.title}\n'
        return output
        
    
    def select_all_worker(self) -> str:
        output = ""
        for i in self.worker_table:
            output += f'{i.full_name} {i.age}\n'
        return output
    
    
    def report(self) -> list[tuple]:
        rep: list[tuple] = []
        for i in self.worker_table:
            rep.append((i.full_name, i.age, self.department_table[i.dep_id].title))
        return rep