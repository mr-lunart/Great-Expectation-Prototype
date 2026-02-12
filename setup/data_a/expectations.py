import great_expectations as gx

class ExpectationsDataA():
    suite_name = "data_a"
    
    def __init__(self, context) -> None:
        self.context = context

    def get_expectations(self):
        list_expectation = []
        list_expectation.append(gx.expectations.ExpectColumnValuesToBeBetween(
            column="age", max_value=6, min_value=1
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