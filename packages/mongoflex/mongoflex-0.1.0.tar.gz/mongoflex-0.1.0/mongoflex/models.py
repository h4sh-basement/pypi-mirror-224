import re
from dataclasses import asdict, dataclass, field, fields
from typing import (
    Any,
    Dict,
    Generic,
    Iterable,
    Mapping,
    Optional,
    Sequence,
    TypeVar,
    Union,
)

from bson import ObjectId
from inflect import engine
from pymongo import IndexModel
from pymongo.collection import Collection
from pymongo.database import Database

from mongoflex.connection import get_database

__all__ = [
    "Model",
    "ModelMeta",
]

inflector = engine()

T = TypeVar("T", bound="Model")


def to_collection_name(class_name):
    words = [x.lower() for x in re.findall("[A-Z][^A-Z]*", class_name)]
    words[-1] = inflector.plural(words[-1])
    return "_".join(words)


class ModelMeta(type):
    models = []

    def __new__(cls, name, bases, attrs):
        if name not in ["Model", "BaseModel"]:
            attrs["collection"] = to_collection_name(name)

        model = super().__new__(cls, name, bases, attrs)

        if model.__name__ not in ["Model", "BaseModel"]:
            cls.models.append(model)

        return model

    def __init_subclass__(
        cls,
        /,
        database: str = None,
        collection: str = None,
        **kwargs,
    ) -> None:
        super().__init_subclass__(**kwargs)

        cls.database = cls.database or database
        cls.collection = cls.collection or collection

    def get_database(cls) -> Database:
        db_name = getattr(cls, "database", None)

        return get_database(db_name)

    @property
    def objects(cls) -> Collection:
        collection = cls.get_database().get_collection(cls.collection)

        indexes = getattr(cls, "INDEXES", [])

        if indexes:
            collection.create_indexes(indexes)

        return collection


class BaseModel(metaclass=ModelMeta):
    INDEXES: Sequence[IndexModel] = []


def as_model(func):
    def wrapper(cls, *args, **kwargs) -> Union[T, Iterable[T]]:
        response = func(cls, *args, **kwargs)

        if not response:
            return response

        if isinstance(response, dict):
            return cls.from_dict(response)

        return map(cls.from_dict, func(cls, *args, **kwargs))

    return wrapper


@dataclass(kw_only=True)
class Model(BaseModel, Generic[T]):
    _id: ObjectId = field(default_factory=ObjectId)

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, document: Dict[str, Any]) -> T:
        return cls(**document)

    def update(self, **kwargs):
        allowed_fields = [x.name for x in fields(self)]

        for key in kwargs.keys():
            if key not in allowed_fields:
                raise KeyError(f"Key {key} not allowed")

        self.__class__.objects.update_one(
            {"_id": self._id},
            {"$set": kwargs},
        )

        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        self.__class__.objects.update_one(
            {"_id": self._id}, {"$set": self.to_dict()}, upsert=True
        )

    @classmethod
    @as_model
    def find_one(
        cls, filter: Optional[Any] = None, *args: Any, **kwargs: Any
    ) -> Optional[T]:
        return cls.objects.find_one(filter, *args, **kwargs)

    @classmethod
    @as_model
    def find(
        cls, filter: Mapping[str, Any] = None, *args: Any, **kwargs: Any
    ) -> Iterable[T]:
        return cls.objects.find(filter, *args, **kwargs)
