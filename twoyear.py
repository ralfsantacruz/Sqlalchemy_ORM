import datetime as dt
def two_yr():
    two_yr_ago = dt.datetime.now() - dt.timedelta(days=365*2)
    two_yr_ago = dt.datetime.strftime(two_yr_ago,'%Y-%m-%d')
    return two_yr_ago
