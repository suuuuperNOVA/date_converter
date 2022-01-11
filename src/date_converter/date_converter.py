from datetime import datetime
from datetime import date


def date_converter(dt, f='%Y-%m-%d'):
    """Convert datenum to date string, or date string to datenum

    Parameters
    ----------
    dt : str or int
        Date number or date string to be converted.
    f : str, optional
        Date string formate.

    Returns
    -------
    int or str
        String if input is int, or int 'if input is string.


    Examples
    --------
    >>> date_converter('2020-01-01')
    >>> date_converter(737425)
    """



    if isinstance(dt, str):
        return date.toordinal(datetime.strptime(dt, f))
    elif isinstance(dt, int):
        return datetime.fromordinal(dt).strftime(f)

    return None
