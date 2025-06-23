from dataclasses import dataclass


@dataclass
class Pocket:
    number: int = -1
    color: str = ""

    def __str__(self) -> str:
        return f"Pocket(number={self.number}, color={self.color})"
