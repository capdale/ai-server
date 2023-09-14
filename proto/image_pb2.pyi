from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ImageClassifierRequest(_message.Message):
    __slots__ = ["image"]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: bytes
    def __init__(self, image: _Optional[bytes] = ...) -> None: ...

class ImageClassifierReply(_message.Message):
    __slots__ = ["state", "class_index"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CLASS_INDEX_FIELD_NUMBER: _ClassVar[int]
    state: int
    class_index: int
    def __init__(self, state: _Optional[int] = ..., class_index: _Optional[int] = ...) -> None: ...
