import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [("George", "Klooney"), ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"), ("Will", "Smith"),
              ("Jaden", "Smith"), ("Scarlett", "Johansson")]
    # Create genres
    for genre in genres:
        Genre.objects.create(name=genre)
    # Create Actors
    for name, surname in actors:
        Actor.objects.create(
            first_name=name,
            last_name=surname
        )
    # Update genres
    Genre.objects.filter(name="Dramma").update(name="Drama")
    # Update actors
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu", last_name="Reeves"
    )
    # Delete genres
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    # Read actors
    filtered_actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    return filtered_actors
