from django.db.models import QuerySet

import init_django_orm  # noqa: F401
from db.models import Genre, Actor


def main() -> QuerySet:
    # Create
    list_of_genres = ["Western", "Action", "Dramma"]
    for genre in list_of_genres:
        Genre.objects.create(name=genre)

    list_of_actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    ]
    for actor_first_name, actor_last_name in list_of_actors:
        Actor.objects.create(first_name=actor_first_name,
                             last_name=actor_last_name)

    # Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves")

    # Delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
