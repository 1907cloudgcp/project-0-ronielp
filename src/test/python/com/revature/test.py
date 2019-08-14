#!/usr/bin/env python3
import service.service as service
import logging
import unittest

'''
This is your main script, this should call several other scripts within your packages.
'''
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='logging_file.log',
                    filemode='w')


class BankingTest(unittest.TestCase):

    def test_a_register(self):
        service.register('Ron', 'testing')

    def test_b_login(self):
        self.assertEqual(service.login('Ron', 'testing'))
        self.assertEqual(service.login('Ron', 'incorrect'))

    def test_c_deposit(self):
        service.deposit(100)
        self.assertEqual(service.viewBalance(), 100)
        service.deposit(200)
        self.assertEqual(service.viewBalance(), 500)


if __name__ == '__main__':
    unittest.main()
