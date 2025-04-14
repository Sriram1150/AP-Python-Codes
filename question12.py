def fee(base_fee, roll_number):
    if len(roll_number) != 7 or roll_number[:2] not in {'DS', 'CS', 'EE', 'ME'}:
        raise ValueError("Invalid Roll Number")
    year = int('20' + roll_number[2:4])
    program = roll_number[4]
    current_year = 2023
    duration = 4 if program == '1' else 2
    if program not in {'1', '2'}:
        raise ValueError("Invalid Program Code")
    years_paid = min(duration, current_year - year)
    total_fee = 0
    for i in range(years_paid):
        total_fee += base_fee
        base_fee += base_fee * 0.1
    return int(total_fee)

print(fee(100000,'CS20143'))
print(fee(100000,'DS18243'))
print(fee(100000,'EE16843'))