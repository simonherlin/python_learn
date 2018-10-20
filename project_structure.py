# the content of my_script.py

# imports
import logging

# constants
LOGGER = logging.getLogger()


def magical_function():
    LOGGER.warning('We are about to do some magical stuff')


def main():
    # The actual logic of the script
    magical_function()


if __name__ == '__main__':
    main()