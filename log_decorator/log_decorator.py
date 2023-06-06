"""Logging some logs."""
from functools import wraps
from logging import info


def log_call(func):
    """Log the loggend."""
    @wraps(func)
    def fn(*args, **kwargs):
        kwmsg = []
        for arg in args:
            kwmsg.append(repr(arg))
        for kw in kwargs:
            kwmsg.append(f"{kw}={repr(kwargs[kw])}")
        info(f'Calling: {func.__name__}(' + ', '.join(kwmsg) + ')')
        return func(*args, **kwargs)
    return fn
