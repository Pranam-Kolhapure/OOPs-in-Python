class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError("Subclass must implement this method")


class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class Developer(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend


# Test - polymorphism again
employees = [
    Manager("Sanjay", 50000, 10000),
    Developer("Priya", 500, 160),
    Intern("Karan", 8000)
]

for emp in employees:
    print(f"{emp.name} ({emp.__class__.__name__}): ₹{emp.calculate_salary()}")

