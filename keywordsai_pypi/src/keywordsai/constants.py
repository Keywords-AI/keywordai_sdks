from os import getenv


KEYWORDSAI_NUM_THREADS = getenv("KEYWORDSAI_NUM_THREADS", 1)

MAX_PAYLOAD_SIZE = 100_000_000  # 100MB