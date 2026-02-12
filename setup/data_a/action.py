from typing import Literal, Union

from typing_extensions import override

from great_expectations.checkpoint import (
    ActionContext,
    CheckpointResult,
    ValidationAction,
)

class CustomAction(ValidationAction):
    name: str = "custom_action"
    type: Literal["custom_action"] = "custom_action"
    message:str = ""
    @override
    def run(self,checkpoint_result: CheckpointResult, action_context: Union[ActionContext, None],) -> dict:
        self._print_to_console(checkpoint_result)
        message = self.message
        return {"some": "info", "extra_context": message}

    def _print_to_console(self, checkpoint_result: CheckpointResult):
        if checkpoint_result.success:
            self.message = "finish process, send notification"
            print(self.message)
        else:
            self.message = "result failed, finish process, send notification"
            print(self.message)
