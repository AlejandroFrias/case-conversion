def aliased(klass):
    """
    Use in combination with `@alias` decorator.

    Classes decorated with @aliased will have their aliased methods
    (via @alias) actually aliased.
    """
    methods = klass.__dict__.copy()
    for method in methods.values():
        if hasattr(method, "_aliases"):
            # add aliases but don't override attributes of 'klass'
            try:
                for alias in method._aliases - set(methods):
                    setattr(klass, alias, method)
            except TypeError:
                pass
    return klass


class alias:
    """
    Decorator for aliasing method names.

    Only works within classes decorated with '@aliased'
    """

    def __init__(self, *aliases):
        self.aliases = set(aliases)

    def __call__(self, f):
        f._aliases = self.aliases
        return f
