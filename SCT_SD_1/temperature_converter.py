"""Convert temperatures among Celsius, Fahrenheit, and Kelvin."""


def to_celsius(value, unit):
    if unit == "C":
        return value
    if unit == "F":
        return (value - 32) * 5 / 9
    if unit == "K":
        return value - 273.15
    raise ValueError("Unknown temperature scale")


def from_celsius(value, unit):
    if unit == "C":
        return value
    if unit == "F":
        return value * 9 / 5 + 32
    if unit == "K":
        return value + 273.15
    raise ValueError("Unknown temperature scale")


def convert(value, source, target):
    source, target = source.upper(), target.upper()
    if source not in {"C", "F", "K"} or target not in {"C", "F", "K"}:
        raise ValueError("Use C, F, or K for the temperature scale")
    celsius = to_celsius(value, source)
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15 °C)")
    return from_celsius(celsius, target)


def main():
    names = {"C": "Celsius", "F": "Fahrenheit", "K": "Kelvin"}
    print("\nTEMPERATURE CONVERTER")
    print("Scales: C = Celsius | F = Fahrenheit | K = Kelvin")
    while True:
        try:
            raw = input("\nEnter temperature (or q to quit): ").strip()
            if raw.lower() == "q":
                print("Goodbye!")
                break
            value = float(raw)
            source = input("Convert from (C/F/K): ").strip().upper()
            target = input("Convert to   (C/F/K): ").strip().upper()
            result = convert(value, source, target)
            print(f"{value:g}° {names[source]} = {result:.2f}° {names[target]}")
        except ValueError as error:
            print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
