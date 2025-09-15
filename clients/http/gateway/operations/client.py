from clients.http.client import HTTPClient
from httpx import Response, QueryParams
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    GetOperationsQuerySchema, GetOperationsSummaryQuerySchema,
    MakeFeeOperationRequestSchema, MakeTopUpOperationRequestSchema, MakeCashbackOperationRequestSchema,
    MakeTransferOperationRequestSchema, MakePurchaseOperationRequestSchema, MakeBillPaymentOperationRequestSchema,
    MakeCashWithdrawalOperationRequestSchema, GetOperationResponseSchema, GetOperationReceiptResponseSchema,
    GetOperationsResponseSchema, GetOperationsSummaryResponseSchema, MakeFeeOperationResponseSchema,
    MakeTopUpOperationResponseSchema, MakeCashbackOperationResponseSchema, MakeTransferOperationResponseSchema,
    MakePurchaseOperationResponseSchema, MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationResponseSchema
)


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определенного счета.
        :param query: Словарь с параметрами запроса, например: {'accountId': '0cd6f602-ec37-4817-9b1d-15255aab71a3'}.
        :return: Объект httpx.Response с данными об операциях.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для определенного счета.
        :param query: Словарь с параметрами запроса, например: {'accountId': '0cd6f602-ec37-4817-9b1d-15255aab71a3'}.
        :return: Объект httpx.Response с данными о статистике операций.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query.model_dump(by_alias=True)))

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

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос на создание операции комиссии.
        :param request: Словарь с данными для создания операции комиссии.
        :return: Объект httpx.Response с данными о созданной операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос на создание операции пополнения.
        :param request: Словарь с данными для создания операции пополнения.
        :return: Объект httpx.Response с данными о созданной операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос на создание операции кэшбэка.
        :param request: Словарь с данными для создания операции кэшбэка.
        :return: Объект httpx.Response с данными о созданной операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос на создание операции перевода.
        :param request: Словарь с данными для создания операции перевода.
        :return: Объект httpx.Response с данными о созданной операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос на создание операции покупки.
        :param request: Словарь с данными для создания операции покупки.
        :return: Объект httpx.Response с данными о созданной операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос на создание операции оплаты по счету.
        :param request: Словарь с данными для создания операции оплаты по счету.
        :return: Объект httpx.Response с данными о созданной операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос на создание операции по снятию наличных денег.
        :param request: Словарь с данными для создания операции по снятию наличных денег.
        :return: Объект httpx.Response с данными о созданной операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        request = MakeFeeOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        request = MakeTopUpOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        request = MakeCashbackOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        request = MakeTransferOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        request = MakePurchaseOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id,
            category="taxi"
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        request = MakeBillPaymentOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str,
                                       account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        request = MakeCashWithdrawalOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
