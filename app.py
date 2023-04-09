import math

file1 = 'data/drivers.txt'
file2 = 'data/address.txt'

def read_files():
    try:
      with open(file1, 'r') as drivers, open(file2, 'r') as address:
          # Read all lines from both files into a list
          driver_list = drivers.readlines()  
          address_list = address.readlines()

          return (driver_list, address_list)
    except Exception as e:
        print(f"There was a error reading files::: {e}")
        return ()

# Calculate base suitability score
def get_base_ss(length, name):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    name_vowels = sum(1 if character.lower() in vowels else 0 for character in name)
    name_consonants = sum(1 if character.lower() not in vowels else 0 for character in name)

    if length % 2 == 0:
        return name_vowels * 1.5
    else:
        return name_consonants

# Calculate suitability score
def get_ss(length, name):
    base_ss = get_base_ss(length, name)

    if math.gcd(length, len(name)) != 1:
        return base_ss * 1.5
    else:
        return base_ss


# Assign shipments to drivers
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


drivers, shipments = read_files()
driver_shipments, scores = assign_shipments(shipments, drivers)

for driver in driver_shipments:
    print(
        f"{driver.title()} is delivering to {driver_shipments[driver]} with a score of {scores[driver]}")
