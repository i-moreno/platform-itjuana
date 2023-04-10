import utils

# Get parameter files from the command line
drivers_file, shipments_file = utils.get_terminal_arguments()

# Read content files
drivers, shipments = utils.read_files(drivers_file, shipments_file)

# Assign shipments to drivers
driver_shipments, scores = utils.assign_shipments(shipments, drivers)

# Return formated output
for driver in driver_shipments:
    print(
        f"{driver} is delivering to {driver_shipments[driver]} with a score of {scores[driver]}")
