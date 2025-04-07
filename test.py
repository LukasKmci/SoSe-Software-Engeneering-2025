from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":
    # Erstellen eines Leistungstests
    supervisor = Supervisor("Alice", "Schmidt")
    subject = Subject("Bob", "Meier", "male", 28)
    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest", "2021-01-01")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    print(experiment)
