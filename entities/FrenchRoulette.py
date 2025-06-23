from dataclasses import dataclass

from entities.Pocket import Pocket
from entities.Roulette import Roulette


@dataclass
class FrenchRoulette(Roulette):
    def startRoulette(self):
        # TODO: change this shit
        self.pockets = [Pocket(number=1, color="rojo")]
