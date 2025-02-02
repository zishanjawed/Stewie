import logging
import os

def setup_logging(verbose=False):
    """#+
    This function sets up logging for the application. It configures both console and file handlers.#+

    Parameters:#+
    verbose (bool): If True, the logger will set the log level to DEBUG. If False, the log level will be INFO. Default is False.#+

    Returns:#+
    None#+
    """#+

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handler
    log_file = os.path.join("logs", "app.log")
    os.makedirs("logs", exist_ok=True)
    fh = logging.FileHandler(log_file)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
