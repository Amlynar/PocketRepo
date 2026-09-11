
import urllib.request

class FileDownloader:
    def __init__(self):
        pass

    def download(self, github_url, output_zip):
        urllib.request.urlretrieve(github_url, output_zip)
