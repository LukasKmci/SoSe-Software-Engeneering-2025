from datetime import date, datetime
import requests

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_info(self):
        print(f"{self.__class__.__name__}:", self.first_name, self.last_name)
    
    def put(self, server_url):
        data = {"first_name": self.first_name}
        response = requests.post(f"{server_url}/persons", json=data)
        return response


class Subject(Person):
    def __init__(self, first_name, last_name, sex, birthdate_str):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.__birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        self.max_hr = None
        self.email = None

    def _calculate_age(self):
        today = date.today()
        return today.year - self.__birthdate.year - (
            (today.month, today.day) < (self.__birthdate.month, self.__birthdate.day)
        )

    def estimate_max_hr(self):
        age = self._calculate_age()
        self.max_hr = 220 - age
    
    def update_email(self, server_url):
        data = {"email": self.email}
        response = requests.post(f"{server_url}/persons/{self.first_name}/email", json=data)
        return response

    def print_info(self):
        super().print_info()
        print("Sex:", self.sex)
        print("Age:", self._calculate_age())
        print("Max HR:", self.max_hr)


class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


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