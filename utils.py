def Money(number, currency="$", space=''):
    return "{0:,.2f} {2}".format(number, space, currency)

