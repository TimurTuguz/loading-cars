from solver import Solver
from db import DataBase
from parse_in_file import File
import logging.config
from config import DB_CONFIG, LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('loading-cars')

if __name__ == "__main__":
    logger.info('Запуск сервиса')
    # получаем список машин и заявок из базы. Реализовать нормальное подключение к базе
    # db = DataBase(CONFIG)
    # получаем список машин и заявок из . Реализовать нормальное подключение к базе
    data = File()
    cars = data.get_cars()
    applications = data.get_applications()

    # запуск алгоритма (создать класс, содержащий все функции и запустить с двумя списками)
    solv = Solver(cars, applications)
    res = solv.run()
    # распарсить результат в удобном виде
    for i in res:
        print(i)
