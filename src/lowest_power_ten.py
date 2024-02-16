def lowest_power_ten() -> int:
    power = 1

    while True:
        ten_to_power = 10 ** -power

        if ten_to_power + 1 - 1 > 0:
            power += 1
        else:
            return power
