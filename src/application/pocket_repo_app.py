from injector import inject

from src.common.repositories.catalog_repo import CatalogRepository


class PocketRepoApp:

    @inject
    def __init__(self, catalog_repo: CatalogRepository):
        self.catalog_repo = catalog_repo

    def run(self):
        print("Starting the PocketRepo application...")
        print("Loading catalog repository...")
        self.catalog_repo.load_catalog()
        catalogs = self.catalog_repo.get_catalogs()
        print("Catalogs loaded:")
        for catalog in catalogs:
            print(f"- {catalog.name} (ID: {catalog.id})")
            