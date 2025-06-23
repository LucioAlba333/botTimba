from abc import abstractmethod
from dataclasses import dataclass, field

from entities.Pocket import Pocket


@dataclass
class Roulette:
    pockets: list[Pocket] = field(init=False)

    @abstractmethod
    def startRoulette(self): ...

    def __post_init__(self) -> None:
        self.startRoulette()
