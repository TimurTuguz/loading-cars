class Car:
    def __init__(self, ident_code: str, volume: int, price: int, fridge_type: int):
        self.ident_code = ident_code
        self.volume = volume
        self.price = price
        self.fridge_type = fridge_type
        self.applications = []

    # def __str__(self):
    #     pass

    def load(self, app_id: str, volume: int):
        pass
