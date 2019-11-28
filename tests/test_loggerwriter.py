import sys
import logging
import logging.handlers
import loggerwriter


def test_loggerwriter():
    rotating_file_handler = logging.handlers.RotatingFileHandler(
        'loggerwritet_test.log', maxBytes=10 * 2 ** 20, backupCount=10)
    rotating_file_handler.terminator = ''

    logger = logging.getLogger(f'{__package__}.stdout')
    logger.addHandler(rotating_file_handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    sys.stdout = loggerwriter.LoggerWriter(logger, sys.__stdout__)
    sys.stderr = loggerwriter.LoggerWriter(logger, sys.__stderr__)

    logging.basicConfig(
        format='[%(asctime)s|%(filename)s:%(lineno)d|%(funcName)s|%(levelname)s] %(message)s'
    )

    logger.info('{}\n'.format('logger test'))
    print('print test')


if __name__ == '__main__':
    test_loggerwriter()
