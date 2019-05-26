import logging

FORMAT = '%(asctime)s [%(levelname)s] [%(name)s] %(message)s'
logging.basicConfig(
    format=FORMAT,
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('petshop.log')
    ]
)


def get_logger(name):
    return logging.getLogger(name)
