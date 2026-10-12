from .errors import TransientError


def with_retry(fn, attempts: int = 3):
    for i in range(attempts):
        try:
            return fn()
        except TransientError:
            if i == attempts - 1:
                raise
