import init_django_orm  # noqa: F401
from db.models import Genre, Actors


def main():
    # Create Genres
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")
    # Create Actors
    Actors.objects.create(first_name="George", last_name="Klooney", )
    Actors.objects.create(first_name="Kianu", last_name="Reaves", )
    Actors.objects.create(first_name="Scarlett", last_name="Keegan", )
    Actors.objects.create(first_name="Will", last_name="Smith", )
    Actors.objects.create(first_name="Jaden", last_name="Smith")
    Actors.objects.create(first_name="Scarlett", last_name="Johansson")
    # Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actors.objects.filter(first_name="George", last_name="Klooney").update(
        last_name="Clooney"
    )
    Actors.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves"
    )
    # Delete
    Genre.objects.filter(name="Action").delete()
    Actors.objects.filter(first_name="Scarlett").delete()

    return Actors.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    print(main())
