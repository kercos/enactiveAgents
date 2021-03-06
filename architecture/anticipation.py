__author__ = 'katja'


class Anticipation:
    def __init__(self, interaction, proclivity):
        self.interaction = interaction
        self.proclivity = proclivity

    def get_interaction(self):
        return self.interaction

    def get_proclivity(self):
        return self.proclivity

    def compare(self):
        return self.interaction.get_valence()

    def __repr__(self):
        return "{0} proclivity {1}".format(self.interaction.get_label(), self.proclivity)
