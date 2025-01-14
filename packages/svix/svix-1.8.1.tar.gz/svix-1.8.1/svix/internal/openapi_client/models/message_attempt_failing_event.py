from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.message_attempt_failing_event_type import MessageAttemptFailingEventType

if TYPE_CHECKING:
    from ..models.message_attempt_failing_event_data import MessageAttemptFailingEventData


T = TypeVar("T", bound="MessageAttemptFailingEvent")


@attr.s(auto_attribs=True)
class MessageAttemptFailingEvent:
    """Sent after a message has been failing for a few times.
    It's sent on the fourth failure. It complements `message.attempt.exhausted` which is sent after the last failure.

        Attributes:
            data (MessageAttemptFailingEventData): Sent when a message delivery has failed (all of the retry attempts have
                been exhausted) as a "message.attempt.exhausted" type or after it's failed four times as a
                "message.attempt.failing" event.
            type (MessageAttemptFailingEventType):  Default: MessageAttemptFailingEventType.MESSAGE_ATTEMPT_FAILING.
    """

    data: "MessageAttemptFailingEventData"
    type: MessageAttemptFailingEventType = MessageAttemptFailingEventType.MESSAGE_ATTEMPT_FAILING
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data.to_dict()

        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message_attempt_failing_event_data import MessageAttemptFailingEventData

        d = src_dict.copy()
        data = MessageAttemptFailingEventData.from_dict(d.pop("data"))

        type = MessageAttemptFailingEventType(d.pop("type"))

        message_attempt_failing_event = cls(
            data=data,
            type=type,
        )

        message_attempt_failing_event.additional_properties = d
        return message_attempt_failing_event

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
