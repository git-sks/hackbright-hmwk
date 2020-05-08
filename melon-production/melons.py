import robots


class Melon(object):
    """Melon."""

    def __init__(self, melon_type):
        """Initialize melon.

        melon_type: type of melon being built.
        """

        self.melon_type = melon_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        """Prepare the melon."""

        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)

    def __str__(self):
        """Print out information about melon."""

        if self.weight <= 0:
            return self.melon_type
        else:
            return "{} {:.2f} lbs {}".format(self.color,
                                             self.weight,
                                             self.melon_type)

# FIXME: Add Squash class definition here.
class Squash(Melon):
    """Winter squash."""
    
    def __init__(self, melon_type):
        """Initialize winter squash."""

        super().__init__(melon_type)


    def prep(self):
        """Prepare the squash."""

        # Prep the squash first by painting it
        robots.painterbot.paint(self)

        # Then carry out the rest of the prep process from its parent class
        super().prep()
