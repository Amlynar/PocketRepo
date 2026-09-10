from injector import Injector

from src.common.repositories.catalog_repo import CatalogRepository

def main():

    print("Starting the application...")
    injector = Injector()

    print("Setting up injector and dependencies...")
    catalog_repo = injector.get(CatalogRepository)

    print("Loading catalog repository...")
    catalog_repo.load_catalog()

    print("Catalogs loaded:")
    for catalog in catalog_repo.get_catalogs():
        print(f"- {catalog.name} (ID: {catalog.id})")

    pass

if __name__ == "__main__":
    main()
