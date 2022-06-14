# import init_django_orm  # noqa: F401


from db.models import Actor, Genre


def main():
    # create
    genres = ("Western", "Action", "Dramma")
    actors = (
        "George Klooney",
        "Kianu Reaves",
        "Scarlett Keegan",
        "Will Smith",
        "Jaden Smith",
        "Scarlett Johansson"
    )
    for genre_name in genres:
        Genre.objects.create(name=genre_name)
    for actor in actors:
        name, surname = actor.split()
        Actor.objects.create(
            first_name=name,
            last_name=surname
        )

    # update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    # delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == '__main__':
    main()
