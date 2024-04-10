import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genre_items = ["Western", "Action", "Dramma"]
    for item in genre_items:
        Genre.objects.create(
            name=item,
        )

    actor_full_name = [("George", "Klooney"),
                       ("Kianu", "Reaves"),
                       ("Scarlett", "Keegan"),
                       ("Will", "Smith"),
                       ("Jaden", "Smith"),
                       ("Scarlett", "Johansson")]
    for first_name, last_name in actor_full_name:
        Actor.objects.create(
            first_name=first_name, last_name=last_name,
        )

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(
        name="Action"
    ).delete()
    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
