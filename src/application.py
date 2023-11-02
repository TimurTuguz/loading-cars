class Application:
    def __init__(self, ident_code: str, volume: int, fridge_type: int, crashed: bool):
        self.ident_code = ident_code
        self.volume = volume
        self.fridge_type = fridge_type
        self.crashed = crashed
        self.loaded = {}

    # def __str__(self):
    #     pass

    def load(self, car_id: str, volume: int):
        pass
