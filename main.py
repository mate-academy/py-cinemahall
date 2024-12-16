import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    lists_genre = ["Western", "Action", "Dramma"]
    lists_actor = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for genre in lists_genre:
        Genre.objects.create(name=genre)

    for actor in lists_actor:
        first_name, last_name = actor
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves",
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(name="Action").delete()

    for actor in lists_actor:
        first_name, last_name = actor
        if first_name == "Scarlett":
            Actor.objects.filter(first_name=first_name).delete()

    return Actor.objects.filter(last_name="Smith").all().order_by("first_name")
