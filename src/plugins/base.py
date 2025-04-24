from abc import ABC, abstractmethod

class PluginBase(ABC):
    name: str
    description: str

    @abstractmethod
    def run(self, target: dict) -> dict:
        pass