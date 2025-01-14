# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .device_data import DeviceData
from .transaction_state import TransactionState
from .transaction_updatable import TransactionUpdatable


class TransactionEvent(pydantic.BaseModel):
    """
    Model for transaction-related events
    """

    transaction_state: TransactionState = pydantic.Field(alias="transactionState")
    timestamp: float = pydantic.Field(description="Timestamp of the event")
    transaction_id: str = pydantic.Field(
        alias="transactionId",
        description='Transaction ID the event pertains to <span style="white-space: nowrap">`non-empty`</span> ',
    )
    event_id: typing.Optional[str] = pydantic.Field(alias="eventId", description="Unique event ID")
    reason: typing.Optional[str] = pydantic.Field(description="Reason for the event or a state change")
    event_description: typing.Optional[str] = pydantic.Field(alias="eventDescription", description="Event description")
    updated_transaction_attributes: typing.Optional[TransactionUpdatable] = pydantic.Field(
        alias="updatedTransactionAttributes"
    )
    meta_data: typing.Optional[DeviceData] = pydantic.Field(alias="metaData")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
