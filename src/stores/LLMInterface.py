from abc import ABC, abstractmethod

class LLMInterface(ABC):

    @abstractmethod
    def set_generation_model(self, model_id: str):
        """Set the generation model by its identifier."""
        pass

    @abstractmethod
    def set_embedding_model(self, model_id: str, embedding_size: int):
        """Set the embedding model by its identifier."""
        pass

    @abstractmethod
    def generate_text(self, prompt: str, chat_history: list=[], max_output_tokens: int=None, 
                            temperature: float = None):
        """Generate text based on the provided prompt."""
        pass

    @abstractmethod
    def embed_text(self, text: str, document_type: str=None):
        """Generate embeddings for the provided text."""
        pass

    @abstractmethod
    def construct_prompt(self, prompt: str, role: str):
        """Construct a prompt with a specific role."""
        pass