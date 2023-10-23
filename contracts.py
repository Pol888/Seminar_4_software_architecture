"""РЕАЛИЗАЦИЯ КОНТРАКТА"""
import datetime
from abc import ABC, abstractmethod
from typing import Union
from ticket import Ticket


class BuyCostumer(ABC):
    @abstractmethod
    def buy_ticket(self, ticket: Ticket) -> bool:
        pass


class SearchTicket(ABC):
    @abstractmethod
    def search_ticket(self, subject_of_search: Union[datetime.date, int, float]):
        pass
