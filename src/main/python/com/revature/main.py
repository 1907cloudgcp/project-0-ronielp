#!/usr/bin/env python3
<<<<<<< HEAD
import service.service as service
import logging
=======
>>>>>>> 472bbfcb6333433b364bb9998f6d4c75b68230f2

'''
This is your main script, this should call several other scripts within your packages.
'''
<<<<<<< HEAD
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='logging_file.log',
                    filemode='w')


def main():
	logging.info('Logger started')
	service.Service()


if __name__ == '__main__':
	main()
=======
def main():
	print('TO-DO')

if __name__ == '__main__':
	main()
>>>>>>> 472bbfcb6333433b364bb9998f6d4c75b68230f2
