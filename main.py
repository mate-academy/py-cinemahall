from django.db.models import QuerySet

import init_django_orm  # noqa: F401

from db.models import Actor, Genre


def main() -> QuerySet:
    genres_to_create = ["Western", "Action", "Dramma"]
    actors_to_create = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    # CREATE
    for genre in genres_to_create:
        Genre.objects.create(name=genre)

    for actor in actors_to_create:
        Actor.objects.create(first_name=actor[0], last_name=actor[1])

    # UPDATE
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )

    # DELETE
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # RETRIEVE
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
