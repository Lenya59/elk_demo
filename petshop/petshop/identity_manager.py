import random

from petshop import get_logger


class IdentityManager:
    user_names = ['piter', 'ann', 'mc crocodile', 'ac^19asdh']

    def __init__(self):
        self.logger = get_logger('IdentityManager')

    def invalid_password(self, user):
        self.logger.warning('user "{}" used wrong password'.format(user))

    def successful_login(self, user):
        self.logger.info('user "{}" successfully logged in'.format(user))

    def scenario_brutforce(self):
        self.invalid_password('garry')

    def scenario_default(self):
        self.successful_login(random.choice(self.user_names))
