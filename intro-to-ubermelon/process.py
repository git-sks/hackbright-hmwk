# set log_file to um-server-01.txt file from the local system
log_file = open("um-server-01.txt")


def sales_reports(log_file):
    """Goes through the log file and prints all (formerly Tuesday) Monday log records."""

    # for every line in the log file
    for line in log_file:
        # remove whitespace from the end of the line (had to look up in docs.python)
        line = line.rstrip()
        # get the day by getting the first three characters of a line
        day = line[0:3]
        # if find a line with beginning with Tue, now Mon
        ##if day == "Tue":
        if day == "Mon":
            # print the line
            print(line)


# call the sales_reports function
sales_reports(log_file)
