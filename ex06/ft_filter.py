def ft_filter(function, iterable):

    if iterable is None:
        return None
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]
