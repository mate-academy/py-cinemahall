import init_django_orm  # noqa: F401

from db.models import Genre
from db.models import Actor


def main():
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")
    Actor.objects.create(
        first_name="George",
        last_name="Clooney"
    )
    Actor.objects.create(
        first_name="Kianu",
        last_name="Reaves"
    )
    Actor.objects.create(
        first_name="Scarlett",
        last_name="Keegan"
    )
    Actor.objects.create(
        first_name="Will",
        last_name="Smith"
    )
    Actor.objects.create(
        first_name="Jaden",
        last_name="Smith"
    )
    Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson"
    )
    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")
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
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    query_set_result = Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")

    return query_set_result
