"""Generate sales report showing total melons each salesperson sold."""

# Initiate the list of salespeople, and the list of melons sold
salespeople = []
melons_sold = []

# Open the sales report file to get access to the contents
f = open('sales-report.txt')
# Go through each line - where one line is a single salesperson's report
for line in f:
    # Process the line into the individual entry elements
    line = line.rstrip()
    entries = line.split('|')

    # The salesperson is the first item in entries
    salesperson = entries[0]
    # The number of melons sold is set to int of the 3 item in entries
    melons = int(entries[2])

    # If the salesperson is already in the salesperson list,
    # get the index of the salesperson and update the # of melons they've sold
    # in the corresponding index in the melons_sold list
    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    else:
        # Otherwise add the salesperson and and the number of melons sold
        # to the salespeople and melons_sold lists respectively
        salespeople.append(salesperson)
        melons_sold.append(melons)


# Go through all the people in the salespeople list
# and print out who sold how many melons
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
