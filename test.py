from my_classes import Subject, Supervisor, Experiment

SERVER_URL = "http://localhost:5000"

def run_test():
    # 1. Create test objects
    supervisor = Supervisor("Alex", "Köhler")
    subject = Subject("Lukas", "Köhler", "male", "2005-05-15")
    subject.estimate_max_hr()
    subject.email = "max@example.com"
    
    # 2. Test REST API
    print("--- Testing REST API ---")
    
    # Create person
    print("Creating person...")
    create_response = subject.put(SERVER_URL)
    print(f"Status: {create_response.status_code}")
    if create_response.ok:
        print(f"Success! Person ID: {subject.id}")
    else:
        print(f"Error: {create_response.text}")
    
    # Update email
    print("\nUpdating email...")
    update_response = subject.update_email(SERVER_URL)
    print(f"Status: {update_response.status_code}")
    if update_response.ok:
        print(f"Success! Updated email to: {subject.email}")
    else:
        print(f"Error: {update_response.text}")
    
    # 3. Demonstrate experiment functionality
    print("\n--- Experiment Info ---")
    experiment = Experiment("Leistungstest", "2021-01-01")
    experiment.add_supervisor(supervisor)
    experiment.add_subject(subject)
    experiment.print_info()

if __name__ == "__main__":
    run_test()

