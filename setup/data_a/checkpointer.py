import great_expectations as gx

class CheckpointerDataA():
    checkpoint_name = "checkpointer_data_a"
    
    def __init__(self, context) -> None:
        self.context = context

    def register_checkpointer(self, validation_definitions, action_list):
        if action_list:
            checkpoint = gx.Checkpoint(
                name=self.checkpoint_name,
                validation_definitions=validation_definitions,
                actions=action_list,
                result_format={"result_format": "COMPLETE"},
            )
            self.context.checkpoints.add(checkpoint)
        else:
            checkpoint = gx.Checkpoint(
                name=self.checkpoint_name,
                validation_definitions=validation_definitions,
                result_format={"result_format": "COMPLETE"},
            )
            self.context.checkpoints.add(checkpoint)

    def get_checkpointer(self):
        checkpoint = self.context.checkpoints.get(self.checkpoint_name)
        return checkpoint

