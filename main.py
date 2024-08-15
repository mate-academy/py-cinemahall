import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]

    for genre in genres:
        Genre.objects.create(name=genre)

    actors = [
        {first_name: "George", last_name: "Klooney"},
        {first_name: "Kianu", last_name: "Reavse"},
        {first_name: "Scarlett", last_name: "Keegan"},
        {first_name: "Will", last_name: "Smith"},
        {first_name: "Jaden", last_name: "Smith"},
        {first_name: "Scarlett", last_name: "Johansson"},
    ]

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu", last_name="Reeves"
    )
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    smith_actors = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
    return smith_actors


if __name__ == "__main__":
    print(main())
    print(Genre.objects.all())
    print(Actor.objects.all())
