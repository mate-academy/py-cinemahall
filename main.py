import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name
        )

    genres = ["Western", "Action", "Dramma"]

    for genre in genres:
        Genre.objects.create(name=genre,)

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")

    Genre.objects.filter(
        name="Action"
    ).delete()

    Actor.objects.filter(
        first_name="George",
        last_name="Klooney"
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()

    filtered_result = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    return filtered_result
