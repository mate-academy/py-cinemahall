from venv import create

import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    for i in ["Western", "Action", "Dramma"]:
        Genre.objects.create(name=i)
    actors = ["George Klooney",
              "Kianu Reaves",
              "Scarlett Keegan",
              "Will Smith",
              "Jaden Smith",
              "Scarlett Johansson"]
    for i in actors:
        a_name, surname = i.split(" ")
        Actor.objects.create(first_name=a_name, last_name=surname)
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    print(Actor.objects.filter(last_name="Smith").order_by("first_name").all())
