#!/usr/bin/env python3
import service.service as service
import logging

'''
This is your main script, this should call several other scripts within your packages.
'''
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='logging_file.log',
                    filemode='w')


def main():
	logging.info('Logger started')
	service.Service()


if __name__ == '__main__':
	main()

def main():
	print('TO-DO')

if __name__ == '__main__':
	main()

