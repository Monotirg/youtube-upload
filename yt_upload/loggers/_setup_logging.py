import json
import logging.config
import logging.handlers

from .logformatter import JSONFormatter


def setup_logging(**kwargs):
    config_file = "yt_upload/loggers/logging_config.json"

    with open(config_file) as f:
        config = json.load(f)

    logging.config.dictConfig(config)
    
    logger = logging.getLogger("yt_logger") 

    filename = kwargs.get("filename", None)
    
    if filename is None:
        return logger
    
    mode = kwargs.get("mode", "a")
    maxBytes = kwargs.get("maxBytes", 0)
    backupCount = kwargs.get("backupCount", 0)
    encoding = kwargs.get("encoding", "utf-8")
    delay = kwargs.get("delay", False)

    file_handler = logging.handlers.RotatingFileHandler(
        filename=filename, 
        mode=mode, 
        maxBytes=maxBytes, 
        backupCount=backupCount, 
        encoding=encoding, 
        delay=delay
    )
    file_handler.setFormatter(JSONFormatter())
    logger.addHandler(file_handler)
    
    return logger
