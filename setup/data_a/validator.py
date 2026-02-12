import great_expectations as gx

class ValidationDataA:
    definition_name = "validator_data_a"

    def __init__(self, context) -> None:
        self.context = context

    def register_validation(self, suite, batch_definition):
        validation_definition = gx.ValidationDefinition(
            data=batch_definition, suite=suite, name=self.definition_name
        )
        self.context.validation_definitions.add(validation_definition)

    def get_validator(self):
        validator = self.context.validation_definitions.get(self.definition_name)
        return validator