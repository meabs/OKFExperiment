class LedgerError(Exception):
    pass


class DuplicateKey(LedgerError):
    """An idempotency key was posted twice."""


class InvalidKey(LedgerError):
    """Keys look like 'kind:identifier', identifier 6 to 64 of [A-Za-z0-9_-]."""


class InvalidEntry(LedgerError):
    pass


class AlreadyReversed(LedgerError):
    pass


class TransientError(LedgerError):
    pass
