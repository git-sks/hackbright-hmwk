def check_customer_underpaid(order_filename, melon_cost):
  """Takes in the name of a file of customer orders,
  and checks if a customer has underpaid."""

  order_file = open(order_filename)

  for line in order_file:
    # Each line in the file is a single customer
    # Parse the line in order to get the individual customer data
    line = line.rstrip()
    customer = line.split("|")

    try:
      customer_name = customer[1]
      customer_num_melons = float(customer[2])
      customer_paid = float(customer[3])

      # Calculate what the customer is expected to pay,
      # then see if what the customer actually paid matches
      # If not, then point out the discrepency
      customer_expected_payment = customer_num_melons * melon_cost
      if customer_expected_payment != customer_paid:
        print(f"{customer_name} paid ${customer_paid:.2f},",
          f"expected ${customer_expected_payment:.2f}")
    except ValueError:
      print("Invalid data entry")


check_customer_underpaid("customer-orders.txt", 1.00)