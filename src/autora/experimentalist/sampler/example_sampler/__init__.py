def example_sampler(pool: enumerate):
    """
    Add a description of the sampler here.
    Returns the first argument of an enumerate
    Args:
        pool: description of the argument
    Returns: first element of the enumeratable

    *Optional*
    Examples:
        These examples add documentations and also work as doctests
        >>> example_sampler([1, 2, 3, 4])
        1
        >>> example_sampler(range(3, 10))
        3
    """
    try:
        return next(iter(pool))
    except (TypeError, StopIteration, IndexError):
        return None
