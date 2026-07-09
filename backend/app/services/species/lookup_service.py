from app.repositories.species.lookup_repository import LookupRepository

class LookupService:
    def __init__(self, repository: LookupRepository):
        self.repository = repository

    def get_countries(self):
        return self.repository.get_countries()

    def get_orders(self):
        return self.repository.get_orders()

    def get_families(self):
        return self.repository.get_families()

    def get_hotspots(self):
        return self.repository.get_hotspots()