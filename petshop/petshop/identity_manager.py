import random

from petshop import get_logger


class IdentityManager:
    user_names = ['piter', 'ann', 'mc crocodile', 'star rocket', 'admin']

    def __init__(self):
        self.logger = get_logger('IdentityManager')

    def invalid_password(self, user):
        self.logger.warning('user "{}" used wrong password'.format(user))

    def successful_login(self, user):
        self.logger.info('user "{}" successfully logged in'.format(user))

    def scenario_brutforce(self):
        self.invalid_password('garry')

    def scenario_failed_login(self):
        self.invalid_password(random.choice(self.user_names))

    def scenario_successful_login(self):
        self.successful_login(random.choice(self.user_names))
