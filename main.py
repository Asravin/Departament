from department import Department
from worker import Worker
from data_base import DataBase

department1: Department = Department(0, "Информационные техгологии")
department2: Department = Department(1, "Отдел кадров")
department3: Department = Department(2, "Бухгалтерия")

worker1: Worker = Worker(0, "Мария Хуановна", 23, 4231, 2)
worker2: Worker = Worker(1, "Сара Иосифовна", 35, 9023, 0)
worker3: Worker = Worker(2, "Борис Аркадьевич", 41, 1234, 2)
worker4: Worker = Worker(3, "Соломон Юрьевич", 28, 1234, 0)

db = DataBase = DataBase()

db.append_worker(worker1)
db.append_worker(worker2)
db.append_worker(worker3)
db.append_worker(worker4)

db.append_department(department1)
db.append_department(department2)
db.append_department(department3)

print(db.select_all_department())
print()
print(db.select_all_worker())
print()
print(db.report())