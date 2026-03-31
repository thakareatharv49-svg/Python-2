class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person_details(self):
        print(f"name:{self.name},age:{self.age}")
class Employee(person):
    def __init__(self,name,age,Employee_id,salary):
        super().__init__(name,age)
        self.Employee_id=Employee_id
        self.salary=salary
    def display_Employee_details(self):
        self.display_person_details()
        print(f"Employee id:{self.Employee_id},salary:{self.salary:.2f}")
class manager(Employee):
    def __init__(self,name,age,Employee_id,salary,Department):
        super().__init__(name,age,Employee_id,salary) 
        self.Department=Department
    def display_manager_details(self):
        self.display_Employee_details()
        print(f"Department:{self.Department}")

person1=person("Aron",37)
person2=Employee("Aron",37,"12345678",60000)
person3=manager("Aron",37,"12345678",60000,"Marketing and Sales")

person1.display_person_details()
person2.display_Employee_details()
person3.display_manager_details()