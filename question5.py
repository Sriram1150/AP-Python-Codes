def shift(s,acount=0,ccount=0):
    acount = acount % len(s)
    ccount = ccount % len(s)
    if not isinstance(ccount, int) or not isinstance(acount, int) or ccount < 0 or acount < 0:
        raise ValueError("Shift values cannot be negative")

    s = s[acount:] + s[:acount]
    s = s[-ccount:] + s[:-ccount]

    return s


print(shift('NinjaHattori'))
print(shift('NinjaHattori', acount=3))
print(shift('NinjaHattori', ccount=3))
print(shift('NinjaHattori',acount=3,ccount=3))
print(shift('NinjaHattori',acount=6,ccount=3))
print(shift('NinjaHattori',acount=3,ccount=6))

    
