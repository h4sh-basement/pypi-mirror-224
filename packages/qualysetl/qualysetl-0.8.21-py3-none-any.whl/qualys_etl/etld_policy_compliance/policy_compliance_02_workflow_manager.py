#!/usr/bin/env python3
import sys
import timeit
from qualys_etl.etld_lib import etld_lib_functions
from qualys_etl.etld_lib import etld_lib_config
#from qualys_etl.etld_lib import etld_lib_credentials
from qualys_etl.etld_lib import etld_lib_authentication_objects

from qualys_etl.etld_policy_compliance import policy_compliance_03_extract_controller
from qualys_etl.etld_policy_compliance import policy_compliance_05_transform_load_json_to_sqlite
from qualys_etl.etld_policy_compliance import policy_compliance_06_distribution

global start_time
global stop_time


def policy_compliance_03_extract_controller_wrapper(
        module_function=policy_compliance_03_extract_controller, message=""
):
    etld_lib_functions.logger.info(f"start {module_function} {message}")
    module_function.main()
    etld_lib_functions.logger.info(f"end   {module_function}")


def policy_compliance_05_transform_load_json_to_sqlite_wrapper(
        module_function=policy_compliance_05_transform_load_json_to_sqlite, message=""
):
    etld_lib_functions.logger.info(f"start {module_function} {message}")
    module_function.main()
    etld_lib_functions.logger.info(f"end   {module_function}")


def policy_compliance_06_distribution_wrapper(
        module_function=policy_compliance_06_distribution, message=""):
    etld_lib_functions.logger.info(f"start {module_function} {message}")
    module_function.main()
    etld_lib_functions.logger.info(f"end   {module_function}")


def begin_policy_compliance_02_workflow_manager():
    global start_time
    start_time = timeit.default_timer()
    etld_lib_functions.logger.info(f"__start__ policy_compliance_etl_workflow {str(sys.argv)}")


def end_policy_compliance_workflow_manager():
    global start_time
    global stop_time

    stop_time = timeit.default_timer()
    etld_lib_functions.logger.info(f"runtime for policy_compliance_etl_workflow in seconds: {stop_time - start_time:,}")
    etld_lib_functions.logger.info(f"__end__ policy_compliance_etl_workflow {str(sys.argv)}")


def policy_compliance_etl_workflow():
    try:
        begin_policy_compliance_02_workflow_manager()
        policy_compliance_03_extract_controller_wrapper(
            message=f"asset_last_updated={etld_lib_config.policy_compliance_asset_last_updated}")
        policy_compliance_06_distribution_wrapper()
        end_policy_compliance_workflow_manager()
    except Exception as e:
        etld_lib_functions.logger.error(f"Error occurred, please investigate {sys.argv}")
        etld_lib_functions.logger.error(f"Exception: {e}")
        exit(1)


def main():
    policy_compliance_etl_workflow()


if __name__ == "__main__":
    etld_lib_functions.main(my_logger_prog_name='policy_compliance_02_workflow_manager')
    etld_lib_config.main()
    #etld_lib_credentials.main()
    etld_lib_authentication_objects.main()
    main()
