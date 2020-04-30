def format_data(day, file_name):
    """Takes in a file name containing the raw delivery data,
    then prints out the data into the proper log report format."""

    print("Day", str(day))
    # open the file containing the raw delivery data
    the_file = open(file_name)

    for line in the_file:
        # convert each line in the file into a list of distinct data
        line = line.rstrip()
        words = line.split('|')

        # parse the list of data into their own data elements
        melon = words[0]
        num_melons = words[1]
        total_price = words[2]

        # print the line into a readable format given the parsed data
        print("Delivered {} {}s for total of ${}".format(
            num_melons, melon, total_price))

    # close the file once all the lines have been handled
    the_file.close()


def start_report():
    """Processes the delivery data for the amount of days delineated."""

    # format the data for Day 1
    day_1_file = format_data(1, "um-deliveries-20140519.txt")
    print()

    # format the data for Day 2
    day_2_file = format_data(2, "um-deliveries-20140520.txt")
    print()

    # format the data for Day 3
    day_3_file = format_data(3, "um-deliveries-20140521.txt")
    print()


start_report()