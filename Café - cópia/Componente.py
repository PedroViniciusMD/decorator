from abc import ABC, abstractmethod


class Componente(ABC):
    @abstractmethod
    def get_descricao(self) -> str:
        pass
    
    @abstractmethod
    def get_preco(self) -> float:
        pass

