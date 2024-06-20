import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    pass
    genres = [
        "Western",
        "Actions",
        "Dramma",
    ]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for genre in genres:
        Genre.objects.create(name=genre)

    for actor in actors:
        first_name, last_name = actor
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")

    Actor.objects.filter(
        first_name="George",
        last_name="Klooney",
    ).update(first_name="George", last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves",
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(
        name="Actions",
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett",
    ).delete()

    return Actor.objects.filter(
        last_name="Smith",
    ).order_by("first_name")


if __name__ == "__main__":
    main()
