import great_expectations as gx

class ExpectationsDataA():
    
    def __init__(self, context, suite_name) -> None:
        self.context = context
        self.suite_name = suite_name

    def get_expectations(self):
        list_expectation = []
        list_expectation.append(
            gx.expectations.ExpectColumnValuesToNotBeNull(
                column="age")
        )
        list_expectation.append(
            gx.expectations.ExpectColumnValuesToNotBeNull(
                column="gender")
        )
        list_expectation.append(
            gx.expectations.ExpectColumnValuesToNotBeNull(
                column="name")
        )
        list_expectation.append(
            gx.expectations.ExpectColumnValuesToBeBetween(
                column="age", max_value=6, min_value=0)
            )
        list_expectation.append(
            gx.expectations.ExpectColumnValuesToBeOfType(
                column="gender",
                type_="str"
        ))
        list_expectation.append(
            gx.expectations.ExpectColumnValuesToBeOfType(
                column="age",
                type_="int"
        ))
        list_expectation.append(
            gx.expectations.ExpectColumnValuesToBeOfType(
                column="name",
                type_="str"
        ))
        return list_expectation
    
    def register_suite(self):
        suite = gx.ExpectationSuite(name=self.suite_name)
        suite = self.context.suites.add(suite)
        list_expectation = self.get_expectations()
        for expectation in list_expectation:
            list_expectation = suite.add_expectation(expectation)

    def get_expectation_suite(self):
        suite = self.context.suites.get(name=self.suite_name)
        return suite