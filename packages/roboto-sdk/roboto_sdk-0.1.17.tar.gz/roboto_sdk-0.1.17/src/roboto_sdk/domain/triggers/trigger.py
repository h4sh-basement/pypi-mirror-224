#  Copyright (c) 2023 Roboto Technologies, Inc.

import collections.abc
from typing import Any, Optional

from ...domain.actions import (
    Action,
    ActionDelegate,
    ComputeRequirements,
    ContainerParameters,
    Invocation,
    InvocationDataSource,
    InvocationDelegate,
    InvocationSource,
)
from ...serde import pydantic_jsonable_dict
from .trigger_delegate import TriggerDelegate
from .trigger_record import TriggerRecord


class Trigger:
    __record: TriggerRecord
    __action_delegate: ActionDelegate
    __invocation_delegate: InvocationDelegate
    __trigger_delegate: TriggerDelegate

    @classmethod
    def create(
        cls,
        name: str,
        action_name: str,
        required_inputs: list[str],
        action_delegate: ActionDelegate,
        invocation_delegate: InvocationDelegate,
        trigger_delegate: TriggerDelegate,
        org_id: Optional[str] = None,
        compute_requirement_overrides: Optional[ComputeRequirements] = None,
        container_parameter_overrides: Optional[ContainerParameters] = None,
    ) -> "Trigger":
        """
        Creates an executor trigger, which automatically invokes an action on every new dataset that meets
        some acceptance criteria.

        :param name: A human-readable name for this trigger. Trigger names must be unique within each
        organization, though collisions are fine across different organizations.
        :param action_name: The name of an executor action that has been registered for the calling organization.
        If an action with the specified name is not found, the trigger will not be created. Furthermore, if the
        action bound to this trigger is ever deleted, the trigger will be deleted along with it.
        :param required_inputs: A list of GitIgnore path patterns with optional wildcard parameters that
        describe a set of files required to invoke an action described by this trigger against a given dataset.
        An action invocation will be spawned if at least one file is uploaded to match each listed condition.

        Once spawned, the invocation will also use the required_inputs patterns to control which files it downloads
        and makes available at runtime in the directory it points to via the `INPUT_DIR` environment variable. If you
        want to make the entire dataset available, just add a condition for "**/*" to the end of required_inputs.
        :param org_id: The ID of the organization the user is making this request on behalf of. If the user is only
        a member of one organization, this parameter will be set implicitly.
        :param compute_requirement_overrides: Overrides of the compute parameters specified in the action defined
        by action_name. Strictly optional.
        :param container_parameter_overrides: Overrides of the container parameters specified int eh action defined
        by action_name. Strictly optional.
        :param action_delegate: An abstraction object for performing actions against the `actions` API
        :param invocation_delegate: An abstraction object for performing actions against the `invocations` API
        :param trigger_delegate: An abstraction object for performing actions against the `triggers` API
        :return: A reference to a Trigger entity object which allow the user to perform additional operations on the
        newly created Trigger.
        """
        record = trigger_delegate.create_trigger(
            name=name,
            org_id=org_id,
            action_name=action_name,
            required_inputs=required_inputs,
            compute_requirement_overrides=compute_requirement_overrides,
            container_parameter_overrides=container_parameter_overrides,
        )
        return cls(
            record=record,
            action_delegate=action_delegate,
            invocation_delegate=invocation_delegate,
            trigger_delegate=trigger_delegate,
        )

    # And version?
    @classmethod
    def from_name(
        cls,
        name: str,
        action_delegate: ActionDelegate,
        invocation_delegate: InvocationDelegate,
        trigger_delegate: TriggerDelegate,
        org_id: Optional[str] = None,
    ) -> "Trigger":
        record = trigger_delegate.get_trigger_by_primary_key(name=name, org_id=org_id)
        return cls(
            record=record,
            action_delegate=action_delegate,
            invocation_delegate=invocation_delegate,
            trigger_delegate=trigger_delegate,
        )

    @classmethod
    def query(
        cls,
        filters: dict[str, Any],
        action_delegate: ActionDelegate,
        invocation_delegate: InvocationDelegate,
        trigger_delegate: TriggerDelegate,
        org_id: Optional[str] = None,
    ) -> collections.abc.Generator["Trigger", None, None]:
        paginated_results = trigger_delegate.query_triggers(
            filters=filters, org_id=org_id
        )
        while True:
            for record in paginated_results.items:
                yield cls(
                    record=record,
                    action_delegate=action_delegate,
                    invocation_delegate=invocation_delegate,
                    trigger_delegate=trigger_delegate,
                )
            if paginated_results.next_token:
                paginated_results = trigger_delegate.query_triggers(
                    filters=filters,
                    org_id=org_id,
                    page_token=paginated_results.next_token,
                )
            else:
                break

    def __init__(
        self,
        record: TriggerRecord,
        action_delegate: ActionDelegate,
        invocation_delegate: InvocationDelegate,
        trigger_delegate: TriggerDelegate,
    ):
        self.__record = record
        self.__action_delegate = action_delegate
        self.__invocation_delegate = invocation_delegate
        self.__trigger_delegate = trigger_delegate

    @property
    def name(self):
        return self.__record.name

    @property
    def record(self) -> TriggerRecord:
        return self.__record

    def delete(self):
        self.__trigger_delegate.delete_trigger(
            name=self.__record.name, org_id=self.__record.org_id
        )

    def action(self) -> Action:
        return Action.from_name(
            name=self.__record.action_name,
            action_delegate=self.__action_delegate,
            invocation_delegate=self.__invocation_delegate,
            org_id=self.__record.org_id,
        )

    def invoke(self, data_source: InvocationDataSource) -> Invocation:
        params: dict[str, Any] = {
            "input_data": self.__record.required_inputs,
            "data_source_id": data_source.data_source_id,
            "data_source_type": data_source.data_source_type,
            "invocation_source": InvocationSource.Trigger,
            "invocation_source_id": self.__record.name,
            "compute_requirement_overrides": self.__record.compute_requirement_overrides,
            "container_parameter_overrides": self.__record.container_parameter_overrides,
        }

        return self.action().invoke(**params)

    def to_dict(self) -> dict[str, Any]:
        return pydantic_jsonable_dict(self.__record)
