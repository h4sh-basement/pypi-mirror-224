from remotemanager.storage.function import Function
from remotemanager.logging import LoggingMixin


class RemoteFunction(LoggingMixin):
    """
    Decorator class to store a function within the "cached functions" property.

    Wrap a function with `@RemoteFunction` to store:

    >>> @RemoteFunction
    >>> def func(val):
    >>>     return val

    This function will then be made available in all runs:

    >>> def main():
    >>>     val = ...
    >>>     return func(val)
    >>>
    >>> ds = Dataset(main)
    >>> ...

    .. versionadded:: 0.3.6
    """

    def __init__(self, function):
        self._storedfunction = function

        storedfunction = Function(function)
        self._logger.info(f"caching function {storedfunction.raw_source}")
        cached_functions[function.__name__] = storedfunction

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)

    @property
    def function(self):
        return self._storedfunction


cached_functions = {}
