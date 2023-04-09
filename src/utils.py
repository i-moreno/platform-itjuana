import math
import sys


def get_terminal_arguments():
    # Check that two command-line arguments were provided
    if len(sys.argv) != 3:
        print("Error: Two file paths are required.")
        print("Usage: python app.py path/to/drivers.txt path/to/shipments.txt")
        sys.exit(1)

    # Get the file paths from the command-line arguments
    drivers = sys.argv[1]  # Order required. Drivers
    shipments = sys.argv[2]  # Order required. Addresses

    return (drivers, shipments)


def read_files(file1, file2):
    try:
        with open(file1, 'r') as drivers, open(file2, 'r') as address:
            # Read all lines from both files into a list
            driver_list = drivers.readlines()
            address_list = address.readlines()

            return (driver_list, address_list)
    except Exception as e:
        print(f"There was a error reading files::: {e}")
        return ()


def assign_shipments(shipments, drivers):
    driver_shipments = {}
    scores = {driver: 0 for driver in drivers}

    for shipment in shipments:
        best_driver = None
        best_score = -1

        for driver in drivers:
            score = get_ss(len(shipment), driver)

            if score > best_score and driver not in driver_shipments:
                best_driver = driver
                best_score = score

        if best_driver is not None:
            driver_shipments[best_driver] = shipment
            scores[best_driver] += best_score

    return (driver_shipments, scores)


def get_ss(length, name):
    # Calculate suitability score
    base_ss = get_base_ss(length, name)

    if math.gcd(length, len(name)) != 1:
        return base_ss * 1.5
    else:
        return base_ss


def get_base_ss(length, name):
    # Calculate base suitability score
    vowels = {'a', 'e', 'i', 'o', 'u'}
    name_vowels = sum(1 if character.lower()
                      in vowels else 0 for character in name)
    name_consonants = sum(1 if character.lower()
                          not in vowels else 0 for character in name)

    if length % 2 == 0:
        return name_vowels * 1.5
    else:
        return name_consonants
