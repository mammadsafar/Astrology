
def persian_to_jd(day, month, year):
    epbase = year - 474
    epyear = 474 + (epbase % 2820)
    mdays = (month - 1) * 31 if month <= 7 else (month - 1) * 30 + 6
    jd = day + mdays + ((epyear * 682 - 110) // 2816) + \
         (epyear - 1) * 365 + (epbase // 2820) * 1029983 + (1948320.5 - 1)
    return jd

def jd_to_gregorian(jd):
    jd += 0.5
    z = int(jd)
    f = jd - z
    a = z if z < 2299161 else z + 1 + int((z - 1867216.25) / 36524.25) - int(int((z - 1867216.25) / 36524.25) / 4)
    b = a + 1524
    c = int((b - 122.1) / 365.25)
    d = int(365.25 * c)
    e = int((b - d) / 30.6001)
    day = b - d - int(30.6001 * e) + f
    month = e - 1 if e < 14 else e - 13
    year = c - 4716 if month > 2 else c - 4715

    print(f"Your birth date in Gregorian: {int(month)}/{int(day)}/{int(year)}\n")
    return int(day), int(month), int(year)

def convert_date(day, month, year):
    if year < 1500:
        print(f"Your birth date in jalali: {year}/{month}/{day}")
        jd = persian_to_jd(day, month, year)
        return jd_to_gregorian(jd)
    
    print(f"Your birth date in Gregorian: {month}/{day}/{year}\n")
    return day, month, year