def assert_failure(func):
    def inner(*args, **kwargs):
        failures = func(*args, **kwargs)
        assert not failures, "\n".join(failures)

    return inner
