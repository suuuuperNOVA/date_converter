from datetime import datetime
from datetime import date


def date_converter(dt, f='%Y-%m-%d'):
    if isinstance(dt, str):
        return date.toordinal(datetime.strptime(dt, f))
    elif isinstance(dt, int):
        return datetime.fromordinal(dt).strftime(f)

    return None
