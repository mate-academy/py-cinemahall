import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Wester", "Action", "Dramma"]
    actors = ["George Klooney", "Kianu Reaves", "Scarlett Keegan",
              "Will Smith", "Jaden Smith", "Scarlett Johansson"]

    for genre in genres:
        Genre.objects.create(name=genre)

    for actor in actors:
        first_name, last_name = actor.split()
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu")
    Actor.objects.filter(last_name="Reaves").update(last_name="Reeves")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")

print(main())
print(Genre.objects.all())
print(Actor.objects.all())
