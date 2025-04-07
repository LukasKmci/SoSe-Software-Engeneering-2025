class Subject:
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.max_hr = None

    def estimate_max_hr(self):
        self.max_hr = 220 - self.age

    def print_info(self):
        print("Subject:", self.first_name, self.last_name)
        print("Sex:", self.sex)
        print("Age:", self.age)
        print("Max HR:", self.max_hr)


class Supervisor:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_info(self):
        print("Supervisor:", self.first_name, self.last_name)


class Experiment:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.subjects = []
        self.supervisors = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_supervisor(self, supervisor):
        self.supervisors.append(supervisor)

    def print_info(self):
        print("Experiment:", self.name)
        print("Date:", self.date)
        print("\nSupervisors:")
        for sup in self.supervisors:
            sup.print_info()
        print("\nSubjects:")
        for sub in self.subjects:
            sub.print_info()

