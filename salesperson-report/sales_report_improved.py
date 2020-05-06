"""Generate sales report showing total melons each salesperson sold.

....Improved! How I would do it, basic version.

NTA: If I had more time/energy I would put all this into functions for
modularity but that's for another time."""

# Initiate a dictionary to track the salespeople and # of melons they've sold
salespeople = {}

# Open the sales report file to get access to the contents
f = open('sales-report.txt')
# Go through each line - where one line is a single salesperson's report
for line in f:
    # Process the line into the individual entry elements
    line = line.rstrip()
    entries = line.split('|')

    # The salesperson is the first item in entries
    name = entries[0]
    # The total amount of the order
    order_amount = float(entries[1])
    # The number of melons sold is set to int of the 3 item in entries
    melons = int(entries[2])

    # Ensure some form of entry for the salesperson is in the salespeople dict
    # If doesn't already exist, instantiate a new dictionary with the values = 0
    salespeople[name] = salespeople.get(name, {
        "total melons sold": 0,
        "total order amount": 0.00,
        })

    # Update the salesperson entry with the amounts
    salespeople[name]["total melons sold"] += melons
    salespeople[name]["total order amount"] += order_amount


# Go through all the people in the salespeople list
# and print out who sold how many melons
for salesperson in salespeople:
    print(f'{salesperson} sold',
          f'{salespeople[salesperson]["total melons sold"]} melons')
