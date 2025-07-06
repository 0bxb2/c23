import logging
from src.cnc import start as start_cnc

def main():
    try:
        start_cnc()
    except Exception as e:
        logging.exception("An error occurred while starting the CNC:")

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    main()
