import datetime


class Ticket:
    def __init__(self, price_ticket: float, place: int, root_number: int, date_time: datetime.datetime):
        self.__price_ticket = price_ticket
        self.__place = place
        self.__root_number = root_number
        self.__date_time = date_time
        self.__is_valid: bool = True

    def __str__(self):
        return (f'Номер билета: {self.__root_number}, дата и время: {self.__date_time}, место: {self.__place}, цена '
                f'билета: {self.__price_ticket}')


class TicketProvider:

    def update_tickets(self, ticket: Ticket) -> bool:
        pass

    def get_ticket(self, __root_number) -> bool:
        pass
