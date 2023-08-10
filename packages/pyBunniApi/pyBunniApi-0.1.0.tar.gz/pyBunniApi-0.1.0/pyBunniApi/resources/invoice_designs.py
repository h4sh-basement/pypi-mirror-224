from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyBunniApi import PyBunniApi


class InvoiceDesigns:
    def __init__(self, bunni_api: "PyBunniApi"):
        self.bunni_api = bunni_api

    def list(self):
        return self.bunni_api.create_http_request('invoice-designs/list')
