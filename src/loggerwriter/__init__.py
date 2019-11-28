# -*- coding: utf-8 -*-


class LoggerWriter:
    def __init__(self, logger, writer):
        self.logger = logger
        self.writer = writer

        for attr_name in dir(writer):
            if attr_name in ['__class__', '__del__', '__dict__', 'flush', 'write']:
                continue
            setattr(self, attr_name, getattr(writer, attr_name))

    def __del__(self):
        if callable(getattr(self.logger, 'close', None)):
            self.logger.close()
        self.writer.__del__()

    def write(self, b):
        self.logger.info(f'{b}')
        self.writer.write(b)

    def flush(self):
        if callable(getattr(self.logger, 'flush', None)):
            self.logger.flush()
        self.writer.flush()
