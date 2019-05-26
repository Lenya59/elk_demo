import random

from petshop import get_logger


class RequestHandler:

    ip_addresses = [
        '221.54.223.186',
        '86.237.67.58',
        '85.52.2.22',
        '69.192.84.200',
        '51.83.131.64',
        '223.175.141.86',
        '230.138.116.108',
        '21.197.161.190',
        '1.76.31.2',
        '6.113.222.172',
        '156.14.97.4',
        '127.35.26.49',
        '11.126.212.206',
        '254.150.17.98',
        '19.6.118.131',
        '78.239.182.177',
        '170.253.156.113',
        '10.71.236.56',
        '82.247.67.130',
        '119.30.232.111'
    ]

    resources = [
        '/index',
        '/products',
        '/settings'
    ]

    not_found = ['/product{}'.format(x) for x in range(21, 30)]

    rnd = random.Random()

    def __init__(self):
        self.logger = get_logger('RequestHandler')
        self.resources.extend('/product{}'.format(x) for x in range(0, 20))

    def handle_request(self, ip, resource, code):
        self.logger.info('{} - {} {}'.format(
            ip,
            resource,
            code
        ))

    def scenario_handle_200(self):
        self.handle_request(
            self.rnd.choice(self.ip_addresses),
            self.rnd.choice(self.resources),
            200
        )

    def scenario_handle_404(self):
        self.handle_request(
            self.rnd.choice(self.ip_addresses),
            self.rnd.choice(self.not_found),
            404
        )

    def scenario_handle_500(self):
        self.handle_request(
            self.rnd.choice(self.ip_addresses),
            self.rnd.choice(self.resources),
            500
        )