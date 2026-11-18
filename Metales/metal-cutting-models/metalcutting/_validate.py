"""Small input checks shared by all modules."""


def positive(**kwargs):
    """Raise ValueError if any keyword argument is not strictly positive."""
    for name, value in kwargs.items():
        if value is None or value <= 0:
            raise ValueError(f"{name} must be greater than zero (got {value}).")


def angle(name, value, low=0.0, high=180.0):
    """Raise ValueError if an angle in degrees falls outside (low, high]."""
    if not (low < value <= high):
        raise ValueError(f"{name} must be in ({low}, {high}] degrees (got {value}).")
