from datetime import date
from my_package import build_person, build_experiment

def main():
    supervisor = build_person("Lukas", "Koehler", "male", 19)

    subject = build_person("Marven", "Otto", "female", 66)

    experiment = build_experiment(
        experiment_name="Ausdauerleistung Herzfrequenz",
        date=str(date.today()),
        supervisor=supervisor,
        subject=subject
    )

    print(experiment)

if __name__ == "__main__":
    main()

