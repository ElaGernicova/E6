def main():
    print("Hello from e6!")


if __name__ == "__main__":
    main()




def average_value(values, round_to=2):
    return round(sum(values) / len(values), round_to)


print(average_value([1200, 980, 1430]))       # round_to=2
print(average_value([1200, 980, 1430], 1))    # round_to=1

def convert_coins(value, from_currency, to_currency):
    if from_currency == "gold" and to_currency == "gems":
        return value / 100
    if from_currency == "gems" and to_currency == "gold":
        return value * 100
    return value


print(convert_coins(2500, "gems", "gold"))

print(convert_coins(value=2500, from_currency="gold", to_currency="gems"))


def compute_score_delta(score, baseline, multiplier=1.0, round_to=2):
    return round((score - baseline) * multiplier, round_to)


print(compute_score_delta(1540, 1200, round_to=1))
print(compute_score_delta(1540, 1200, 0.5, round_to=3))


def normalize_signal(values, min_value=0, max_value=1):
    low = min(values)
    high = max(values)
    scale = high - low
    return [min_value + (v - low) * (max_value - min_value) / scale for v in values]


print(normalize_signal([2, 4, 6], max_value=100))
print(normalize_signal([2, 4, 6], 0, 100))


DEFAULT_ROUND = 2


def round_value(value):
    return round(value, DEFAULT_ROUND)


print(round_value(12.3456))  # 12.35



