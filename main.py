import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    Genre.objects.bulk_create(
        [
            Genre(name="Western"),
            Genre(name="Action"),
            Genre(name="Dramma")
        ]
    )
    Actor.objects.bulk_create(
        [
            Actor(first_name="George", last_name="Klonney"),
            Actor(first_name="Kianu", last_name="Reaves"),
            Actor(first_name="Scarlett", last_name="Keegan"),
            Actor(first_name="Will", last_name="Smith"),
            Actor(first_name="Jaden", last_name="Smith"),
            Actor(first_name="Scarlett", last_name="Johansson")
        ]
    )
    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")
    Actor.objects.filter(
        last_name="Klonney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")
    Genre.objects.filter(
        name="Action"
    ).delete()
    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).all().order_by("first_name")
