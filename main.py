from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    pass
    genres = (
        "Western",
        "Action",
        "Dramma",
    )
    Genre.objects.bulk_create([Genre(name=genre) for genre in genres])

    actors = (
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    )
    Actor.objects.bulk_create([
        Actor(
            first_name=first_name,
            last_name=last_name
        ) for first_name, last_name in actors
    ])

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
