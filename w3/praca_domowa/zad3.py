import logging
#import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
#logging.basicConfig(stream=sys.stdout)


def log_this(logger, level, format):
    def decorated_fun(dec_fun):
        def inner(*args, **kwargs):
            arg_list = []
            for item in args:
                arg_list.append(f'{item}')

            for key, value in kwargs.items():
                arg_list.append(f'{key}={value}')

            return logger.log(level, format, dec_fun.__name__, tuple(arg_list), dec_fun(*args, **kwargs))

        return inner

    return decorated_fun


@log_this(logger, level=logging.INFO, format='%s: %s -> %s')
def my_func(a, b, c=None, d=False):
    return 'Wow!'


my_func(1, 2, d=True)
