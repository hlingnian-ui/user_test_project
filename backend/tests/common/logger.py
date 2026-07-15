import logging

logger = logging.getLogger("user_test")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(message)s"
)

console = logging.StreamHandler()
console.setFormatter(formatter)

file_handler = logging.FileHandler(
    "tests.log",
    encoding="utf-8"
)

file_handler.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(file_handler)