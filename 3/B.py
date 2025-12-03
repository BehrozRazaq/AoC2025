data = """"""

banks = []
for pre_bank in data.splitlines():
    bank = []
    for battery in pre_bank.strip():
        bank.append(int(battery))
    banks.append(bank)


def next_largest_digit(bank: str, start_i: int, digits_needed: int):
    largest_digit = 0
    largest_i = 0

    for current_i in range(start_i, len(bank) - (digits_needed - 1)):
        current = int(bank[current_i])
        if current > largest_digit:
            largest_digit = current
            largest_i = current_i
    return str(largest_digit), largest_i


sum_banks = 0
n_digits = 12
for bank in banks:
    digits = ""
    latest_i = -1
    for digit in reversed(range(1, n_digits + 1)):
        next_largest, latest_i = next_largest_digit(bank, latest_i + 1, digit)
        digits += next_largest
    sum_banks += int(digits)
print(sum_banks)
