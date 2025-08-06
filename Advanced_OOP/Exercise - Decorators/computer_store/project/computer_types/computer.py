from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        if not manufacturer.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        if not model.strip():
            raise ValueError("Model name cannot be empty.")

        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    @abstractmethod
    def available_processors(self) -> dict[str, int]:
        pass

    @property
    @abstractmethod
    def max_ram(self) -> int:
        pass

    @property
    def valid_ram(self) -> list[int]:
        return [2 ** i for i in range(1, int(log2(self.max_ram)) + 1)]

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with {self.__str__()} {self.manufacturer} {self.model}!")
        if ram not in self.valid_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.__str__()} {self.manufacturer} {self.model}!")

        processor_price = self.available_processors[processor]
        ram_price = log2(ram) * 100
        self.processor = processor
        self.ram = ram
        self.price = int(processor_price + ram_price)

        return f"Created {repr(self)} for {self.price}$."

    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
