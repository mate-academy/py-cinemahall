import init_django_orm  # noqa: F401
from db.models import Actor, Genre


def main():
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(name=genre)
    actors = [
        "George Klooney",
        "Kianu Reaves",
        "Scarlett Keegan",
        "Will Smith",
        "Jaden Smith",
        "Scarlett Johansson"
    ]
    for actor in actors:
        first_name, last_name = actor.split()
        Actor.objects.create(first_name=first_name, last_name=last_name)
    # change incorrect values
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")
    # delete some data
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()
    query_res = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return query_res


if __name__ == "__main__":
    main()
