import random

from petshop import get_logger


class DatabaseConnector:
    rnd = random.Random()

    def __init__(self):
        self.logger = get_logger('DatabaseConnector')

    def scenario_query_executed(self):
        self.logger.info("query took {:.0f}".format(self.rnd.gauss(10, 2)))

    def scenario_query_failed(self):
        self.logger.error("'UPDATE table_name SET name = \"teapot\" WHERE product_id = 1123;' failed because of non unique name")