from sqlalchemy import select

from app.db.database import SessionLocal
from app.models.order import Order

ORDER_COMMON_NAMES = {
    "Struthioniformes": "Ostriches",
    "Tinamiformes": "Tinamous",
    "Anseriformes": "Waterfowl",
    "Galliformes": "Gamebirds",
    "Phoenicopteriformes": "Flamingos",
    "Podicipediformes": "Grebes",
    "Columbiformes": "Pigeons & Doves",
    "Mesitornithiformes": "Mesites",
    "Pterocliformes": "Sandgrouse",
    "Musophagiformes": "Turacos",
    "Cuculiformes": "Cuckoos",
    "Caprimulgiformes": "Nightjars",
    "Apodiformes": "Swifts",
    "Otidiformes": "Bustards",
    "Gruiformes": "Cranes & Rails",
    "Charadriiformes": "Shorebirds",
    "Eurypygiformes": "Sunbittern & Kagu",
    "Phaethontiformes": "Tropicbirds",
    "Gaviiformes": "Loons",
    "Procellariiformes": "Pelagics",
    "Sphenisciformes": "Penguins",
    "Ciconiiformes": "Storks",
    "Suliformes": "Cormorants & Gannets",
    "Pelecaniformes": "Pelicans, Herons & Ibises",
    "Cathartiformes": "New World Vultures",
    "Accipitriformes": "Birds of Prey",
    "Strigiformes": "Owls",
    "Coliiformes": "Mousebirds",
    "Leptosomiformes": "Cuckoo Roller",
    "Trogoniformes": "Trogons",
    "Bucerotiformes": "Hornbills & Hoopoes",
    "Coraciiformes": "Kingfishers & Bee-eaters",
    "Piciformes": "Woodpeckers & Barbets",
    "Falconiformes": "Falcons",
    "Psittaciformes": "Parrots",
    "Passeriformes": "Perching Birds",
    "Aegotheliformes": "Owlet-nightjars",
    "Apterygiformes": "Kiwis",
    "Cariamiformes": "Seriemas",
    "Casuariiformes": "Cassowaries & Emus",
    "Nyctibiiformes": "Potoos",
    "Opisthocomiformes": "Hoatzin",
    "Podargiformes": "Frogmouths",
    "Rheiformes": "Rheas",
    "Steatornithiformes": "Oilbird",
}


def main() -> None:
    db = SessionLocal()

    try:
        orders = db.scalars(
            select(Order).order_by(Order.taxon_order)
        ).all()

        updated = 0
        missing = []

        for order in orders:
            common_name = ORDER_COMMON_NAMES.get(order.name)

            if common_name is None:
                missing.append(order.name)
                continue

            if order.common_name != common_name:
                order.common_name = common_name
                updated += 1

        db.commit()

        print(f"Updated : {updated}")
        print(f"Total   : {len(orders)}")

        if missing:
            print("\nOrders without a common name mapping:")
            for name in sorted(missing):
                print(f" - {name}")

    finally:
        db.close()


if __name__ == "__main__":
    main()