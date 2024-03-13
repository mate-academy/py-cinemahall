import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre
from db.models import Actor


def main() -> QuerySet:
    list_of_genres = ["Western", "Action", "Dramma"]

    for name_of_genre in list_of_genres:
        Genre.objects.create(name=name_of_genre)

    actor_and_actresses_names = (
        "George",
        "Kianu",
        "Scarlett",
        "Will",
        "Jaden",
        "Scarlett"
    )
    actor_and_actresses_surnames = (
        "Klooney",
        "Reaves",
        "Keegan",
        "Smith",
        "Smith",
        "Johansson"
    )

    for first_name, last_name in zip(
            actor_and_actresses_names,
            actor_and_actresses_surnames
    ):
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(first_name="George", last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
