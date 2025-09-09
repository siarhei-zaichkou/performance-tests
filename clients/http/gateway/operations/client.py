from clients.http.client import HTTPClient
from httpx import Response
from typing import TypedDict


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
    Структура данных с общими полями для создания операций.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции комиссии.
    """
    pass


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции пополнения.
    """
    pass


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции кэшбэка.
    """
    pass


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции перевода.
    """
    pass


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции покупки.
    """
    category: str


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции оплаты по счету.
    """
    pass


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции по снятию наличных денег.
    """
    pass


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определенного счета.
        :param query: Словарь с параметрами запроса, например: {'accountId': '0cd6f602-ec37-4817-9b1d-15255aab71a3'}.
        :return: Объект httpx.Response с данными об операциях.
        """
        return self.get("/api/v1/operations", params=query)

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для определенного счета.
        :param query: Словарь с параметрами запроса, например: {'accountId': '0cd6f602-ec37-4817-9b1d-15255aab71a3'}.
        :return: Объект httpx.Response с данными о статистике операций.
        """
        return self.get("/api/v1/operations/operations-summary", params=query)

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение чека по операции по operation_id.
        :param operation_id: Идентификатор операции
        :return: Объект httpx.Response с данными чека.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение информации об операции по operation_id.
        :param operation_id: Идентификатор операции
        :return: Объект httpx.Response с данными операции.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции комиссии.
        :param request: Словарь с данными для создания операции комиссии.
        :return: Объект httpx.Response с данными о созданной операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции пополнения.
        :param request: Словарь с данными для создания операции пополнения.
        :return: Объект httpx.Response с данными о созданной операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции кэшбэка.
        :param request: Словарь с данными для создания операции кэшбэка.
        :return: Объект httpx.Response с данными о созданной операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции перевода.
        :param request: Словарь с данными для создания операции перевода.
        :return: Объект httpx.Response с данными о созданной операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции покупки.
        :param request: Словарь с данными для создания операции покупки.
        :return: Объект httpx.Response с данными о созданной операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции оплаты по счету.
        :param request: Словарь с данными для создания операции оплаты по счету.
        :return: Объект httpx.Response с данными о созданной операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции по снятию наличных денег.
        :param request: Словарь с данными для создания операции по снятию наличных денег.
        :return: Объект httpx.Response с данными о созданной операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)
