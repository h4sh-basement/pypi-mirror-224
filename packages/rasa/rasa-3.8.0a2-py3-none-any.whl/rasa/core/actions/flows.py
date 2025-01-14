from typing import Any, Dict, Optional, Text, List
import logging
from rasa.core.actions import action
from rasa.core.channels import OutputChannel
from rasa.cdu.flow_stack import FlowStack, FlowStackFrame, StackFrameType
from rasa.shared.constants import FLOW_PREFIX

from rasa.shared.core.constants import FLOW_STACK_SLOT
from rasa.shared.core.domain import Domain
from rasa.shared.core.events import (
    ActiveLoop,
    Event,
    SlotSet,
)
from rasa.core.nlg import NaturalLanguageGenerator
from rasa.shared.core.trackers import DialogueStateTracker

logger = logging.getLogger(__name__)


class FlowTriggerAction(action.Action):
    """Action which implements and executes the form logic."""

    def __init__(self, flow_action_name: Text) -> None:
        """Creates a `FlowTriggerAction`.

        Args:
            flow_action_name: Name of the flow.
        """
        super().__init__()
        self._flow_name = flow_action_name[len(FLOW_PREFIX) :]
        self._flow_action_name = flow_action_name

    def name(self) -> Text:
        """Return the flow name."""
        return self._flow_action_name

    async def run(
        self,
        output_channel: "OutputChannel",
        nlg: "NaturalLanguageGenerator",
        tracker: "DialogueStateTracker",
        domain: "Domain",
        metadata: Optional[Dict[Text, Any]] = None,
    ) -> List[Event]:
        """Trigger the flow."""
        stack = FlowStack.from_tracker(tracker)
        if self._flow_name == "pattern_continue_interrupted":
            frame_type = StackFrameType.RESUME
        elif tracker.active_loop_name and not stack.is_empty():
            frame_type = StackFrameType.INTERRUPT
        else:
            frame_type = StackFrameType.REGULAR

        stack.push(
            FlowStackFrame(
                flow_id=self._flow_name,
                frame_type=frame_type,
            )
        )

        slots_to_be_set = metadata.get("slots", {}) if metadata else {}
        slot_set_events: List[Event] = [
            SlotSet(key, value) for key, value in slots_to_be_set.items()
        ]

        events: List[Event] = [
            SlotSet(FLOW_STACK_SLOT, stack.as_dict())
        ] + slot_set_events
        if tracker.active_loop_name:
            events.append(ActiveLoop(None))

        return events
