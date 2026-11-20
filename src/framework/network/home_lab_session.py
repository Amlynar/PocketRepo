
import os
from urllib.parse import urlparse

import requests

HOME_LAB_DOMAIN_SUFFIX = ".home.arpa"

CA_BUNDLE_PATH = os.path.expanduser(
    "~/Documents/site-packages-3/pocketrepo_shared/homelab-ca.crt"
)


class PYIHomeLabSession(requests.Session):
    """requests.Session that trusts the home-lab CA for *.home.arpa hosts.

    Every other host uses requests' normal certificate verification.
    """

    def request(self, method, url, **kwargs):
        if self._is_home_lab_url(url):
            if not os.path.exists(CA_BUNDLE_PATH):
                raise RuntimeError(
                    "Home-lab CA certificate not found at "
                    f"{CA_BUNDLE_PATH}. Go to Settings and press "
                    "'Download CA Certificate' first."
                )
            kwargs.setdefault("verify", CA_BUNDLE_PATH)
        return super().request(method, url, **kwargs)

    @staticmethod
    def _is_home_lab_url(url) -> bool:
        hostname = urlparse(str(url)).hostname or ""
        return hostname.lower().endswith(HOME_LAB_DOMAIN_SUFFIX)
