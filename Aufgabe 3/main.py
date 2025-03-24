from datetime import date
from my_package import build_person, build_experiment

def main():
    # Supervisor erstellen
    supervisor = build_person("Max", "Mustermann", "male", 35)

    # Subject erstellen
    subject = build_person("Anna", "Schmidt", "female", 28)

    # Experiment erstellen
    experiment = build_experiment(
        experiment_name="Ausdauerleistung Herzfrequenz",
        date=str(date.today()),
        supervisor=supervisor,
        subject=subject
    )

    # Ausgabe des Experiment-Dictionaries
    print(experiment)

if __name__ == "__main__":
    main()

