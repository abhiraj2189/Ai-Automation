from abc import ABC, abstractmethod


class BaseVoiceProvider(ABC):

    @abstractmethod
    def generate(self, text: str, output_path: str):
        pass