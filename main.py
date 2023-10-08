import init_django_orm  # noqa: F401
from db.models import Genre, Actor
from django.db.models import QuerySet


def main() -> QuerySet:
    create_genres = ["Western", "Action", "Dramma"]
    for genre in create_genres:
        Genre.objects.create(name=genre)

    create_actors = (
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson")
    )

    for first_name, last_name in create_actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    update_genres = {"Dramma": "Drama"}
    for old_name, new_name in update_genres.items():
        Genre.objects.filter(name=old_name).update(name=new_name)

        Actor.objects.filter(
            last_name="Klooney"
        ).update(
            last_name="Clooney"
        )

        Actor.objects.filter(
            first_name="Kianu", last_name="Reaves"
        ).update(
            first_name="Keanu", last_name="Reeves"
        )

        Genre.objects.filter(name="Action").delete()

    delete_actors = {"first_name": "Scarlett"}
    Actor.objects.filter(**delete_actors).delete()

    last_name_is_smith = Actor.objects.filter(
        last_name="Smith").order_by("first_name")

    return last_name_is_smith
