import init_django_orm  # noqa: F401

from db.models import Genre, Actor

from django.db.models import QuerySet


def main() -> QuerySet:
    genres_to_add = [
        "Western",
        "Action",
        "Dramma"
    ]
    actors_to_add = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]

    for genre in genres_to_add:
        Genre.objects.create(
            name=genre
        )

    for actor_name, actor_last_name in actors_to_add:
        Actor.objects.create(
            first_name=actor_name,
            last_name=actor_last_name
        )

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    Actor.objects.filter(
        first_name="George"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
