from pydantic import BaseModel, Field, ConfigDict, HttpUrl


class DocumentDict(BaseModel):
    url: HttpUrl
    document: str


class GetTariffDocumentResponseDict(BaseModel):
    tariff: DocumentDict


class GetContractDocumentResponseDict(BaseModel):
    contract: DocumentDict
