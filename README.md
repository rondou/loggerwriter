Logger Writer
=============

Description
-----------
This module provides a class to fork the output to a logger.

Examples
--------

Prepare a logger from logging to make the loggerwriter to direct the output.
```python
logger = logging.getLogger()
logger.setLevel(logging.INFO)
```

Capture and redirect output to logger and sys.__stdout__.
```python
sys.stdout = loggerwriter.LoggerWriter(logger, sys.__stdout__)
```
