class Subject:
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.max_hr = None

    def estimate_max_hr(self):
        """Estimate the maximum heart rate using the formula: 220 - age"""
        self.max_hr = 220 - self.age
        return self.max_hr

    def __str__(self):
        return f"Subject: {self.first_name} {self.last_name}, Sex: {self.sex}, Age: {self.age}, Max HR: {self.max_hr}"


class Supervisor:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Supervisor: {self.first_name} {self.last_name}"


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

    def __str__(self):
        subject_info = "\n".join(str(s) for s in self.subjects)
        supervisor_info = "\n".join(str(s) for s in self.supervisors)
        return f"Experiment: {self.name} on {self.date}\nSupervisors:\n{supervisor_info}\nSubjects:\n{subject_info}"
