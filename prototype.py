from setup.data_a.checkpointer import CheckpointerDataA
from setup.data_a.expectations import ExpectationsDataA
from setup.data_a.validator import ValidationDataA
from setup.data_a.action import CustomAction

import great_expectations as gx

# only relevant if using file system instead of memory
root_project_folder = "src/"
# only exist in memory, run for single python session
context = gx.get_context(mode="file",project_root_dir=root_project_folder)

# setup data source
data_source_name = "local_data_source"
source_folder = "data_source/csv"
data_source = context.data_sources.add_pandas_filesystem(
    name=data_source_name, base_directory=source_folder
)

# setup data asset
data_asset_name = "csv_asset"
data_asset = data_source.add_csv_asset(name=data_asset_name)

# setup batch definition
batch_definition_name = "test_batch"
batch_definition_path = "test.csv"
batch_definition = data_asset.add_batch_definition_path(
    name=batch_definition_name, path=batch_definition_path
)

# for easier development
# expectation is unit test
expectation = ExpectationsDataA(context=context, suite_name="data_a")
# Validator controls which dataset is tested against which expectation unit test
validator = ValidationDataA(context=context)
# checkpointer can run multiple validator and invoke action after validation process
checkpointer = CheckpointerDataA(context=context)
base_directory = "/home/rozen/Python/Architecture/Great Expectation Validation/data_docs/local_site"  # this is the default path (relative to the root folder of the Data Context) but can be changed as required
site_config = {
    "class_name": "SiteBuilder",
    "site_index_builder": {"class_name": "DefaultSiteIndexBuilder"},
    "store_backend": {
        "class_name": "TupleFilesystemStoreBackend",
        "base_directory": base_directory,
    },
}
site_name = "data_docs_site"
context.add_data_docs_site(site_name=site_name, site_config=site_config)
# simple custom action
action = CustomAction()


try:
    expectation.register_suite()
    suite = expectation.get_expectation_suite()
    validator.register_validation(suite=suite,batch_definition=batch_definition)
    validation = validator.get_validator()
    checkpointer.register_checkpointer(validation_definitions=[validation], action_list=[action])
    checkpointer = checkpointer.get_checkpointer()
    result = checkpointer.run()
    # build data docs manually after checkpointer run
    context.build_data_docs(site_names=site_name)
    if result.run_results:
        print(result.run_results)
except Exception as err:
    print(err)