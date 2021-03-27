

class WrappedCommand:
    def __init__(self, something):
        self.something = something


def test_decorator(func):
    def wrapper(*args, **kwargs):
        print('okDec')
        present_result = func(*args, **kwargs)
        print(present_result + "test")
        print('done')
        return present_result
    return wrapper


@test_decorator
def try_wrapper(present: WrappedCommand):
    return present.something
