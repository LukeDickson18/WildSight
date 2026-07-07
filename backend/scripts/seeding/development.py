from scripts.seeding.users import seed_users
from scripts.seeding.observations import seed_observations
from scripts.seeding.locations import seed_locations


def seed_development() -> None:
    print("===================================")
    print("WildSight Development Seeder")
    print("===================================\n")

    print("Seeding users...")
    seed_users()
    print("\nSeeding locations...")
    seed_locations()
    print("\nSeeding observations...")
    seed_observations()

    print("\n===================================")
    print("Development database seeded!")
    print("===================================")


if __name__ == "__main__":
    seed_development()