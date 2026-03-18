def load_signal_from_txt(path):
    with open(path, mode="r") as file:
        signal = file.readlines()
    return [float(value.strip()) for value in sugnal ]

if __name__ == "__main__":
    print(load_signal_from_txt("ekg_signal.txt"))

def signal_min(values):
    return min (values)

def signal_max(values):
    return max(values)

def signal_avg(values):
    return


if __name__ == "__main__":
my_signal = load_signal_from_txt("ekg_signal.txt")
print()
plot