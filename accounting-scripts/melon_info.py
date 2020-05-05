"""Print out all the melons in our inventory."""


from melons import melon_catalog


def print_melon(melon_name, melon_traits):
    """Print each melon with corresponding attribute information."""

    # Print the name
    print(melon_name)
    # Go through each trait in the melon's list of traits and print them
    for trait in melon_traits:
        print(f"    {trait}: {melon_traits[trait]}")

    # Print an empty space to divide with the next melon
    print()


# Go through each melon in the melon catalog and print it
for melon in melon_catalog:
    print_melon(melon, melon_catalog[melon])
