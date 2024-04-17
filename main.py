from django.db.models import QuerySet

import init_django_orm  # noqa: F401
from db.models import Actor, Genre


def main() -> QuerySet:
    create_section()
    update_section()
    delete_section()
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


def create_section() -> None:
    genres = ("Western", "Action", "Dramma")
    for genre in genres:
        Genre.objects.create(name=genre)

    actors = (
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    )
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)


def update_section() -> None:
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )


def delete_section() -> None:
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
