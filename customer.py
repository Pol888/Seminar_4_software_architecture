import datetime
from typing import Union
from contracts import BuyCostumer, SearchTicket
from ticket import Ticket


class Customer(BuyCostumer, SearchTicket):
    def __init__(self, id: int, tickets: list[Ticket], card: int):
        self.__id = id
        self.__tickets = tickets
        self.__cash: CashProvider = CashProvider(card)

    def buy_ticket(self, ticket: Ticket) -> bool:
        pass

    def search_ticket(self, subject_of_search: Union[datetime.date, int, float]):
        pass


class CashProvider:
    def __init__(self, card: int, is_authorization: bool = False):
        self.__card = card
        self.__is_authorization = is_authorization

    def buy(self, price: int) -> bool:
        pass

    def authorization(self, customer: Customer) -> bool:
        pass
