import sys
import loggerwriter
import logging


def test_loggerwriter():
    logger = logging.getLogger(f'{__package__}.stdout')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    sys.stdout = loggerwriter.LoggerWriter(logger, sys.__stdout__)
    sys.stderr = loggerwriter.LoggerWriter(logger, sys.__stderr__)

    logging.basicConfig(
        format='[%(asctime)s|%(filename)s:%(lineno)d|%(funcName)s|%(levelname)s] %(message)s'
    )

    print('test')


if __name__ == '__main__':
    test_loggerwriter()
