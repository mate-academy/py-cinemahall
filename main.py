# import init_django_orm  # noqa: F401
#
# from django.db.models import QuerySet
# from db.models import Genre, Actor
#
#
# def main() -> QuerySet:
#     gernes_list = ["Western", "Action", "Dramma"]
#     for gerne in gernes_list:
#         Genre.objects.create(name=gerne)
#
#     actors = [["George", "Klooney"], ["Kianu", "Reaves"],
#               ["Scarlett", "Keegan"], ["Will", "Smith"],
#               ["Jaden", "Smith"], ["Scarlett", "Johansson"]]
#     for actor in actors:
#         Actor.objects.create(first_name=actor[0],
#                              last_name=actor[1])
#
#     Genre.objects.filter(name="Dramma").update(
#         name="Drama"
#     )
#     Actor.objects.filter(first_name="George").update(
#         last_name="Clooney"
#     )
#     Actor.objects.filter(first_name="Kianu").update(
#         first_name="Keanu",
#         last_name="Reeves"
#     )
#     Genre.objects.filter(name="Action").delete()
#     Actor.objects.filter(first_name="Scarlett").delete()
#     print(Actor.objects.filter(last_name="Smith").order_by(
#         "first_name"
#     ))
#
#
# if __name__ == "__main__":
#     main()
from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    list_of_genres = [
        "Western",
        "Action",
        "Dramma"
    ]
    list_of_actors = [
        "George Klooney",
        "Kianu Reaves",
        "Scarlett Keegan",
        "Will Smith",
        "Jaden Smith",
        "Scarlett Johansson"
    ]

    for genre in list_of_genres:
        Genre.objects.create(name=genre)

    list_of_actors = [
        (actor.split()[0], actor.split()[1])
        for actor in list_of_actors
    ]
    for name, surname in list_of_actors:
        Actor.objects.create(
            first_name=name,
            last_name=surname
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")

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

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")