import collections.abc
import copy
import typing

import pydantic

StrSequence = typing.Union[list[str], tuple[str, ...], set[str]]


class MetadataChangeset(pydantic.BaseModel):
    # Add each tag in this sequence if it doesn't exist
    put_tags: typing.Optional[StrSequence] = None
    # Remove each tag in this sequence if it exists
    remove_tags: typing.Optional[StrSequence] = None
    # Add each field in this dict if it doesn't exist, else overwrite the existing value
    # Expands dot notation to nested objects
    put_fields: typing.Optional[dict[str, typing.Any]] = None
    # Remove each field in this sequence if it exists
    # Expands dot notation to nested objects
    remove_fields: typing.Optional[StrSequence] = None

    def apply_field_updates(
        self, existing_metadata: dict[str, typing.Any]
    ) -> dict[str, typing.Any]:
        updated_metadata = copy.deepcopy(existing_metadata)
        if self.put_fields:
            for key, value in self.put_fields.items():
                self.__set_nested(updated_metadata, key, value)
        if self.remove_fields:
            for key in self.remove_fields:
                self.__del_nested(updated_metadata, key)
        return updated_metadata

    def apply_tag_updates(self, existing_tags: list[str]) -> StrSequence:
        updated_tags = existing_tags.copy()
        if self.put_tags:
            for tag in self.put_tags:
                if tag not in updated_tags:
                    updated_tags.append(tag)
        if self.remove_tags:
            updated_tags = [tag for tag in updated_tags if tag not in self.remove_tags]
        return updated_tags

    def combine(self, other: "MetadataChangeset") -> "MetadataChangeset":
        return self.copy(update=other.dict(exclude_unset=True, exclude_none=True))

    def is_empty(self) -> bool:
        return not any(
            [
                self.put_tags,
                self.remove_tags,
                self.put_fields,
                self.remove_fields,
            ]
        )

    def __set_nested(
        self, obj: dict[str, typing.Any], key: str, value: typing.Any
    ) -> None:
        """
        Set nested path to value using dot notation
        """
        keys = key.split(".")
        subobj = obj
        for key in keys[:-1]:
            if isinstance(subobj, collections.abc.MutableSequence):
                key = int(key)
                if key >= len(subobj):
                    raise IndexError(f"Index {key} out of range for {subobj}")
                subobj = subobj[key]
            else:
                subobj = subobj.setdefault(key, {})

        if isinstance(subobj, collections.abc.MutableMapping):
            subobj[keys[-1]] = value
        elif isinstance(subobj, collections.abc.MutableSequence):
            subobj.insert(int(keys[-1]), value)

    def __del_nested(self, obj: dict[str, typing.Any], key: str) -> None:
        """
        Delete a value from nested path using dot notation
        """

        def __key_in_collection(
            key: str | int, collection: collections.abc.Collection
        ) -> bool:
            if isinstance(collection, collections.abc.MutableSequence):
                key = int(key)
                return key < len(collection)
            else:
                return key in collection

        def __del_from_collection(
            key: str | int, collection: collections.abc.Collection
        ) -> None:
            if not __key_in_collection(key, collection):
                return

            if isinstance(collection, collections.abc.MutableMapping):
                del collection[key]
            elif isinstance(collection, collections.abc.MutableSequence):
                collection.pop(int(key))

        keys = key.split(".")
        path: list[
            tuple[
                # subobj
                typing.Union[
                    collections.abc.MutableMapping, collections.abc.MutableMapping
                ],
                # key
                typing.Optional[typing.Union[str, int]],
                # parent_obj
                typing.Optional[
                    typing.Union[
                        collections.abc.MutableMapping, collections.abc.MutableMapping
                    ]
                ],
            ]
        ] = [(obj, None, None)]
        for key in keys[:-1]:
            sub_obj, _, _ = path[-1]
            if isinstance(sub_obj, collections.abc.MutableSequence):
                key = int(key)

            if not __key_in_collection(key, sub_obj):
                return

            path.append((sub_obj[key], key, sub_obj))

        __del_from_collection(keys[-1], path[-1][0])

        # remove any now empty collections, working backwards
        for _, key_path, parent_obj in reversed(path):
            if key_path is None or parent_obj is None:
                # root object
                return

            if isinstance(parent_obj, collections.abc.MutableSequence):
                key_path = int(key_path)

            if not __key_in_collection(key_path, parent_obj):
                return

            if not len(parent_obj[key_path]):
                __del_from_collection(key_path, parent_obj)


class UpdateCondition(pydantic.BaseModel):
    """
    A condition to be applied to an update operation, succeeding only if the condition evaluates to True at update-time.

    `value` is compared to the resource's current value of `key` using `comparator`.

    This is a severely constrainted subset of the conditions supported by DynamoDB. See:
    https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.OperatorsAndFunctions.html
    """

    key: str
    value: typing.Any
    # Comparators are tied to convenience methods exposed on boto3.dynamodb.conditions.Attr. See:
    # https://github.com/boto/boto3/blob/5ad1a624111ed25efc81f425113fa51150516bb4/boto3/dynamodb/conditions.py#L246
    comparator: typing.Literal["eq", "ne"]
