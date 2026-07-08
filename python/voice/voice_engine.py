from abc import ABC, abstractmethod


class VoiceEngine(ABC):

    @abstractmethod
    def generate(
        self,
        text: str,
        language: str,
        output_path: str
    ) -> str:
        """
        Generate speech and save it to output_path.

        Returns:
            output_path
        """
        pass