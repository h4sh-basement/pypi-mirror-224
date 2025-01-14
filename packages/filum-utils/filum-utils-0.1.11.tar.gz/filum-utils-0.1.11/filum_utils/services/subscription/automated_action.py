from typing import Dict, Any, Optional, Callable, List

from filum_utils.clients.notification import RoutePath, PublisherType
from filum_utils.enums import ParentType
from filum_utils.services.subscription import SubscriptionService
from filum_utils.types.action import Action
from filum_utils.types.automated_action import AutomatedAction
from filum_utils.types.common import CallableResponse, TriggerFunctionResponse
from filum_utils.types.organization import Organization
from filum_utils.types.subscription import Subscription, SubscriptionData

Event = Optional[Dict[str, Any]]
Object = Optional[Dict[str, Any]]


class AutomatedActionSubscriptionService(SubscriptionService):
    def __init__(
        self,
        automated_action: AutomatedAction,
        subscription: Subscription,
        action: Action,
        organization: Organization
    ):
        super().__init__(subscription, organization)

        self.automated_action = automated_action
        self.action = action

    @property
    def parent(self):
        return self.automated_action

    @property
    def member_account_id(self):
        account = self.automated_action["account"] or {}
        return account.get("id")

    @property
    def run_type(self):
        return self.automated_action.get("run_type")

    @property
    def _parent_type(self):
        return ParentType.AUTOMATED_ACTION

    @property
    def _notification_route(self):
        return {
            "path": RoutePath.AUTOMATED_ACTIONS_DETAIL,
            "params": {
                "automatedActionId": self.automated_action["id"]
            }
        }

    @property
    def _notification_publisher_type(self):
        return PublisherType.AUTOMATED_ACTION

    def handle_real_time_trigger(
        self,
        process_real_time_fn: Callable[
            [Action, AutomatedAction, Organization, Event, SubscriptionData, Any],
            CallableResponse
        ],
        event: [Dict[str, Any]],
        **kwargs
    ) -> TriggerFunctionResponse:
        result = self._handle_trigger(
            process_real_time_fn,
            event,
            **kwargs
        )

        return {
            "is_finished": True,
            "success_count": result.get("success_count")
        }

    def handle_segment_manual_trigger(
        self,
        process_segment_manual_fn: Callable,
        properties: List[str],
        required_properties: Optional[List[List[str]]] = None,
        last_current_index: int = 0,
        **kwargs,
    ):
        ...

    def handle_object_manual_trigger(
        self,
        process_object_manual_fn: Callable[
            [Action, AutomatedAction, Organization, Object, SubscriptionData, Any],
            CallableResponse
        ],
        **kwargs,
    ):
        context = self.automated_action.get("context") or {}
        context_id = context.get("id")
        context_type = context.get("type")

        data = {}
        if context_type == Object.SEGMENT:
            data = self.filum_client.get_segment(
                segment_id=context_id,
                organization=self.subscription_client.get_organization()
            )
        elif context_type == Object.CAMPAIGN:
            data = self.filum_client.get_campaign(campaign_id=context_id)

        result = self._handle_trigger(
            process_fn=process_object_manual_fn,
            data=data,
            **kwargs,
        )

        return {
            "is_finished": True,
            "success_count": result.get("success_count")
        }

    def _handle_trigger(
        self,
        process_fn: Callable,
        data: Any,
        **kwargs,
    ):
        params = {
            "action": self.action,
            "automated_action": self.automated_action,
            "data": data,
            "subscription_data": self.subscription_data,
            "organization": self.organization,
            **kwargs
        }

        return process_fn(**params)
