from injector import Injector
# from src.application.pocket_repo_app import PocketRepoApp
from src.application.dev_app import DevApp

def main():
    injector = Injector()
    app = injector.get(DevApp)
    app.run()
    pass

if __name__ == "__main__":
    main()
