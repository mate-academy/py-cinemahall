import init_django_orm  # noqa: F401
from db.models import Genre, Actor


def main():

    genres = ("Western", "Action", "Dramma")
    actors = ("George Klooney", "Kianu Reaves",
              "Scarlett Keegan", "Will Smith",
              "Jaden Smith", "Scarlett Johansson")
    for genre in genres:
        Genre.objects.create(
            name=genre
        )
    for actor in actors:
        Actor.objects.create(
            first_name=actor.split(' ')[0],
            last_name=actor.split(' ')[1],
        )
    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")
    Actor.objects.filter(
        last_name="Klooney",
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves",
    ).update(first_name="Keanu",
             last_name="Reeves")

    Genre.objects.filter(
        name="Action",
    ).delete()
    Actor.objects.filter(
        first_name="Scarlett"
    ).delete()
    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
