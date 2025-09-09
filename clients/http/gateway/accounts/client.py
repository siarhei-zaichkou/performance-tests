from httpx import Response
from typing import TypedDict
from clients.http.client import HTTPClient


class GetAccountsQueryDict(TypedDict):
    """
    Структура данных для получения списка счетов пользователя.
    """
    userId: str

class OpenDepositAccountRequest(TypedDict):
    """
    Структура данных для открытия депозитного счета.
    """
    userId: str

class OpenSavingsAccountRequest(TypedDict):
    """
    Структура данных для открытия сберегательного счета.
    """
    userId: str

class OpenDebitCardAccountRequest(TypedDict):
    """
    Структура данных для открытия дебетового счета.
    """
    userId: str

class OpenCreditCardAccountRequest(TypedDict):
    """
    Структура данных для открытия кредитного счета.
    """
    userId: str

class AccountsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/accounts сервиса http-gateway.
    """

    def get_accounts_api(self, query: GetAccountsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка счетов пользователя.

        :param query: Словарь с параметрами запроса, например: {'userId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get("/api/v1/accounts", params=query)

    def open_deposit_account_api(self, request: OpenDepositAccountRequest):
        """
        Выполняет POST-запрос для открытия депозитного счёта.

        :param request: Словарь с userId.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post('/api/v1/accounts/open-deposit-account', json=request)

    def open_savings_account_api(self, request: OpenSavingsAccountRequest):
        """
        Выполняет POST-запрос для открытия сберегательного счёта.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post('/api/v1/accounts/open-savings-account', json=request)

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequest):
        """
        Выполняет POST-запрос для открытия дебетовой карты.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post('/api/v1/accounts/open-debit-card-account', json=request)

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequest):
        """
        Выполняет POST-запрос для открытия кредитной карты.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post('/api/v1/accounts/open-credit-card-account', json=request)
