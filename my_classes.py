from datetime import date, datetime
import requests
import uuid

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id = str(uuid.uuid4())  # Generate unique ID for each person

    def print_info(self):
        print(f"{self.__class__.__name__}:", self.first_name, self.last_name)
    
    def put(self, server_url):
        """Create person on server"""
        person_data = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': None,
            'sex': None,
            'birthdate': None,
            'max_hr': None
        }
        response = requests.post(
            f"{server_url}/person/",
            json=person_data,
            headers={'Content-Type': 'application/json'}
        )
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
        """Update only the email field using server's expected format"""
        try:
            # First get the current person data
            get_response = requests.get(f"{server_url}/person/{self.id}")
            if get_response.status_code != 200:
                return get_response
            
            current_data = get_response.json()
            
            # Update only the email field
            update_data = {
                'id': current_data['id'],
                'first_name': current_data['first_name'],
                'last_name': current_data['last_name'],
                'email': self.email,
                # Include all other fields exactly as they were
                'sex': current_data.get('sex'),
                'birthdate': current_data.get('birthdate'),
                'max_hr': current_data.get('max_hr')
            }
            
            response = requests.put(
                f"{server_url}/person/{self.id}",
                json=update_data,
                headers={'Content-Type': 'application/json'}
            )
            return response
            
        except Exception as e:
            print(f"Update failed: {str(e)}")
            raise

    def print_info(self):
        super().print_info()
        print("Sex:", self.sex)
        print("Age:", self._calculate_age())
        print("Max HR:", self.max_hr)
        if self.email:
            print("Email:", self.email)


class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


class Experiment:
    def __init__(self, name, date_str):
        self.name = name
        self.date = datetime.strptime(date_str, "%Y-%m-%d").date()
        self.subjects = []
        self.supervisors = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_supervisor(self, supervisor):
        self.supervisors.append(supervisor)

    def print_info(self):
        print("Experiment:", self.name)
        print("Date:", self.date.strftime("%Y-%m-%d"))
        print("\nSupervisors:")
        for sup in self.supervisors:
            sup.print_info()
        print("\nSubjects:")
        for sub in self.subjects:
            sub.print_info()