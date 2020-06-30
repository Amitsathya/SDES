from django.db import models

"""A hand of cards (bridge style)"""
class Hand:
    def __init__(self, x):
        # Input parameters are lists of cards ('Ah', '9s', etc.)
        self.x = x

class Input(models.Model):
    K = models.FloatField()
    PT = models.FloatField()
    IP = models.FloatField(default=None)
    IPi = models.FloatField(default=None)
    P10 = models.FloatField(default=None)
    P8 = models.FloatField(default=None)
    P4 = models.FloatField(default=None)
    E = models.FloatField(default=None)
    S0 = models.FloatField(default=None)
    S1 = models.FloatField(default=None)
    O = models.FloatField(default=None)
