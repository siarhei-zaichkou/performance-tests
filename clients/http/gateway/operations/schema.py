from enum import StrEnum
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, HttpUrl


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class OperationReceiptSchema(BaseModel):
    url: HttpUrl
    document: str

class OperationsSummarySchema(BaseModel):
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")

class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")

class GetOperationsResponseSchema(BaseModel):
    operations: list[OperationSchema]

class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")

class GetOperationsSummaryResponseSchema(BaseModel):
    summary: OperationsSummarySchema

class GetOperationReceiptResponseSchema(BaseModel):
    receipt: OperationReceiptSchema

class GetOperationResponseSchema(BaseModel):
    operation: OperationSchema

class MakeOperationRequestSchema(BaseModel):
    """
    Структура данных с общими полями для создания операций.
    """
    model_config = ConfigDict(populate_by_name=True)
    status: str
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeOperationResponseSchema(BaseModel):
    operation: OperationSchema

class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции комиссии.
    """
    pass


class MakeFeeOperationResponseSchema(MakeOperationResponseSchema):
    pass


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции пополнения.
    """
    pass

class MakeTopUpOperationResponseSchema(MakeOperationResponseSchema):
    pass

class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции кэшбэка.
    """
    pass


class MakeCashbackOperationResponseSchema(MakeOperationResponseSchema):
    pass


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции перевода.
    """
    pass



class MakeTransferOperationResponseSchema(MakeOperationResponseSchema):
    pass


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции покупки.
    """
    category: str

class MakePurchaseOperationResponseSchema(MakeOperationResponseSchema):
    pass


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции оплаты по счету.
    """
    pass

class MakeBillPaymentOperationResponseSchema(MakeOperationResponseSchema):
    pass


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции по снятию наличных денег.
    """
    pass


class MakeCashWithdrawalOperationResponseSchema(MakeOperationResponseSchema):
    pass
