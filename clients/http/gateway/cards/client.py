from clients.http.client import HTTPClient
from httpx import Response
from typing import TypedDict


class IssueCardDict(TypedDict):
    """
    Структура данных для выпуска новой карты (физической или виртуальной).
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards/... сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: IssueCardDict) -> Response:
        """
        Выпуск новой виртуальной карты.

        :param request: Словарь с данными для выпуска новой виртуальной карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssueCardDict) -> Response:
        """
        Выпуск новой физической карты.

        :param request: Словарь с данными для выпуска новой физической карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)
