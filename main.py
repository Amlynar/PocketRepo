from injector import Injector
from src.common.repositories.catalog_repo import CatalogRepository
from src.application.pocket_repo_app import PocketRepoApp
# from src.application.dev_app import DevApp

def main():
    injector = Injector()
    app = injector.get(PocketRepoApp)

    app.catalog_repo.load_catalog()
    projects = app.catalog_repo.get_all_projects()
    print(f"Catalogs loaded: {len(projects)}")


    test = injector.get(CatalogRepository)
    projects2 = test.get_all_projects()
    print(f"Catalogs loaded from test: {len(projects2)}")

    app.run()
    pass

if __name__ == "__main__":
    main()
