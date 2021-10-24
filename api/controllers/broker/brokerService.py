from . import appCelery
class BrokerService:
    def customerForm(attr=None):
        appCelery.signature("post-form").delay(attr)
