class DataBase:
    def __init__(self, conf):
        self.conf = conf
        self.connect()

    def connect(self):
        pass

    @staticmethod
    def get_cars() -> list:
        return []

    @staticmethod
    def get_applications() -> list:
        return []
