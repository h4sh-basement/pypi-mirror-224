from typing import TypedDict, Optional, Dict, Any

from filum_utils.types.action import Action
from filum_utils.types.automated_action import AutomatedAction
from filum_utils.types.campaign import Campaign
from filum_utils.types.subscription import Subscription


class MessagePayload(TypedDict, total=False):
    organization_id: str
    organization_slug: str
    data: Optional[Dict[str, Any]]
    subscription: Subscription
    action: Action
    campaign: Optional[Campaign]
    automated_action: Optional[AutomatedAction]


class CallableResponse(TypedDict):
    success_count: int


class TriggerFunctionResponse(TypedDict):
    is_finished: bool
    success_count: Optional[int]
