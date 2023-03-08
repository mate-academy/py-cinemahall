import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [("George", "Klooney"),
              ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"),
              ("Will", "Smith"),
              ("Jaden", "Smith"),
              ("Scarlett", "Johansson")]

    for genre in genres:
        Genre.objects.create(name=genre)

    for name, surname in actors:
        Actor.objects.create(first_name=name, last_name=surname)

    Genre.objects.filter(name="Dramma").update(name="Drama")

    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")

    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Genre.objects.get(name="Action").delete()

    scarlett_ls = Actor.objects.filter(first_name="Scarlett")
    for person in scarlett_ls:
        person.delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
