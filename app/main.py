import init_django_orm  # noqa: F401

from db.models import Genre, Actor


def main():
    # CREATE

    list_of_genres = [{"name": "Western"},
                      {"name": "Action"},
                      {"name": "Dramma"}
                      ]

    for genres in list_of_genres:
        Genre.objects.create(**genres)

    list_of_actors = [
        {
            "first_name": "George",
            "last_name": "Klooney"
        },
        {
            "first_name": "Kianu",
            "last_name": "Reaves"
        },
        {
            "first_name": "Scarlett",
            "last_name": "Keegan"
        },
        {
            "first_name": "Will",
            "last_name": "Smith"
        },
        {
            "first_name": "Jaden",
            "last_name": "Smith"
        },
        {
            "first_name": "Scarlett",
            "last_name": "Johansson"
        }
    ]

    for actor in list_of_actors:
        Actor.objects.create(**actor)

    # UPDATE

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney")\
        .update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves")\
        .update(first_name="Keanu", last_name="Reeves")

    # DELETE

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # READ

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    main()
