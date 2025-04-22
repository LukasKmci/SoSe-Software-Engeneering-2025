from my_classes import Subject, Supervisor, Experiment

SERVER_URL = "http://localhost:5000"

if __name__ == "__main__":

    # Erstellen eines Leistungstests
    supervisor = Supervisor("FirstName", "LastName")
    subject = Subject("FirstName", "LastName", "female", "2005-09-16")
    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest", "2021-01-01")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)


    experiment.print_info()
    
    # REST API Tests
    print("\n--- Testing REST API ---")

    create_response = subject.put(SERVER_URL)
    print(f"Created person: {create_response}")
    

    update_response = subject.update_email(SERVER_URL)
    print(f"Updated email: {update_response}")

