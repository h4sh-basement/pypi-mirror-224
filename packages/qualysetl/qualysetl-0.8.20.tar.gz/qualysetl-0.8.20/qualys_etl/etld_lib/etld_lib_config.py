from pathlib import Path
import os
import csv
import gzip
import re
import yaml
import resource
from qualys_etl.etld_lib import etld_lib_functions
from qualys_etl.etld_lib import etld_lib_datetime
# 2023-05-13 import oschmod
from qualys_etl.etld_lib import etld_lib_oschmod as oschmod


global setup_completed_flag           # Set to true when completed
global system_usage_counters          # Dict of system usage counters
# APPLICATION
global qetl_code_dir                  # Parent Directory of qualys_etl
global qetl_code_dir_child            # qualys_etl directory
global qetl_user_root_dir             # opt/qetl/users/{$USER NAME}
global qetl_all_users_dir             # opt/qetl/users
# TEMPLATES
global qetl_code_dir_etld_cred_yaml_template_path  # Template for initializing .etld_cred.yaml file.
# USER INIT
global qetl_create_user_dirs_ok_flag  # False.  Set to true by qetl_manage_user
global qualys_etl_user_home_env_var
global qetl_user_home_dir
global qetl_user_data_dir
global qetl_user_log_dir
global qetl_user_config_dir
global qetl_user_cred_dir
global qetl_user_cred_file
global qetl_user_bin_dir
global qetl_user_default_config
global qetl_user_config_settings_yaml_file
global qetl_user_config_settings_yaml
global etld_lib_config_settings_yaml_dict
global qetl_manage_user_selected_datetime
# Requests Module SSL Verify Status
global requests_module_tls_verify_status
# USER KNOWLEDGEBASE
global kb_data_dir
global kb_bin_dir
global kb_export_dir
global kb_last_modified_after
global kb_payload_option
global kb_extract_dir
global kb_extract_dir_file_search_blob
global kb_distribution_dir
global kb_distribution_dir_file_search_blob
global kb_distribution_csv_flag
global kb_distribution_csv_max_field_size
global kb_xml_file
global kb_shelve_file
global kb_sqlite_file
global kb_cve_qid_file
global kb_cve_qid_map_shelve
global kb_csv_file
global kb_json_file
global kb_log_file
global kb_log_table_name
global kb_lock_file
global kb_log_rotate_file
global kb_table_name
global kb_table_name_cve_list_view
global kb_table_name_merge_new_data
global kb_status_table_name
global kb_csv_truncate_cell_limit
global kb_data_files
global kb_present_csv_cell_as_json
global kb_truncation_limit
global kb_chunk_size_calc
global kb_try_extract_max_count
global kb_http_conn_timeout
global kb_open_file_compression_method

# USER HOST LIST
global host_list_data_dir
global host_list_export_dir
global host_list_vm_processed_after
global host_list_payload_option
global host_list_extract_dir
global host_list_extract_dir_file_search_blob
global host_list_distribution_dir
global host_list_distribution_dir_file_search_blob
global host_list_distribution_csv_flag
global host_list_distribution_csv_max_field_size
# TODO eliminate these variables
global host_list_xml_file_list
global host_list_other_xml_file
global host_list_ec2_xml_file
global host_list_gcp_xml_file
global host_list_azure_xml_file
global host_list_shelve_file

global host_list_sqlite_file
global host_list_csv_file
global host_list_json_file

global host_list_log_file
global host_list_lock_file
global host_list_log_rotate_file
global host_list_table_name
global host_list_status_table_name
global host_list_csv_truncate_cell_limit
global host_list_data_files
global host_list_present_csv_cell_as_json
global host_list_xml_to_sqlite_via_multiprocessing
global host_list_chunk_size_calc
global host_list_try_extract_max_count
global host_list_http_conn_timeout
global host_list_api_payload
global host_list_open_file_compression_method
global host_list_test_system_flag
global host_list_test_number_of_files_to_extract

# USER HOST LIST DETECTION
global host_list_detection_data_dir
global host_list_detection_export_dir
global host_list_detection_vm_processed_after
global host_list_detection_payload_option
global host_list_detection_extract_dir
global host_list_detection_extract_dir_file_search_blob
global host_list_detection_distribution_dir
global host_list_detection_distribution_dir_file_search_blob
global host_list_detection_distribution_csv_flag
global host_list_detection_distribution_csv_max_field_size
global host_list_detection_xml_file
global host_list_detection_shelve_file
global host_list_detection_sqlite_file
global host_list_detection_csv_truncate_cell_limit
global host_list_detection_csv_file
global host_list_detection_json_file
global host_list_detection_log_file
global host_list_detection_lock_file
global host_list_detection_log_rotate_file
global host_list_detection_concurrency_limit
global host_list_detection_multi_proc_batch_size
global host_list_detection_limit_hosts
global host_list_detection_hosts_table_name
global host_list_detection_q_knowledgebase_in_host_list_detection
global host_list_detection_qids_table_name
global host_list_detection_table_view_name
global host_list_detection_status_table_name
global host_list_detection_data_files
global host_list_detection_present_csv_cell_as_json
global host_list_detection_chunk_size_calc
global host_list_detection_try_extract_max_count
global host_list_detection_http_conn_timeout
global host_list_detection_api_payload
global host_list_detection_open_file_compression_method
global host_list_detection_xml_to_sqlite_via_multiprocessing

# USER ASSET INVENTORY
global asset_inventory_data_dir
global asset_inventory_export_dir
global asset_inventory_asset_last_updated
global asset_inventory_payload_option
global asset_inventory_json_batch_file
global asset_inventory_extract_dir
global asset_inventory_extract_dir_file_search_blob
global asset_inventory_extract_dir_file_search_blob_two
global asset_inventory_distribution_dir
global asset_inventory_distribution_dir_file_search_blob
global asset_inventory_distribution_csv_flag
global asset_inventory_distribution_csv_max_field_size
global asset_inventory_shelve_software_assetid_file
global asset_inventory_shelve_software_unique_file
global asset_inventory_shelve_software_os_unique_file
global asset_inventory_shelve_file
global asset_inventory_sqlite_file
global asset_inventory_csv_truncate_cell_limit
global asset_inventory_csv_file
global asset_inventory_csv_software_assetid_file
global asset_inventory_csv_software_unique_file
global asset_inventory_csv_software_os_unique_file
global asset_inventory_json_file
global asset_inventory_log_file
global asset_inventory_lock_file
global asset_inventory_log_rotate_file
global asset_inventory_concurrency_limit
global asset_inventory_multi_proc_batch_size
global asset_inventory_limit_hosts
global asset_inventory_table_name
global asset_inventory_status_table_name
global asset_inventory_table_name_software_unique
global asset_inventory_table_name_software_os_unique
global asset_inventory_table_name_software_assetid
global asset_inventory_data_files
global asset_inventory_temp_shelve_file
global asset_inventory_present_csv_cell_as_json
global asset_inventory_json_to_sqlite_via_multiprocessing
global asset_inventory_chunk_size_calc
global asset_inventory_try_extract_max_count
global asset_inventory_http_conn_timeout
global asset_inventory_open_file_compression_method
global asset_inventory_test_system_flag
global asset_inventory_test_number_of_files_to_extract
global asset_inventory_last_seen_asset_id_for_restart

# test system global variables
global test_system_log_file
global test_system_log_rotate_file
global test_system_lock_file
global test_system_test_intermediary_extract_flag

# WAS system global variables
global was_data_dir
global was_export_dir
global was_webapp_last_scan_date
global was_payload_option
global was_extract_dir
global was_extract_dir_file_search_blob
global was_extract_dir_file_search_blob_webapp
global was_extract_dir_file_search_blob_webapp_detail
global was_extract_dir_file_search_blob_finding
global was_extract_dir_file_search_blob_finding_detail
global was_extract_dir_file_search_blob_catalog
global was_extract_dir_file_search_blob_webapp_count
global was_extract_dir_file_search_blob_finding_count
global was_extract_dir_file_search_blob_catalog_count
global was_distribution_dir
global was_distribution_dir_file_search_blob
global was_distribution_csv_flag
global was_distribution_csv_max_field_size
global was_sqlite_file
global was_log_file
global was_lock_file
global was_log_rotate_file
global was_concurrency_limit
global was_multi_proc_batch_size
global was_limit_hosts
global was_status_table_name
global was_webapp_table_name
global was_finding_table_name
global was_catalog_table_name
global was_q_knowledgebase_in_was_finding_table
global was_data_files
global was_json_to_sqlite_via_multiprocessing
global was_chunk_size_calc
global was_try_extract_max_count
global was_http_conn_timeout
global was_open_file_compression_method
global was_test_system_flag
global was_test_number_of_files_to_extract
global was_catalog_start_greater_than_last_id

# POLICY COMPLIANCE PCRS
global policy_compliance_data_dir
global policy_compliance_export_dir
global policy_compliance_asset_last_updated
global policy_compliance_payload_option
global policy_compliance_json_batch_file
global policy_compliance_extract_dir
global policy_compliance_extract_dir_file_search_blob
global policy_compliance_extract_dir_file_search_blob_two
global policy_compliance_distribution_dir
global policy_compliance_distribution_dir_file_search_blob
global policy_compliance_distribution_csv_flag
global policy_compliance_distribution_csv_max_field_size
global policy_compliance_sqlite_file
global policy_compliance_csv_file
global policy_compliance_csv_software_assetid_file
global policy_compliance_csv_software_unique_file
global policy_compliance_csv_software_os_unique_file
global policy_compliance_json_file
global policy_compliance_log_file
global policy_compliance_lock_file
global policy_compliance_log_rotate_file
global policy_compliance_concurrency_limit
global policy_compliance_multi_proc_batch_size
global policy_compliance_limit_hosts
global policy_compliance_table_name
global policy_compliance_status_table_name
global policy_compliance_table_name_policy_list
global policy_compliance_table_name_policy_host_ids
global policy_compliance_table_name_posture_info
global policy_compliance_data_files
global policy_compliance_temp_shelve_file
global policy_compliance_present_csv_cell_as_json
global policy_compliance_json_to_sqlite_via_multiprocessing
global policy_compliance_chunk_size_calc
global policy_compliance_try_extract_max_count
global policy_compliance_http_conn_timeout
global policy_compliance_open_file_compression_method
global policy_compliance_test_system_flag
global policy_compliance_test_number_of_files_to_extract
global policy_compliance_last_seen_asset_id_for_restart

# CSV Distribution CSV Writer Options
global csv_distribution_python_csv_quoting
global csv_distribution_python_csv_dialect_delimiter
global csv_distribution_python_csv_dialect_doublequote
global csv_distribution_python_csv_dialect_escapechar
global csv_distribution_python_csv_dialect_lineterminator
global csv_distribution_python_csv_dialect_quotechar
global csv_distribution_python_csv_dialect_skipinitialspace
global csv_distribution_python_csv_dialect_strict
global csv_distribution_mysql_load_example

qetl_create_user_dirs_ok_flag = False      # Automatically create unknown user directories default - False
qetl_manage_user_selected_datetime = None  # Initialize qetl_manage_user datetime to None
system_usage_counters = []                 # Initialize system usage counters dictionary
default_distribution_csv_max_field_size = 1000000
test_system_do_not_test_intermediary_extracts_flag = False  # Set to True when running etld_lib_test_system

# Useful to run thorugh all known workflows.
etl_workflow_list = ['knowledgebase_etl_workflow','host_list_etl_workflow',
                     'host_list_detection_etl_workflow', 'asset_inventory_etl_workflow',
                     'was_etl_workflow', 'test_system_etl_workflow']


def get_etl_workflow_data_location_dict(etl_workflow) -> dict:

    # Useful when qetl_manage_user -e validate_etl_[workflow] is executed.
    etl_test_workflow_no_logs = False
    if etl_workflow == 'validate_etl_knowledgebase':
        etl_workflow = 'knowledgebase_etl_workflow'
    if etl_workflow.startswith('knowledgebase_0'):
        etl_workflow = 'knowledgebase_etl_workflow'
        etl_test_workflow_no_logs = True
    elif etl_workflow == 'validate_etl_host_list':
        etl_workflow = 'host_list_etl_workflow'
    elif etl_workflow.startswith('host_list_0'):
        etl_workflow = 'host_list_etl_workflow'
        etl_test_workflow_no_logs = True
    elif etl_workflow.startswith('host_list_detection_0'):
        etl_workflow = 'host_list_detection_etl_workflow'
        etl_test_workflow_no_logs = True
    elif etl_workflow == 'validate_etl_host_list_detection':
        etl_workflow = 'host_list_detection_etl_workflow'
    elif etl_workflow.startswith('asset_inventory_0'):
        etl_workflow = 'asset_inventory_etl_workflow'
        etl_test_workflow_no_logs = True
    elif etl_workflow == 'validate_etl_asset_inventory':
        etl_workflow = 'asset_inventory_etl_workflow'
    elif etl_workflow.startswith('was_0'):
        etl_workflow = 'was_etl_workflow'
        etl_test_workflow_no_logs = True
    elif etl_workflow == 'validate_etl_was':
        etl_workflow = 'was_etl_workflow'
    elif etl_workflow.startswith('test_system_0'):
        etl_workflow = 'test_system_etl_workflow'
        etl_test_workflow_no_logs = True
    elif etl_workflow == 'validate_etl_test_system':
        etl_workflow = 'test_system_etl_workflow'

    etl_workflow_location_dict = \
        {
            'test_system_etl_workflow':
                {
                    'etl_workflow': 'test_system_etl_workflow',
                    'sqlite_file': None,
                    'log_file': test_system_log_file,
                    'etl_test_workflow_no_logs': etl_test_workflow_no_logs,
                },
            'knowledgebase_etl_workflow':
                {
                    'etl_workflow': 'knowledgebase_etl_workflow',
                    'sqlite_file': kb_sqlite_file,
                    'log_file': kb_log_file,
                    'extract_dir': kb_extract_dir,
                    'distribution_dir': kb_distribution_dir,
                    'csv_max_field_size': kb_distribution_csv_max_field_size,
                    'etl_test_workflow_no_logs': etl_test_workflow_no_logs,
                    'csv_distribution_display_counter_at': 25000,
                    'open_file_compression_method': kb_open_file_compression_method
                  },
            'host_list_etl_workflow':
                {
                    'etl_workflow': 'host_list_etl_workflow',
                    'sqlite_file': host_list_sqlite_file,
                    'log_file': host_list_log_file,
                    'extract_dir': host_list_extract_dir,
                    'distribution_dir': host_list_distribution_dir,
                    'csv_max_field_size': host_list_distribution_csv_max_field_size,
                    'etl_test_workflow_no_logs': etl_test_workflow_no_logs,
                    'csv_distribution_display_counter_at': 25000,
                    'open_file_compression_method': host_list_open_file_compression_method
                },
            'host_list_detection_etl_workflow':
                {
                    'etl_workflow': 'host_list_detection_etl_workflow',
                    'sqlite_file': host_list_detection_sqlite_file,
                    'log_file': host_list_detection_log_file,
                    'extract_dir': host_list_detection_extract_dir,
                    'distribution_dir': host_list_detection_distribution_dir,
                    'csv_max_field_size': host_list_detection_distribution_csv_max_field_size,
                    'etl_test_workflow_no_logs': etl_test_workflow_no_logs,
                    'csv_distribution_display_counter_at': 250000,
                    'open_file_compression_method': host_list_detection_open_file_compression_method
                },
            'asset_inventory_etl_workflow':
                {
                    'etl_workflow': 'asset_inventory_etl_workflow',
                    'sqlite_file': asset_inventory_sqlite_file,
                    'log_file': asset_inventory_log_file,
                    'extract_dir': asset_inventory_extract_dir,
                    'distribution_dir': asset_inventory_distribution_dir,
                    'csv_max_field_size': asset_inventory_distribution_csv_max_field_size,
                    'etl_test_workflow_no_logs': etl_test_workflow_no_logs,
                    'csv_distribution_display_counter_at': 10000,
                    'open_file_compression_method': asset_inventory_open_file_compression_method
                },
            'was_etl_workflow':
                {
                    'etl_workflow': 'was_etl_workflow',
                    'sqlite_file': was_sqlite_file,
                    'log_file': was_log_file,
                    'extract_dir': was_extract_dir,
                    'distribution_dir': was_distribution_dir,
                    'csv_max_field_size': was_distribution_csv_max_field_size,
                    'etl_test_workflow_no_logs': etl_test_workflow_no_logs,
                    'csv_distribution_display_counter_at': 10000,
                    'open_file_compression_method': was_open_file_compression_method
                }
         }
    if etl_workflow in etl_workflow_location_dict:
        return etl_workflow_location_dict[etl_workflow]
    else:
        return {}


def prepare_extract_batch_file_name(next_batch_number_str='batch_000001',
                                    next_batch_date='1970-01-01T00:00:00Z',
                                    extract_dir=None,
                                    file_name_type="host_list_detection",
                                    file_name_option="vm_processed_after",
                                    file_name_option_date='1970-01-01T00:00:00Z',
                                    file_extension="xml",
                                    compression_method=open):

    next_batch_number = int(next_batch_number_str.split("_")[1])
    next_file_name = f"{file_name_type}" \
                     f"_utc_run_datetime_" \
                     f"{next_batch_date}" \
                     f"_utc_" \
                     f"{file_name_option}" \
                     f"_" \
                     f"{file_name_option_date}" \
                     f"_" \
                     f"{next_batch_number_str}.{file_extension}"
    if compression_method == gzip.open:
        next_file_name = next_file_name + ".gz"
    next_file_path = Path(extract_dir, next_file_name)
    return {
            'next_batch_number': next_batch_number,
            'next_batch_number_str': next_batch_number_str,
            'next_file_name': next_file_name,
            'next_file_path': next_file_path
            }


def create_directory(dir_path=None):
    if dir_path is not None:
        os.makedirs(dir_path, exist_ok=True)
        # 2023-05-13 oschmod.set_mode(dir_path, "a+rwx,g-rwx,o-rwx")
        oschmod.set_mode(dir_path, "u+rwx,g-rwx,o-rwx")


def remove_old_files(dir_path=None,
                     dir_search_glob=None,
                     other_files_list: list = [],
                     other_files_list_exclusions: list = []):
    if dir_path is None or dir_search_glob is None:
        return True

    if Path(dir_path).is_dir() is not True:
        create_directory(dir_path)

    if Path(dir_path).is_dir():
        file_list = list(Path(dir_path).glob(dir_search_glob))
        count_files = len(file_list)
        etld_lib_functions.logger.info(f"Removing {count_files} old files from dir: {dir_path}")
        try:
            for file_name in file_list:
                if Path(file_name).is_file():
                    etld_lib_functions.logger.info(f"Removing old file: {str(file_name)}")
                    Path(file_name).unlink()
        except OSError as e:
            etld_lib_functions.logger.error(f"{e}")
            exit(1)
    try:
        for file_name in other_files_list:
            if file_name in other_files_list_exclusions:
                pass
            else:
                if Path(file_name).is_file():
                    etld_lib_functions.logger.info(f"Removing old file: {str(file_name)}")
                    Path(file_name).unlink()

    except Exception as e:
        etld_lib_functions.logger.error(f"{e}")
        exit(1)


def get_attribute_from_config_settings(key, default_value, fix_escape=False):
    new_value = ""
    if key in etld_lib_config_settings_yaml_dict.keys():
        new_value = etld_lib_config_settings_yaml_dict.get(key)
    else:
        new_value = default_value
    if fix_escape and isinstance(new_value, str):
        new_value = new_value.replace('\\n', '\n')
        new_value = new_value.replace('\\t', '\t')
        new_value = new_value.replace('\\\\', '\\')

    return new_value


def setup_csv_distribution_vars():
    global csv_distribution_python_csv_quoting
    global csv_distribution_python_csv_dialect_delimiter
    global csv_distribution_python_csv_dialect_doublequote
    global csv_distribution_python_csv_dialect_escapechar
    global csv_distribution_python_csv_dialect_lineterminator
    global csv_distribution_python_csv_dialect_quotechar
    global csv_distribution_python_csv_dialect_skipinitialspace
    global csv_distribution_python_csv_dialect_strict
    global csv_distribution_mysql_load_example

    # DEFAULTS SET HERE
    # See https://docs.python.org/3/library/csv.html#csv-fmt-params
    csv_distribution_python_csv_quoting = 'csv.QUOTE_NONE'
    csv_distribution_python_csv_dialect_delimiter = '\t'
    csv_distribution_python_csv_dialect_doublequote = False
    csv_distribution_python_csv_dialect_escapechar = '\\'
    csv_distribution_python_csv_dialect_lineterminator = '\n'
    csv_distribution_python_csv_dialect_quotechar = None
    csv_distribution_python_csv_dialect_skipinitialspace = False
    csv_distribution_python_csv_dialect_strict = False
    csv_distribution_mysql_load_example = '''mysql $PORT_OPT -v -e "LOAD DATA LOCAL INFILE '/dev/stdin' INTO TABLE ${TABLE_NAME} CHARACTER SET UTF8 FIELDS TERMINATED BY '\\t' ESCAPED BY '\\\\' LINES TERMINATED BY '\\n';"'''

    # csv_writer = csv.writer(
    #     file_handle,
    #     quoting=csv.QUOTE_MINIMAL,  # Minimal quoting
    #     delimiter=',',  # Comma delimited
    #     doublequote=True,  # Controls how instances of quotechar appearing inside a field should be quoted
    #     escapechar=None,  # A string of one character used to escape delimiter when quoting is set to QUOTE_NONE
    #     lineterminator='\n',  # Specifies the character sequence which should terminate rows
    #     quotechar='"',  # A one-character string used to quote fields containing special characters
    #     skipinitialspace=False,  # When True, whitespace immediately following the delimiter is ignored
    #     strict=etld_lib_config.csv_distribution_python_csv_dialect_strict  # When True, raise exception Error on bad CSV input
    # )


def get_python_csv_quoting_option_dict():
    csv_quoting_dict = {
        'csv.QUOTE_ALL': csv.QUOTE_ALL,
        'csv.QUOTE_MINIMAL': csv.QUOTE_MINIMAL,
        'csv.QUOTE_NONNUMERIC': csv.QUOTE_NONNUMERIC,
        'csv.QUOTE_NONE': csv.QUOTE_NONE
                        }
    return csv_quoting_dict


def get_python_csv_quoting_option_key(csv_value=None):
    csv_key = ""
    csv_quote_dict = get_python_csv_quoting_option_dict()
    for key, value in csv_quote_dict.items():
        if csv_value == value:
            csv_key = key
    return csv_key


def get_csv_distribution_config():
    global csv_distribution_python_csv_quoting
    global csv_distribution_python_csv_dialect_delimiter
    global csv_distribution_python_csv_dialect_doublequote
    global csv_distribution_python_csv_dialect_escapechar
    global csv_distribution_python_csv_dialect_lineterminator
    global csv_distribution_python_csv_dialect_quotechar
    global csv_distribution_python_csv_dialect_skipinitialspace
    global csv_distribution_python_csv_dialect_strict

    csv_quoting_dict = get_python_csv_quoting_option_dict()

    csv_distribution_python_csv_quoting = \
    get_attribute_from_config_settings('csv_distribution_python_csv_quoting',
                                       csv_distribution_python_csv_quoting, True)
    if csv_distribution_python_csv_quoting in csv_quoting_dict:
        csv_quoting = csv_quoting_dict[csv_distribution_python_csv_quoting]
        etld_lib_functions.logger.info(f"csv_distribution_python_csv_quoting: {csv_distribution_python_csv_quoting}"
                                       f" is being reset to literal: {csv_quoting}")
        csv_distribution_python_csv_quoting = csv_quoting
    else:
        etld_lib_functions.logger.error(f"invalid etld_config_settings.yaml seeting csv_distribution_python_csv_quoting: {csv_distribution_python_csv_quoting}")
        etld_lib_functions.logger.error(f"error reported, setting to csv_distribution_python_csv_quoting to default csv.QUOTE_MINIMAL")
        etld_lib_functions.logger.error(f"job will continue, please fix etld_config_settings.yaml.")
        etld_lib_functions.logger.error(f"valid values for csv_distribution_python_csv_quoting are: 'csv.QUOTE_ALL' or 'csv.QUOTE_MINIMAL' or 'csv.QUOTE_NONNUMERIC' or 'csv.QUOTE_NONE'")
        etld_lib_functions.logger.error(f"see python csv constants: https://docs.python.org/3/library/csv.html#csv.QUOTE_ALL")
        csv_distribution_python_csv_quoting = csv.QUOTE_MINIMAL

    csv_distribution_python_csv_dialect_delimiter = \
    get_attribute_from_config_settings('csv_distribution_python_csv_dialect_delimiter',
                                       csv_distribution_python_csv_dialect_delimiter, True)
    csv_distribution_python_csv_dialect_doublequote = \
    get_attribute_from_config_settings('csv_distribution_python_csv_dialect_doublequote',
                                       csv_distribution_python_csv_dialect_doublequote, True)
    csv_distribution_python_csv_dialect_escapechar = \
    get_attribute_from_config_settings('csv_distribution_python_csv_dialect_escapechar',
                                       csv_distribution_python_csv_dialect_escapechar, True)
    csv_distribution_python_csv_dialect_lineterminator = \
    get_attribute_from_config_settings('csv_distribution_python_csv_dialect_lineterminator',
                                       csv_distribution_python_csv_dialect_lineterminator, True)
    csv_distribution_python_csv_dialect_quotechar = \
    get_attribute_from_config_settings('csv_distribution_python_csv_dialect_quotechar',
                                       csv_distribution_python_csv_dialect_quotechar, True)
    if csv_distribution_python_csv_dialect_quotechar == 'None':
        csv_distribution_python_csv_dialect_quotechar = None

    csv_distribution_python_csv_dialect_skipinitialspace = \
    get_attribute_from_config_settings('csv_distribution_python_csv_dialect_skipinitialspace',
                                       csv_distribution_python_csv_dialect_skipinitialspace, True)
    csv_distribution_python_csv_dialect_strict = \
    get_attribute_from_config_settings('csv_distribution_python_csv_dialect_strict',
                                       csv_distribution_python_csv_dialect_strict, True)

def get_csv_distribution_var_dict() -> dict:
    global csv_distribution_python_csv_quoting
    global csv_distribution_python_csv_dialect_delimiter
    global csv_distribution_python_csv_dialect_doublequote
    global csv_distribution_python_csv_dialect_escapechar
    global csv_distribution_python_csv_dialect_lineterminator
    global csv_distribution_python_csv_dialect_quotechar
    global csv_distribution_python_csv_dialect_skipinitialspace
    global csv_distribution_python_csv_dialect_strict

    csv_distribution_writer_options = {
        'quoting': csv_distribution_python_csv_quoting,
        'delimiter': csv_distribution_python_csv_dialect_delimiter,
        'doublequote': csv_distribution_python_csv_dialect_doublequote,
        'escapechar': csv_distribution_python_csv_dialect_escapechar,
        'lineterminator': csv_distribution_python_csv_dialect_lineterminator,
        'quotechar': csv_distribution_python_csv_dialect_quotechar,
        'skipinitialspace': csv_distribution_python_csv_dialect_skipinitialspace,
        'strict': csv_distribution_python_csv_dialect_strict
    }
    return csv_distribution_writer_options

def get_open_file_compression_method_from_config_settings(key):
    compression_method = gzip.open
#    if key in etld_lib_config_settings_yaml_dict.keys():
#        if etld_lib_config_settings_yaml_dict[key] == 'open':
#            compression_method = open
    return compression_method


def set_api_payload(payload_default: dict, payload_option_from_config):
    payload_option = get_attribute_from_config_settings(payload_option_from_config, 'default')
    if isinstance(payload_option, dict):
        payload = get_attribute_from_config_settings(payload_option_from_config, {})
        for key in payload_default:
            if key not in payload.keys():
                payload[key] = payload_default[key]
    else:
        payload = payload_default
    return payload


def set_path_qetl_user_home_dir():
    global qualys_etl_user_home_env_var
    global qetl_user_home_dir
    global qetl_user_root_dir
    global qetl_all_users_dir
    global qetl_user_data_dir
    global qetl_user_log_dir
    global qetl_user_config_dir
    global qetl_user_cred_dir
    global qetl_user_cred_file
    global qetl_user_bin_dir

    if os.environ.keys().__contains__("qualys_etl_user_home") is not True:
        # qetl_all_users_dir = Path(Path.home(), 'opt', 'qetl', 'users')
        # qetl_user_root_dir = Path(Path.home(), 'opt', 'qetl', 'users', 'default_user')
        # qetl_user_home_dir = Path(qetl_user_root_dir, 'qetl_home')
        # Entry is now qetl_manage_user.  If qualys_etl_user_home env is not set, then abort.
        try:
            etld_lib_functions.logger.error(f"Error, no qualys_etl_user_home.")
            etld_lib_functions.logger.error(f"Ensure you are running qetl_manage_user to run your job")
            etld_lib_functions.logger.error(f"see qetl_manage_user -h for options.")
            exit(1)
        except AttributeError as e:
            print(f"Error, no qualys_etl_user_home.")
            print(f"Ensure you are using opt/qetl/users as part of your path")
            print(f"see qetl_manage_user -h for options.")
            print(f"Exception {e}")
            exit(1)
    else:
        qualys_etl_user_home_env_var = Path(os.environ.get("qualys_etl_user_home"))
        # Strip qetl_home if the user accidentally added it.
        qualys_etl_user_home_env_var = \
            Path(re.sub("/qetl_home.*$", "", str(qualys_etl_user_home_env_var)))
        # Ensure prefix is opt/qetl/users
        if qualys_etl_user_home_env_var.parent.name == 'users' and \
            qualys_etl_user_home_env_var.parent.parent.name == 'qetl' and \
                qualys_etl_user_home_env_var.parent.parent.parent.name == 'opt':
            # Valid directory ${USER DIR}/opt/qetl/users/{QualysUser}/qetl_home
            qetl_all_users_dir = qualys_etl_user_home_env_var.parent
            qetl_user_root_dir = qualys_etl_user_home_env_var
            qetl_user_home_dir = Path(qualys_etl_user_home_env_var, 'qetl_home')
        else:
            # User directory not set correctly to include opt/qetl/users, abort
            try:
                etld_lib_functions.logger.error(f"error setting user home directory: {qualys_etl_user_home_env_var}")
                etld_lib_functions.logger.error(f"Ensure you are using opt/qetl/users as part of your path")
                etld_lib_functions.logger.error(f"see qetl_manage_user -h for options.")
                exit(1)
            except AttributeError as e:
                print(f"error setting user home directory: {qualys_etl_user_home_env_var}")
                print(f"Ensure you are using opt/qetl/users as part of your path")
                print(f"see qetl_manage_user -h for options.")
                print(f"Exception {e}")
                exit(1)

    qetl_user_data_dir = Path(qetl_user_home_dir, "data")
    qetl_user_log_dir = Path(qetl_user_home_dir, "log")
    qetl_user_config_dir = Path(qetl_user_home_dir, "config")
    qetl_user_cred_dir = Path(qetl_user_home_dir, "cred")
    qetl_user_cred_file = Path(qetl_user_cred_dir, ".etld_cred.yaml")
    qetl_user_bin_dir = Path(qetl_user_home_dir, "bin")
    validate_char_qetl_user_home_dir(qetl_user_home_dir)
    setup_csv_distribution_vars()
    setup_kb_vars()
    setup_host_list_vars()
    setup_host_list_detection_vars()
    setup_asset_inventory_vars()
    setup_was_vars()
    setup_test_system_vars()


def create_user_data_dirs():
    global qetl_user_data_dir
    global qetl_user_log_dir
    global qetl_user_config_dir
    global qetl_user_cred_dir
    global qetl_user_bin_dir
    global qetl_create_user_dirs_ok_flag  # False.  Set to true by qetl_manage_user
    if qetl_create_user_dirs_ok_flag is True:
        try:
            os.makedirs(qetl_user_home_dir, exist_ok=True)
            # 2023-05-13 oschmod.set_mode(qetl_user_home_dir, "a+rwx,g-rwx,o-rwx")
            oschmod.set_mode(qetl_user_home_dir, "u+rwx,g-rwx,o-rwx")
            os.makedirs(qetl_user_data_dir, exist_ok=True)
            # 2023-05-13 oschmod.set_mode(qetl_user_data_dir, "a+rwx,g-rwx,o-rwx")
            oschmod.set_mode(qetl_user_data_dir, "u+rwx,g-rwx,o-rwx")
            os.makedirs(qetl_user_log_dir, exist_ok=True)
            # 2023-05-13 oschmod.set_mode(qetl_user_log_dir, "a+rwx,g-rwx,o-rwx")
            oschmod.set_mode(qetl_user_log_dir, "u+rwx,g-rwx,o-rwx")
            os.makedirs(qetl_user_config_dir, exist_ok=True)
            # 2023-05-13 oschmod.set_mode(qetl_user_config_dir, "a+rwx,g-rwx,o-rwx")
            oschmod.set_mode(qetl_user_config_dir, "u+rwx,g-rwx,o-rwx")
            os.makedirs(qetl_user_cred_dir, exist_ok=True)
            # 2023-05-13 oschmod.set_mode(qetl_user_cred_dir, "a+rwx,g-rwx,o-rwx")
            oschmod.set_mode(qetl_user_cred_dir, "u+rwx,g-rwx,o-rwx")
            os.makedirs(qetl_user_bin_dir, exist_ok=True)
            # 2023-05-13 oschmod.set_mode(qetl_user_bin_dir, "a+rwx,g-rwx,o-rwx")
            oschmod.set_mode(qetl_user_bin_dir, "u+rwx,g-rwx,o-rwx")
        except Exception as e:
            etld_lib_functions.logger.error(
                f"error creating qetl home directories.  check permissions on "
                f"{str(qetl_user_home_dir.parent.parent)}")
            etld_lib_functions.logger.error(
                f"determine if permissions on file allow creating directories "
                f"{str(qetl_user_home_dir.parent.parent)}")
            etld_lib_functions.logger.error(f"Exception: {e}")
    elif Path(qetl_user_home_dir).is_dir() and \
        Path(qetl_user_log_dir).is_dir() and \
            Path(qetl_user_config_dir).is_dir() and \
            Path(qetl_user_cred_dir).is_dir() and \
            Path(qetl_user_bin_dir).is_dir() and \
            Path(qetl_user_data_dir).is_dir():
        pass
    else:
        try:
            etld_lib_functions.logger.error(
                f"error with qetl home directories. "
                f" Check {str(qetl_user_home_dir)} for data,config,log,bin,cred directories exist.")
            etld_lib_functions.logger.error(
                f"Use qetl_manage_user -h to create your qetl "
                f"user home directories if they don't exists.")
            exit(1)
        except AttributeError as ae:
            print(f"error with qetl home directories. "
                  f" Check {str(qetl_user_home_dir)} for data,config,log,bin,cred directories exist.")
            print(f"Use qetl_manage_user -h to create your qetl user home directories if they don't exists.")
            print(f"Exception {ae}")
            exit(1)


def validate_char_qetl_user_home_dir(p: Path):
    p_match = re.fullmatch(r"[_A-Za-z0-9/]+", str(p))
    if etld_lib_functions.logging_is_on_flag is False:
        logging_method = print
    else:
        logging_method = etld_lib_functions.logger.error

    if p_match is None:
        logging_method(f"see qetl_manage_user -h, malformed parent directory: {p}")
        logging_method(f" Characters other than [_A-Za-z0-9/]+ found: {str(p)}")
        exit(1)
    if p.name != 'qetl_home':
        logging_method(f"see qetl_manage_user -h, malformed parent directory: {p}")
        logging_method(f" qetl_home not found: {str(p)}")
        exit(1)
    if p.parent.parent.name != 'users':
        logging_method(f"see qetl_manage_user -h, malformed parent directory: {p}")
        logging_method(f" users not found in parent: {str(p)}")
        exit(1)
    if p.parent.parent.parent.name != 'qetl':
        logging_method(f"see qetl_manage_user -h, malformed parent directory: {p}")
        logging_method(f" qetl not found in parent: {str(p)}")
        exit(1)
    if p.parent.parent.parent.parent.name != 'opt':
        logging_method(f"see qetl_manage_user -h, malformed parent directory: {p}")
        logging_method(f" opt not found in parent: {str(p)}")
        exit(1)

# DATA ENVIRONMENT AND DIRECTORIES
#
# Data Directory Structures and contents are:
#  - qetl_user_home_dir
#  - qetl_user_home_dir/qetl_home/data - All XML, JSON, CSV, SQLITE Data
#  - qetl_user_home_dir/qetl_home/log  - Optional Logs Location
#  - qetl_user_home_dir/qetl_home/config - date configurations for knowledgebase, host list and host list detection
#  - qetl_user_home_dir/qetl_home/cred   - Qualys Credentials Directory, ensure this is secure.
#  - qetl_user_home_dir/qetl_home/bin    - Initial Canned Scripts for Qualys API User


def setup_user_home_directories():
    # TODO setup home directories before logging so
    # TODO we can reference paths in qetl_manage_user before logging is turned on.
    # Directory Structure
    #  ${ANYDIR}/opt/qetl/users/${NAME OF USER}/qetl_home
    #
    #  qetl_user_root_dir = ${ANYDIR}/opt/qetl/users/{$NAME OF USER} = directory of a qetl user.
    #                       Ex. /home/dgregory/opt/qetl/users/{$NAME OF USER}
    #                       Ex. /opt/qetl/users/{$NAME OF USER}
    #  qetl_user_home_dir = ${ANYDIR}/opt/qetl/users/{$NAME OF USER}/qetl_home
    #                       Ex. /home/dgregory/opt/qetl/users/quays01/qetl_home
    #
    # Top level directories
    global qetl_all_users_dir            # opt/qetl/users
    global qetl_user_root_dir            # Parent directory for qetl_user_home_dir
    global qualys_etl_user_home_env_var  # Environment variable set to qualys_etl_user_home
    global qetl_user_home_dir            # Home directory for api data, config, credentials, logs.
    # Directories holding a users data
    global qetl_user_data_dir            # xml,json,csv,sqlite,shelve data
    global qetl_user_log_dir             # logs
    global qetl_user_config_dir          # configuration
    global qetl_user_cred_dir            # credentials
    global qetl_user_cred_file           # credentials
    global qetl_user_bin_dir             # TODO determine what to do with qetl_user_bin_dir

    global qetl_user_config_settings_yaml_file
    global qetl_user_config_settings_yaml

    global qetl_code_dir                 # Parent Directory of qualys_etl code dir.
    global qetl_code_dir_etld_cred_yaml_template_path
    global qetl_user_default_config      # Initial configuration populated into qetl_user_config_dir

    set_path_qetl_user_home_dir()
    create_user_data_dirs()

    etld_lib_functions.logger.info(f"parent user app dir  - {str(qetl_user_root_dir)}")
    etld_lib_functions.logger.info(f"user home directory  - {str(qetl_user_home_dir)}")
    etld_lib_functions.logger.info(f"qetl_all_users_dir   - All users dir       - {qetl_all_users_dir}")
    etld_lib_functions.logger.info(f"qetl_user_root_dir   - User root dir       - {qetl_user_root_dir}")
    etld_lib_functions.logger.info(f"qetl_user_home_dir   - qualys user         - {qetl_user_home_dir}")
    etld_lib_functions.logger.info(f"qetl_user_data_dir   - xml,json,csv,sqlite - {qetl_user_data_dir}")
    etld_lib_functions.logger.info(f"qetl_user_log_dir    - log files           - {qetl_user_log_dir}")
    etld_lib_functions.logger.info(f"qetl_user_config_dir - yaml configuration  - {qetl_user_config_dir}")
    etld_lib_functions.logger.info(f"qetl_user_cred_dir   - yaml credentials    - {qetl_user_cred_dir}")
    etld_lib_functions.logger.info(f"qetl_user_bin_dir    - etl scripts         - {qetl_user_bin_dir}")


def load_etld_lib_config_settings_yaml():
    #
    # sets global etld_lib_config_settings_yaml_dict for reuse
    #
    global qetl_user_home_dir
    global qetl_user_data_dir
    global qetl_user_log_dir
    global qetl_user_config_dir
    global qetl_user_cred_dir
    global qetl_user_cred_file
    global qetl_user_bin_dir
    global qetl_user_default_config
    global etld_lib_config_settings_yaml_dict
    global qetl_user_config_settings_yaml_file

# Create Default YAML if it doesn't exist.
    qetl_user_config_settings_yaml_file = Path(qetl_user_config_dir, "etld_config_settings.yaml")
    if not Path.is_file(qetl_user_config_settings_yaml_file):  # api_home/cred/etld_config_settings.yaml
        etld_lib_config_template = \
            Path(qetl_code_dir, "qualys_etl", "etld_templates", "etld_config_settings.yaml")
        # Get Template
        with open(str(etld_lib_config_template), "r", encoding='utf-8') as etld_lib_config_template_f:
            etld_lib_config_template_string = etld_lib_config_template_f.read()

        # Write etld_lib_config_template_string to users directory.
        with open(qetl_user_config_settings_yaml_file, 'w', encoding='utf-8') as acf:
            local_date = etld_lib_datetime.get_local_date()  # Add date updated to file
            etld_lib_config_template_string = re.sub('\$DATE', local_date, etld_lib_config_template_string)
            acf.write(etld_lib_config_template_string)

    oschmod.set_mode(str(qetl_user_config_settings_yaml_file), "u+rw,u-x,go-rwx")

# Read YAML into global etld_lib_config_settings_yaml_dict

    try:
        with open(qetl_user_config_settings_yaml_file, 'r', encoding='utf-8') as etld_lib_config_yaml_file:
            etld_lib_config_settings_yaml_dict = yaml.safe_load(etld_lib_config_yaml_file)
            for key in etld_lib_config_settings_yaml_dict.keys():
                etld_lib_functions.logger.info(
                    f"etld_config_settings.yaml - {key}: {etld_lib_config_settings_yaml_dict.get(key)} ")
    except Exception as e:
        etld_lib_functions.logger.error(f"etld_config_settings.yaml Exception: {e}")
        exit(1)


def setup_test_system_vars():
    global test_system_log_file
    global test_system_log_rotate_file
    global test_system_lock_file
    test_system_log_file = Path(qetl_user_log_dir, "test_system.log")
    test_system_lock_file = Path(qetl_user_log_dir, ".test_system.lock")
    test_system_log_rotate_file = Path(qetl_user_log_dir, "test_system.1.log")


def get_kb_user_config():
    global kb_export_dir
    global kb_last_modified_after
    global kb_payload_option
    global kb_extract_dir
    global kb_extract_dir_file_search_blob
    global kb_distribution_dir
    global kb_distribution_dir_file_search_blob
    global kb_distribution_csv_flag
    global kb_distribution_csv_max_field_size
    global default_distribution_csv_max_field_size
    global qetl_user_config_settings_yaml_file
    global kb_csv_truncate_cell_limit
    global kb_present_csv_cell_as_json
    global kb_truncation_limit
    global kb_chunk_size_calc
    global kb_try_extract_max_count
    global kb_http_conn_timeout
    global kb_open_file_compression_method

    def set_kb_last_modified_after():
        global kb_last_modified_after
        kb_last_modified_after = get_attribute_from_config_settings('kb_last_modified_after', 'default')
        if qetl_manage_user_selected_datetime is not None:
            kb_last_modified_after = qetl_manage_user_selected_datetime
            etld_lib_functions.logger.info(f"kb_last_modified_after set by qetl_manage_user "
                                           f"-d option - {kb_last_modified_after}")
        elif kb_last_modified_after == 'default':
            # kb_last_modified_after = etld_lib_datetime.get_utc_date_minus_days(7)
            # Keep default so knowledgebase_04_extract can set the date to max_date found in database.
            pass
        else:
            etld_lib_functions.logger.info(f"kb_last_modified_after yaml - {kb_last_modified_after}")

        if kb_last_modified_after == 'default':
            pass
        elif etld_lib_datetime.is_valid_qualys_datetime_format(kb_last_modified_after) is False:
            etld_lib_functions.logger.error(f"kb_last_modified_after date is not in correct form "
                                            f"(YYYY-MM-DDThh:mm:ssZ) date is {kb_last_modified_after}")

    kb_payload_option = \
        {'action': 'list', 'details': 'All', 'show_disabled_flag': '1', 'show_qid_change_log': '1',
         'show_supported_modules_info': '1', 'show_pci_reasons': '1'}

    kb_extract_dir = Path(kb_data_dir, "knowledgebase_extract_dir")
    kb_extract_dir_file_search_blob = 'kb_utc*'

    kb_distribution_dir = Path(kb_data_dir, "knowledgebase_distribution_dir")
    kb_distribution_dir_file_search_blob = 'Q_*'
    kb_distribution_csv_flag = get_attribute_from_config_settings('kb_distribution_csv_flag', False)
    kb_distribution_csv_max_field_size = \
        get_attribute_from_config_settings('kb_distribution_csv_max_field_size', default_distribution_csv_max_field_size)

    kb_export_dir = get_attribute_from_config_settings('kb_export_dir', 'default')
    set_kb_last_modified_after()
    kb_csv_truncate_cell_limit = 0  # get_attribute_from_config_settings('kb_csv_truncate_cell_limit', 0)
    kb_present_csv_cell_as_json = get_attribute_from_config_settings('kb_present_csv_cell_as_json', True)
    kb_truncation_limit = \
        get_attribute_from_config_settings('kb_truncation_limit', '0')
    kb_chunk_size_calc = int(get_attribute_from_config_settings('kb_chunk_size_calc', '20480'))
    kb_try_extract_max_count = int(get_attribute_from_config_settings('kb_try_extract_max_count', '30'))
    kb_http_conn_timeout = int(get_attribute_from_config_settings('kb_http_conn_timeout', '900'))
    kb_open_file_compression_method = \
        get_open_file_compression_method_from_config_settings('kb_open_file_compression_method')

    etld_lib_functions.logger.info(f"knowledgeBase config - {qetl_user_config_settings_yaml_file}")
    etld_lib_functions.logger.info(f"kb_export_dir yaml   - {kb_export_dir}")


def setup_kb_vars():
    global qetl_user_data_dir
    global kb_data_dir
    global kb_bin_dir
    global kb_xml_file
    global kb_shelve_file
    global kb_sqlite_file
    global kb_cve_qid_file
    global kb_cve_qid_map_shelve
    global kb_csv_file
    global kb_json_file
    global kb_log_file
    global kb_log_table_name
    global kb_lock_file
    global kb_log_rotate_file
    global kb_table_name
    global kb_table_name_cve_list_view
    global kb_table_name_merge_new_data
    global kb_status_table_name
    global kb_data_files

    kb_data_dir = qetl_user_data_dir
    kb_bin_dir = qetl_user_bin_dir
    kb_xml_file = Path(kb_data_dir, "kb.xml")
    kb_shelve_file = Path(kb_data_dir, "kb_shelve")
    kb_sqlite_file = Path(kb_data_dir, "kb_sqlite.db")
    kb_cve_qid_file = Path(kb_data_dir, "kb_cve_qid_map.csv")
    kb_cve_qid_map_shelve = Path(kb_data_dir, "kb_cve_qid_map_shelve")
    kb_csv_file = Path(kb_data_dir, "kb.csv")
    kb_json_file = Path(kb_data_dir, "kb.json")
    kb_log_file = Path(qetl_user_log_dir, "kb.log")
    kb_log_table_name = 'Q_KnowledgeBase_RUN_LOG'
    kb_lock_file = Path(qetl_user_log_dir, ".kb.lock")
    kb_log_rotate_file = Path(qetl_user_log_dir, "kb.1.log")
    kb_table_name = 'Q_KnowledgeBase'
    kb_table_name_cve_list_view = 'Q_KnowledgeBase_CVE_LIST'
    kb_table_name_merge_new_data = 'Q_KnowledgeBase_Merge_New_Data'
    kb_status_table_name = 'Q_KnowledgeBase_Status'
    kb_data_files = [kb_xml_file, kb_shelve_file, kb_sqlite_file, kb_cve_qid_file, kb_cve_qid_map_shelve, kb_csv_file,
                     kb_json_file]


def get_host_list_user_config():
    global host_list_data_dir
    global host_list_export_dir
    global host_list_distribution_csv_flag
    global host_list_distribution_csv_max_field_size
    global default_distribution_csv_max_field_size
    global qetl_user_config_settings_yaml_file
    global host_list_vm_processed_after
    global host_list_payload_option
    global qetl_manage_user_selected_datetime
    global host_list_csv_truncate_cell_limit
    global host_list_sqlite_file
    global host_list_present_csv_cell_as_json
    global host_list_xml_to_sqlite_via_multiprocessing
    global host_list_chunk_size_calc
    global host_list_try_extract_max_count
    global host_list_http_conn_timeout
    global host_list_api_payload
    global host_list_open_file_compression_method
    global host_list_test_system_flag
    global host_list_test_number_of_files_to_extract

    def set_host_list_vm_processed_after():
        global host_list_vm_processed_after
        host_list_vm_processed_after = get_attribute_from_config_settings('host_list_vm_processed_after', 'default')
        if qetl_manage_user_selected_datetime is not None:
            host_list_vm_processed_after = qetl_manage_user_selected_datetime
            etld_lib_functions.logger.info(f"host_list_vm_processed_after set by qetl_manage_user -d option - "
                                           f"{host_list_vm_processed_after}")
        elif host_list_vm_processed_after == 'default':
            host_list_vm_processed_after = etld_lib_datetime.get_utc_date_minus_days(7)
            # (min_date, max_date) = etld_lib_sqlite_tables.get_q_table_min_max_dates(
            #     host_list_sqlite_file, "LAST_VULN_SCAN_DATETIME", "Q_Host_List")
            # if str(max_date).startswith("20"):
            #     etld_lib_functions.logger.info(f"Found Q_Host_List Min Date: {min_date} Max Date: {max_date}")
            #     max_date = re.sub(":..$", ":00", max_date)
            #     max_date = re.sub(" ", "T", max_date)
            #     max_date = re.sub("$", "Z", max_date)
            #     host_list_vm_processed_after = max_date
            #     etld_lib_functions.logger.info(
            #         f"host_list_vm_processed_after using max_date from database - {host_list_vm_processed_after}")
            # else:
            #     host_list_vm_processed_after = etld_lib_datetime.get_utc_date_minus_days(1)
            #     etld_lib_functions.logger.info(
            #         f"host_list_vm_processed_after using utc.now minus 1 days - {host_list_vm_processed_after}")
        else:
            etld_lib_functions.logger.info(f"host_list_vm_processed_after yaml - {host_list_vm_processed_after}")

        if not etld_lib_datetime.is_valid_qualys_datetime_format(host_list_vm_processed_after):
            etld_lib_functions.logger.error(
                f"Format Error host_list_vm_processed_after: {host_list_vm_processed_after} ")
            exit(1)

        if str(host_list_vm_processed_after).__contains__("1970"):  # Don't add date to process all data.
            return {}
        else:
            return {'vm_processed_after': host_list_vm_processed_after}

    def set_host_list_api_payload():
        global host_list_api_payload
        global host_list_payload_option

        # QWEB < 10.23
        #host_list_payload_default = {'action': 'list', 'details': 'All', 'truncation_limit': '25000', 'show_tags': '1',
        #                             'show_cloud_tags': '1', 'show_asset_id': '1', 'host_metadata': 'all'}

        # QWEB >= 10.23
        host_list_payload_default = {
            'action': 'list', 'details': 'All', 'truncation_limit': '25000', 'show_tags': '1',
            'show_cloud_tags': '1', 'show_asset_id': '1', 'host_metadata': 'all',
            'show_trurisk': '1', 'show_trurisk_factors': '1'
        }

        host_list_payload_option = get_attribute_from_config_settings('host_list_payload_option', 'default')
        host_list_api_payload = set_api_payload(host_list_payload_default, 'host_list_payload_option')
        host_list_show_tags = get_attribute_from_config_settings('host_list_show_tags', '1')  # Legacy support
        if host_list_show_tags == '0':
            host_list_api_payload.update({'show_tags': '0'})
        host_list_api_payload.update(set_host_list_vm_processed_after())

    host_list_data_dir = qetl_user_data_dir
    host_list_export_dir = get_attribute_from_config_settings('host_list_export_dir', 'default')
    host_list_distribution_csv_flag = get_attribute_from_config_settings('host_list_distribution_csv_flag', False)
    host_list_distribution_csv_max_field_size = \
        get_attribute_from_config_settings('host_list_distribution_csv_max_field_size', default_distribution_csv_max_field_size)
    host_list_xml_to_sqlite_via_multiprocessing = \
        get_attribute_from_config_settings('host_list_xml_to_sqlite_via_multiprocessing', True)
    host_list_csv_truncate_cell_limit = 0
    # get_attribute_from_config_settings('host_list_csv_truncate_cell_limit', '0')

    host_list_present_csv_cell_as_json = get_attribute_from_config_settings('host_list_present_csv_cell_as_json', True)
    host_list_chunk_size_calc = int(get_attribute_from_config_settings('host_list_chunk_size_calc', '20480'))
    host_list_try_extract_max_count = int(get_attribute_from_config_settings('host_list_try_extract_max_count', '30'))
    host_list_http_conn_timeout = int(get_attribute_from_config_settings('host_list_http_conn_timeout', '900'))
    host_list_open_file_compression_method = \
        get_open_file_compression_method_from_config_settings('host_list_open_file_compression_method')
    host_list_test_system_flag = \
        get_attribute_from_config_settings('host_list_test_system_flag', False)
    host_list_test_number_of_files_to_extract = \
        get_attribute_from_config_settings('host_list_test_number_of_files_to_extract', 2)
    set_host_list_api_payload()
    etld_lib_functions.logger.info(f"host list config - {qetl_user_config_settings_yaml_file}")
    etld_lib_functions.logger.info(f"host_list_export_dir - {host_list_export_dir}")


def setup_host_list_vars():
    global qetl_user_data_dir
    global host_list_data_dir
    global host_list_extract_dir
    global host_list_extract_dir_file_search_blob
    global host_list_distribution_dir
    global host_list_distribution_dir_file_search_blob
    # TODO eliminate these variables
    global host_list_xml_file_list
    global host_list_other_xml_file
    global host_list_ec2_xml_file
    global host_list_gcp_xml_file
    global host_list_azure_xml_file
    global host_list_shelve_file

    global host_list_sqlite_file
    global host_list_csv_file
    global host_list_json_file
    global host_list_log_file
    global host_list_lock_file
    global host_list_log_rotate_file
    global host_list_table_name
    global host_list_status_table_name
    global host_list_data_files

    host_list_data_dir = qetl_user_data_dir
    host_list_extract_dir = Path(host_list_data_dir, "host_list_extract_dir")
    host_list_extract_dir_file_search_blob = 'host_list_utc*'
    host_list_distribution_dir = Path(host_list_data_dir, "host_list_distribution_dir")
    host_list_distribution_dir_file_search_blob = 'Q_*'
    host_list_other_xml_file = Path(host_list_data_dir, "host_list_other_file.xml")
    host_list_ec2_xml_file = Path(host_list_data_dir, "host_list_ec2_file.xml")
    host_list_gcp_xml_file = Path(host_list_data_dir, "host_list_gcp_file.xml")
    host_list_azure_xml_file = Path(host_list_data_dir, "host_list_azure_file.xml")
    host_list_xml_file_list = [host_list_other_xml_file, host_list_ec2_xml_file,
                               host_list_gcp_xml_file, host_list_azure_xml_file]
    host_list_shelve_file = Path(host_list_data_dir, "host_list_shelve")
    host_list_sqlite_file = Path(host_list_data_dir, "host_list_sqlite.db")
    host_list_csv_file = Path(host_list_data_dir, "host_list.csv")
    host_list_json_file = Path(host_list_data_dir, "host_list.json")
    host_list_log_file = Path(qetl_user_log_dir, "host_list.log")
    host_list_lock_file = Path(qetl_user_log_dir, ".host_list.lock")
    host_list_log_rotate_file = Path(qetl_user_log_dir, "host_list.1.log")
    host_list_table_name = 'Q_Host_List'
    host_list_status_table_name = 'Q_Host_List_Status'
    host_list_data_files = [host_list_other_xml_file, host_list_ec2_xml_file, host_list_gcp_xml_file,
                            host_list_azure_xml_file, host_list_shelve_file, host_list_sqlite_file,
                            host_list_csv_file, host_list_json_file]


def get_host_list_detection_user_config():
    global host_list_detection_data_dir
    global host_list_detection_export_dir
    global host_list_detection_distribution_csv_flag
    global host_list_detection_distribution_csv_max_field_size
    global default_distribution_csv_max_field_size
    global host_list_detection_vm_processed_after
    global host_list_detection_payload_option
    global host_list_detection_concurrency_limit
    global host_list_detection_multi_proc_batch_size
    global host_list_detection_limit_hosts
    global host_list_detection_csv_truncate_cell_limit
    global qetl_user_config_settings_yaml_file
    global qetl_manage_user_selected_datetime
    global host_list_vm_processed_after
    global host_list_detection_present_csv_cell_as_json
    global host_list_detection_chunk_size_calc
    global host_list_detection_try_extract_max_count
    global host_list_detection_http_conn_timeout
    global host_list_detection_api_payload
    global host_list_detection_open_file_compression_method
    global host_list_detection_xml_to_sqlite_via_multiprocessing

    def set_host_list_detection_vm_processed_after():
        global host_list_detection_vm_processed_after
        global host_list_vm_processed_after

        host_list_detection_vm_processed_after = \
            get_attribute_from_config_settings('host_list_detection_vm_processed_after', 'default')
        if qetl_manage_user_selected_datetime is not None:
            host_list_detection_vm_processed_after = qetl_manage_user_selected_datetime
            host_list_vm_processed_after = qetl_manage_user_selected_datetime
            etld_lib_functions.logger.info(f"host_list_detection_vm_processed_after and host_list_vm_processed_after "
                                           f"set by qetl_manage_user -d option")
        # FOR TESTING
        elif host_list_detection_vm_processed_after == 'default':
            host_list_detection_vm_processed_after = etld_lib_datetime.get_utc_date_minus_days(1)
            # if Path(host_list_sqlite_file).exists():
            #     (min_date, max_date) = etld_lib_sqlite_tables.get_q_table_min_max_dates(
            #         host_list_sqlite_file, "LAST_VULN_SCAN_DATETIME", "Q_Host_List")
            #     if str(max_date).startswith("20"):
            #         max_date = re.sub(":..$", ":00", max_date)
            #         max_date = re.sub(" ", "T", max_date)
            #         max_date = re.sub("$", "Z", max_date)
            #         host_list_detection_vm_processed_after = max_date
            #         host_list_vm_processed_after = max_date
            #         etld_lib_functions.logger.info(f"Found Q_Host_List Min Date: {min_date} Max Date: {max_date}")
            #         etld_lib_functions.logger.info(f"host_list_detection_vm_processed_after and "
            #                                        f"host_list_vm_processed_after using "
            #                                        f"max_date from Q_Host_List database")
            #     else:
            #         host_list_detection_vm_processed_after = etld_lib_datetime.get_utc_date_minus_days(1)
            #         host_list_vm_processed_after = host_list_detection_vm_processed_after
            #         etld_lib_functions.logger.info(f"{host_list_sqlite_file} did not have a valid max date. "
            #                                        f"host_list_detection_vm_processed_after and "
            #                                        f"host_list_vm_processed_after "
            #                                        f"set using utc.now minus 1 days")

        if not etld_lib_datetime.is_valid_qualys_datetime_format(host_list_detection_vm_processed_after):
            etld_lib_functions.logger.error(f"Format Error host_list_detection_vm_processed_after: "
                                            f"{host_list_detection_vm_processed_after} ")
            exit(1)

        etld_lib_functions.logger.info(f"host_list_vm_processed_after: {host_list_detection_vm_processed_after}")
        etld_lib_functions.logger.info(
            f"host_list_detection_vm_processed_after: {host_list_detection_vm_processed_after}")

        if str(host_list_detection_vm_processed_after).__contains__("1970"):  # Don't add date to process all data.
            return {}
        else:
            return {'vm_processed_after': host_list_detection_vm_processed_after}

    def set_host_detection_list_api_payload():
        global host_list_detection_api_payload
        global host_list_detection_payload_option
        global host_list_detection_multi_proc_batch_size
        global host_list_detection_limit_hosts

        host_list_detection_payload_default = \
            {'action': 'list', 'show_asset_id': '1', 'show_reopened_info': '1', 'show_tags': '0', 'show_results': '1',
             'show_igs': '1', 'status': 'Active,New,Re-Opened,Fixed', 'arf_kernel_filter': '1',
             'arf_service_filter': '0', 'arf_config_filter': '0', 'include_ignored': '1', 'include_disabled': '1',
             'truncation_limit': '0'}

        host_list_detection_payload_option = get_attribute_from_config_settings('host_list_detection_payload_option',
                                                                                'default')
        host_list_detection_api_payload = set_api_payload(host_list_detection_payload_default,
                                                          'host_list_detection_payload_option')
        host_list_detection_discarded_vm_processed_after_date = set_host_list_detection_vm_processed_after()

        host_list_detection_multi_proc_batch_size = \
            get_attribute_from_config_settings('host_list_detection_multi_proc_batch_size', '1000')

        if int(host_list_detection_multi_proc_batch_size) > 2000:
            etld_lib_functions.logger.info(f"reset batch_size_max to 2000.")
            etld_lib_functions.logger.info(
                f" user select batch_size_max was {host_list_detection_multi_proc_batch_size}.")
            host_list_detection_multi_proc_batch_size = 2000
        elif int(host_list_detection_multi_proc_batch_size) > 100:
            etld_lib_functions.logger.info(f"reset batch_size_max to {host_list_detection_multi_proc_batch_size}.")
            etld_lib_functions.logger.info(
                f" user select batch_size_max is {host_list_detection_multi_proc_batch_size}.")
            host_list_detection_multi_proc_batch_size = int(host_list_detection_multi_proc_batch_size)
        else:
            etld_lib_functions.logger.info(f"reset batch_size_max to 100.")
            etld_lib_functions.logger.info(f" user select batch_size_max is "
                                           f"{host_list_detection_multi_proc_batch_size},"
                                           f"but is not within range. 100 - 2000.  Reset to 100")
            host_list_detection_multi_proc_batch_size = 100

        host_list_detection_limit_hosts = \
            get_attribute_from_config_settings('host_list_detection_limit_hosts', '0')

    host_list_detection_data_dir = qetl_user_data_dir
    host_list_detection_export_dir = \
        get_attribute_from_config_settings('host_list_detection_export_dir', 'default')
    host_list_detection_distribution_csv_flag = get_attribute_from_config_settings('host_list_detection_distribution_csv_flag', False)
    host_list_detection_distribution_csv_max_field_size = \
        get_attribute_from_config_settings('host_list_detection_distribution_csv_max_field_size', default_distribution_csv_max_field_size)
    host_list_detection_csv_truncate_cell_limit = '0'
    # get_attribute_from_config_settings('host_list_detection_csv_truncate_cell_limit', '0')

    host_list_detection_payload_option = get_attribute_from_config_settings('host_list_detection_payload_option', '')
    host_list_detection_concurrency_limit = \
        get_attribute_from_config_settings('host_list_detection_concurrency_limit', '2')
    host_list_detection_present_csv_cell_as_json = \
        get_attribute_from_config_settings('host_list_detection_present_csv_cell_as_json', True)
    host_list_detection_xml_to_sqlite_via_multiprocessing = \
        get_attribute_from_config_settings('host_list_xml_to_sqlite_via_multiprocessing', True)
    host_list_detection_payload_option = \
        get_attribute_from_config_settings('host_list_detection_payload_option', 'notags')
    host_list_detection_chunk_size_calc = \
        int(get_attribute_from_config_settings('host_list_detection_chunk_size_calc', '20480'))
    host_list_detection_try_extract_max_count = \
        int(get_attribute_from_config_settings('host_list_detection_try_extract_max_count', '30'))
    host_list_detection_http_conn_timeout = \
        int(get_attribute_from_config_settings('host_list_detection_http_conn_timeout', '900'))
    host_list_detection_open_file_compression_method = \
        get_open_file_compression_method_from_config_settings('host_list_detection_open_file_compression_method')

    set_host_detection_list_api_payload()

    etld_lib_functions.logger.info(f"host list detection config - {qetl_user_config_settings_yaml_file}")
    etld_lib_functions.logger.info(f"host_list_detection_export_dir - {host_list_detection_export_dir}")
    etld_lib_functions.logger.info(f"host_list_detection_concurrency_limit - {host_list_detection_concurrency_limit}")
    etld_lib_functions.logger.info(f"host_list_detection_multi_proc_batch_size - "
                                   f"{host_list_detection_multi_proc_batch_size}")
    etld_lib_functions.logger.info(f"host_list_api_payload - {host_list_api_payload}")
    etld_lib_functions.logger.info(f"host_list_detection_api_payload - {host_list_detection_api_payload}")


def setup_host_list_detection_vars():
    global qetl_user_data_dir
    global host_list_detection_data_dir
    global host_list_detection_xml_file
    global host_list_detection_extract_dir
    global host_list_detection_extract_dir_file_search_blob
    global host_list_detection_distribution_dir
    global host_list_detection_distribution_dir_file_search_blob
    global host_list_detection_shelve_file
    global host_list_detection_sqlite_file
    global host_list_detection_csv_file
    global host_list_detection_csv_truncate_cell_limit
    global host_list_detection_json_file
    global host_list_detection_log_file
    global host_list_detection_lock_file
    global host_list_detection_log_rotate_file
    global host_list_detection_table_view_name
    global host_list_detection_status_table_name
    global host_list_detection_hosts_table_name
    global host_list_detection_q_knowledgebase_in_host_list_detection
    global host_list_detection_qids_table_name
    global host_list_detection_data_files

    host_list_detection_data_dir = Path(qetl_user_data_dir)
    host_list_detection_extract_dir = Path(host_list_detection_data_dir, "host_list_detection_extract_dir")
    host_list_detection_extract_dir_file_search_blob = "host_list_detection_utc*"
    host_list_detection_distribution_dir = Path(host_list_detection_data_dir, "host_list_detection_distribution_dir")
    host_list_detection_distribution_dir_file_search_blob = "Q_*"
    host_list_detection_shelve_file = Path(host_list_detection_data_dir, "host_list_detection_shelve")
    host_list_detection_sqlite_file = Path(host_list_detection_data_dir, "host_list_detection_sqlite.db")
    host_list_detection_csv_file = Path(host_list_detection_data_dir, "host_list_detection.csv")
    host_list_detection_json_file = Path(host_list_detection_data_dir, "host_list_detection.json")
    host_list_detection_log_file = Path(qetl_user_log_dir, "host_list_detection.log")
    host_list_detection_lock_file = Path(qetl_user_log_dir, ".host_list_detection.lock")
    host_list_detection_log_rotate_file = Path(qetl_user_log_dir, "host_list_detection.1.log")
    host_list_detection_table_view_name = 'Q_Host_List_Detection'
    host_list_detection_status_table_name = 'Q_Host_List_Detection_Status'
    host_list_detection_hosts_table_name = 'Q_Host_List_Detection_HOSTS'
    host_list_detection_qids_table_name = 'Q_Host_List_Detection_QIDS'
    host_list_detection_q_knowledgebase_in_host_list_detection = 'Q_KnowledgeBase_In_Host_List_Detection'
    host_list_detection_data_files = [host_list_detection_shelve_file, host_list_detection_sqlite_file,
                                      host_list_detection_csv_file, host_list_detection_json_file]


def get_asset_inventory_user_config():
    global asset_inventory_data_dir
    global asset_inventory_export_dir
    global asset_inventory_distribution_csv_flag
    global asset_inventory_distribution_csv_max_field_size
    global default_distribution_csv_max_field_size
    global asset_inventory_asset_last_updated
    global asset_inventory_payload_option
    global asset_inventory_concurrency_limit
    global asset_inventory_multi_proc_batch_size
    global asset_inventory_limit_hosts
    global asset_inventory_present_csv_cell_as_json
    global asset_inventory_csv_truncate_cell_limit
    global qetl_user_config_settings_yaml_file
    global qetl_manage_user_selected_datetime
    global asset_inventory_json_to_sqlite_via_multiprocessing
    global asset_inventory_chunk_size_calc
    global asset_inventory_try_extract_max_count
    global asset_inventory_http_conn_timeout
    global asset_inventory_open_file_compression_method
    global asset_inventory_test_system_flag
    global asset_inventory_test_number_of_files_to_extract
    global asset_inventory_last_seen_asset_id_for_restart

    def set_asset_inventory_last_updated():
        global asset_inventory_asset_last_updated
        if qetl_manage_user_selected_datetime is not None:
            asset_inventory_asset_last_updated = qetl_manage_user_selected_datetime
            etld_lib_functions.logger.info(f"asset_inventory_asset_last_updated set by qetl_manage_user -d option")
        elif asset_inventory_asset_last_updated == 'default':
            asset_inventory_asset_last_updated = etld_lib_datetime.get_utc_date_minus_days(1)
            etld_lib_functions.logger.info(f"asset_inventory_asset_last_updated default set to utc.now minus 1 days")

        etld_lib_functions.logger.info(f"asset_inventory_asset_last_updated - "
                                       f"{asset_inventory_asset_last_updated}")

    asset_inventory_data_dir = qetl_user_data_dir
    asset_inventory_export_dir = \
        get_attribute_from_config_settings('asset_inventory_export_dir', 'default')
    asset_inventory_distribution_csv_flag = get_attribute_from_config_settings('asset_inventory_distribution_csv_flag', False)
    asset_inventory_distribution_csv_max_field_size = \
        get_attribute_from_config_settings('asset_inventory_distribution_csv_max_field_size', default_distribution_csv_max_field_size)
    asset_inventory_csv_truncate_cell_limit = '0'
    # get_attribute_from_config_settings('asset_inventory_csv_truncate_cell_limit', '0')
    asset_inventory_asset_last_updated = \
        get_attribute_from_config_settings('asset_inventory_asset_last_updated', 'default')
    asset_inventory_payload_option = get_attribute_from_config_settings('asset_inventory_payload_option', '')
    asset_inventory_concurrency_limit = get_attribute_from_config_settings('asset_inventory_concurrency_limit', '2')
    asset_inventory_multi_proc_batch_size = \
        get_attribute_from_config_settings('asset_inventory_multi_proc_batch_size', '300')
    asset_inventory_limit_hosts = \
        get_attribute_from_config_settings('asset_inventory_limit_hosts', '300')
    asset_inventory_json_to_sqlite_via_multiprocessing = \
        get_attribute_from_config_settings('asset_inventory_json_to_sqlite_via_multiprocessing', True)
    asset_inventory_present_csv_cell_as_json = \
        get_attribute_from_config_settings('asset_inventory_present_csv_cell_as_json', True)
    asset_inventory_chunk_size_calc = \
        int(get_attribute_from_config_settings('asset_inventory_chunk_size_calc', '20480'))
    asset_inventory_try_extract_max_count = \
        int(get_attribute_from_config_settings('asset_inventory_try_extract_max_count', '30'))
    asset_inventory_http_conn_timeout = \
        int(get_attribute_from_config_settings('asset_inventory_http_conn_timeout', '900'))
    asset_inventory_open_file_compression_method = \
        get_open_file_compression_method_from_config_settings('asset_inventory_open_file_compression_method')
    asset_inventory_test_system_flag = get_attribute_from_config_settings('asset_inventory_test_system_flag', False)
    asset_inventory_test_number_of_files_to_extract = \
        get_attribute_from_config_settings('asset_inventory_test_number_of_files_to_extract', 3)
    asset_inventory_last_seen_asset_id_for_restart = \
        get_attribute_from_config_settings('asset_inventory_last_seen_asset_id_for_restart', 0)
    set_asset_inventory_last_updated()

    etld_lib_functions.logger.info(f"asset inventory config - {qetl_user_config_settings_yaml_file}")
    etld_lib_functions.logger.info(f"asset_inventory_export_dir yaml - {asset_inventory_export_dir}")
    etld_lib_functions.logger.info(f"asset_inventory_extract_dir yaml - {asset_inventory_extract_dir}")
    etld_lib_functions.logger.info(f"asset_inventory_concurrency_limit yaml - {asset_inventory_concurrency_limit}")
    etld_lib_functions.logger.info(
        f"asset_inventory_multi_proc_batch_size yaml - {asset_inventory_multi_proc_batch_size}")
    etld_lib_functions.logger.info(
        f"asset_inventory_csv_truncate_cell_limit set to zero by program.")


def setup_asset_inventory_vars():
    global qetl_user_data_dir
    global asset_inventory_data_dir
    global asset_inventory_json_batch_file
    global asset_inventory_extract_dir
    global asset_inventory_extract_dir_file_search_blob
    global asset_inventory_extract_dir_file_search_blob_two
    global asset_inventory_distribution_dir
    global asset_inventory_distribution_dir_file_search_blob
    global asset_inventory_shelve_file
    global asset_inventory_shelve_software_assetid_file
    global asset_inventory_shelve_software_unique_file
    global asset_inventory_shelve_software_os_unique_file
    global asset_inventory_sqlite_file
    global asset_inventory_csv_file
    global asset_inventory_csv_software_assetid_file
    global asset_inventory_csv_software_unique_file
    global asset_inventory_csv_software_os_unique_file
    global asset_inventory_csv_truncate_cell_limit
    global asset_inventory_json_file
    global asset_inventory_log_file
    global asset_inventory_lock_file
    global asset_inventory_log_rotate_file
    global asset_inventory_table_name
    global asset_inventory_status_table_name
    global asset_inventory_table_name_software_assetid
    global asset_inventory_table_name_software_unique
    global asset_inventory_table_name_software_os_unique
    global asset_inventory_data_files
    global asset_inventory_temp_shelve_file

    asset_inventory_data_dir = Path(qetl_user_data_dir)
    asset_inventory_extract_dir = Path(asset_inventory_data_dir, "asset_inventory_extract_dir")
    asset_inventory_extract_dir_file_search_blob = "asset_inventory_utc*"
    asset_inventory_extract_dir_file_search_blob_two = "asset_inventory_count_utc*"
    asset_inventory_distribution_dir = Path(asset_inventory_data_dir, "asset_inventory_distribution_dir")
    asset_inventory_distribution_dir_file_search_blob = "Q_*"
    asset_inventory_temp_shelve_file = Path(asset_inventory_extract_dir, "asset_inventory_temp_shelve.db")
    asset_inventory_shelve_file = Path(asset_inventory_data_dir, "asset_inventory_shelve")
    asset_inventory_shelve_software_assetid_file = \
        Path(asset_inventory_data_dir, "asset_inventory_shelve_software_assetid")

    asset_inventory_shelve_software_unique_file = \
        Path(asset_inventory_data_dir, "asset_inventory_shelve_software_unique")
    asset_inventory_shelve_software_os_unique_file = \
        Path(asset_inventory_data_dir, "asset_inventory_shelve_software_os_unique")

    asset_inventory_sqlite_file = Path(asset_inventory_data_dir, "asset_inventory_sqlite.db")
    asset_inventory_csv_file = Path(asset_inventory_data_dir, "asset_inventory.csv")
    asset_inventory_csv_software_assetid_file = Path(asset_inventory_data_dir, "asset_inventory_software_assetid.csv")
    asset_inventory_csv_software_unique_file = Path(asset_inventory_data_dir, "asset_inventory_software_unique.csv")
    asset_inventory_csv_software_os_unique_file = \
        Path(asset_inventory_data_dir, "asset_inventory_software_os_unique.csv")
    asset_inventory_json_file = Path(asset_inventory_data_dir, "asset_inventory.json")
    asset_inventory_log_file = Path(qetl_user_log_dir, "asset_inventory.log")
    asset_inventory_lock_file = Path(qetl_user_log_dir, ".asset_inventory.lock")
    asset_inventory_log_rotate_file = Path(qetl_user_log_dir, "asset_inventory.1.log")
    asset_inventory_table_name = 'Q_Asset_Inventory'
    asset_inventory_status_table_name = 'Q_Asset_Inventory_Status'
    asset_inventory_table_name_software_assetid = 'Q_Asset_Inventory_Software_AssetId'
    asset_inventory_table_name_software_unique = 'Q_Asset_Inventory_Software_Unique'
    asset_inventory_table_name_software_os_unique = 'Q_Asset_Inventory_Software_OS_Unique'
    asset_inventory_data_files = [asset_inventory_shelve_file, asset_inventory_sqlite_file,
                                  asset_inventory_csv_file, asset_inventory_csv_software_unique_file,
                                  asset_inventory_csv_software_assetid_file, asset_inventory_json_file,
                                  asset_inventory_shelve_software_assetid_file,
                                  asset_inventory_shelve_software_unique_file,
                                  asset_inventory_shelve_software_os_unique_file]


def get_was_user_config():
    global was_data_dir
    global was_export_dir
    global was_distribution_csv_flag
    global was_distribution_csv_max_field_size
    global default_distribution_csv_max_field_size
    global was_webapp_last_scan_date
    global was_payload_option
    global was_concurrency_limit
    global was_multi_proc_batch_size
    global was_limit_hosts
    global qetl_user_config_settings_yaml_file
    global qetl_manage_user_selected_datetime
    global was_json_to_sqlite_via_multiprocessing
    global was_chunk_size_calc
    global was_try_extract_max_count
    global was_http_conn_timeout
    global was_open_file_compression_method
    global was_test_system_flag
    global was_test_number_of_files_to_extract
    global was_catalog_start_greater_than_last_id

    def set_was_webapp_last_scan_date():
        global was_webapp_last_scan_date
        if qetl_manage_user_selected_datetime is not None:
            was_webapp_last_scan_date = qetl_manage_user_selected_datetime
            if was_webapp_last_scan_date.startswith("20"):
                etld_lib_functions.logger.info(f"was_webapp_last_scan_date set by qetl_manage_user -d option")
            else:
                was_webapp_last_scan_date = "2000-01-01T00:00:00Z"
                etld_lib_functions.logger.info(f"was_webapp_last_scan_date reset to 2000-01-01T00:00:00Z.  reset from qetl_manage_user -d option")
        elif was_webapp_last_scan_date == 'default':
            was_webapp_last_scan_date = etld_lib_datetime.get_utc_date_minus_days(365)
            etld_lib_functions.logger.info(f"was_webapp_last_scan_date default set to utc.now minus 365 days")

        etld_lib_functions.logger.info(f"was_webapp_last_scan_date - "
                                       f"{was_webapp_last_scan_date}")

    was_data_dir = qetl_user_data_dir
    was_export_dir = \
        get_attribute_from_config_settings('was_export_dir', 'default')
    was_distribution_csv_flag = get_attribute_from_config_settings('was_distribution_csv_flag', False)
    was_distribution_csv_max_field_size = \
        get_attribute_from_config_settings('was_distribution_csv_max_field_size', default_distribution_csv_max_field_size)
    was_webapp_last_scan_date = \
        get_attribute_from_config_settings('was_webapp_last_scan_date', 'default')
    was_payload_option = get_attribute_from_config_settings('was_payload_option', '')
    was_multi_proc_batch_size = \
        get_attribute_from_config_settings('was_multi_proc_batch_size', '300')
    was_limit_hosts = \
        get_attribute_from_config_settings('was_limit_hosts', '300')
    was_json_to_sqlite_via_multiprocessing = \
        get_attribute_from_config_settings('was_json_to_sqlite_via_multiprocessing', True)
    was_chunk_size_calc = \
        int(get_attribute_from_config_settings('was_chunk_size_calc', '20480'))
    was_try_extract_max_count = \
        int(get_attribute_from_config_settings('was_try_extract_max_count', '30'))
    was_http_conn_timeout = \
        int(get_attribute_from_config_settings('was_http_conn_timeout', '900'))
    was_open_file_compression_method = \
        get_open_file_compression_method_from_config_settings('was_open_file_compression_method')
    was_test_system_flag = get_attribute_from_config_settings('was_test_system_flag', False)
    was_test_number_of_files_to_extract = \
        get_attribute_from_config_settings('was_test_number_of_files_to_extract', 3)
    was_catalog_start_greater_than_last_id = \
        get_attribute_from_config_settings('was_catalog_start_greater_than_last_id', 0)
    set_was_webapp_last_scan_date()

    etld_lib_functions.logger.info(f"was_export_dir - {was_export_dir}")
    etld_lib_functions.logger.info(f"was_extract_dir - {was_extract_dir}")


def setup_was_vars():
    global qetl_user_data_dir
    global was_data_dir
    global was_extract_dir
    global was_extract_dir_file_search_blob
    global was_extract_dir_file_search_blob_webapp
    global was_extract_dir_file_search_blob_webapp_detail
    global was_extract_dir_file_search_blob_finding
    global was_extract_dir_file_search_blob_finding_detail
    global was_extract_dir_file_search_blob_catalog
    global was_extract_dir_file_search_blob_webapp_count
    global was_extract_dir_file_search_blob_finding_count
    global was_extract_dir_file_search_blob_catalog_count
    global was_distribution_dir
    global was_distribution_dir_file_search_blob
    global was_sqlite_file
    global was_log_file
    global was_lock_file
    global was_log_rotate_file
    global was_status_table_name
    global was_webapp_table_name
    global was_catalog_table_name
    global was_finding_table_name
    global was_q_knowledgebase_in_was_finding_table
    global was_data_files

    was_data_dir = Path(qetl_user_data_dir)
    was_extract_dir = Path(was_data_dir, "was_extract_dir")
    was_extract_dir_file_search_blob = "was_*_utc_*"
    was_extract_dir_file_search_blob_webapp = "was_webapp_utc_*"
    was_extract_dir_file_search_blob_webapp_detail = "was_webapp_detail_utc_*"
    was_extract_dir_file_search_blob_finding = "was_finding_utc_*"
    was_extract_dir_file_search_blob_finding_detail = "was_finding_detail_utc_*"
    was_extract_dir_file_search_blob_catalog = "was_catalog_utc_*"
    was_extract_dir_file_search_blob_webapp_count = "was_count_webapp_utc_*"
    was_extract_dir_file_search_blob_finding_count = "was_count_finding_utc_*"
    was_extract_dir_file_search_blob_catalog_count = "was_count_catalog_utc_*"
    was_distribution_dir = Path(was_data_dir, "was_distribution_dir")
    was_distribution_dir_file_search_blob = "Q_*"
    was_sqlite_file = Path(was_data_dir, "was_sqlite.db")
    was_log_file = Path(qetl_user_log_dir, "was.log")
    was_lock_file = Path(qetl_user_log_dir, ".was.lock")
    was_log_rotate_file = Path(qetl_user_log_dir, "was.1.log")
    was_q_knowledgebase_in_was_finding_table = 'Q_KnowledgeBase_In_Q_WAS_FINDING'
    was_webapp_table_name = 'Q_WAS_WebApp'
    was_catalog_table_name = 'Q_WAS_Catalog'
    was_finding_table_name = 'Q_WAS_Finding'

    was_status_table_name = 'Q_WAS_Status'
    was_data_files = [was_sqlite_file]


def setup_completed():
    global setup_completed_flag
    setup_completed_flag = True


def get_qetl_code_dir():
    global qetl_code_dir         # Parent of qualys_etl directory
    global qetl_code_dir_child   # qualys_etl directory
    qetl_code_dir = etld_lib_functions.qetl_code_dir
    qetl_code_dir_child = etld_lib_functions.qetl_code_dir_child


def set_qetl_code_dir_etld_cred_yaml_template_path():
    global qetl_code_dir_etld_cred_yaml_template_path
    qetl_code_dir_etld_cred_yaml_template_path = \
        Path(etld_lib_functions.qetl_code_dir, "qualys_etl", "etld_templates", ".etld_cred.yaml")


def setup_requests_module_tls_verify_status():
    global requests_module_tls_verify_status
    if 'requests_module_tls_verify_status' in etld_lib_config_settings_yaml_dict:
        requests_module_tls_verify_status = etld_lib_config_settings_yaml_dict.get('requests_module_tls_verify_status')
    else:
        requests_module_tls_verify_status = True

    if requests_module_tls_verify_status is True or requests_module_tls_verify_status is False:
        pass
    else:
        requests_module_tls_verify_status = True
        etld_lib_functions.logger.warn(f"requests_module_tls_verify_status defaulting to True")

    if requests_module_tls_verify_status is False:
        etld_lib_functions.logger.warn(f"requests_module_tls_verify_status in etld_config.yaml is set "
                                       f"to: {requests_module_tls_verify_status} "
                                       f"You have selected to not verify tls certificates, subjecting your application "
                                       f"to man in the middle attacks.  Please repair your certificate issue and "
                                       f"reset requests_module_tls_verify_status in etld_config.yaml to True. ")


def run_log_csv_columns():
    csv_columns = ['LOG_DATETIME', 'LOG_LEVEL', 'LOG_WORKFLOW', 'LOG_USERNAME',
                   'LOG_FUNCTION', 'LOG_MESSAGE']
    return csv_columns


def run_log_csv_column_types():
    csv_columns = {
    }
    return csv_columns


def kb_csv_columns():
    csv_columns = ['QID', 'TITLE', 'VULN_TYPE', 'SEVERITY_LEVEL', 'CATEGORY', 'LAST_SERVICE_MODIFICATION_DATETIME',
                   'PUBLISHED_DATETIME', 'PATCHABLE', 'DIAGNOSIS', 'CONSEQUENCE', 'SOLUTION', 'PCI_FLAG',
                   'SUPPORTED_MODULES', 'IS_DISABLED',
                   'CVE_LIST', 'THREAT_INTELLIGENCE', 'CORRELATION', 'BUGTRAQ_LIST', 'SOFTWARE_LIST',
                   'VENDOR_REFERENCE_LIST', 'CVSS', 'CVSS_V3', 'CHANGE_LOG_LIST', 'DISCOVERY', 'PCI_REASONS',
                   'BATCH_DATE', 'BATCH_NUMBER', 'Row_Last_Updated'
                   ]

    return csv_columns


def kb_csv_column_types():

    csv_columns = {
        'QID': 'INTEGER'
    }
    return csv_columns


def host_list_csv_columns():  # Return list of csv columns
    # QWEB < 10.23 release
    # csv_columns = [
    #     'ID', 'ASSET_ID', 'IP', 'IPV6', 'TRACKING_METHOD', 'NETWORK_ID', 'DNS', 'DNS_DATA', 'CLOUD_PROVIDER',
    #     'CLOUD_SERVICE', 'CLOUD_RESOURCE_ID', 'EC2_INSTANCE_ID', 'NETBIOS', 'OS', 'QG_HOSTID', 'TAGS', 'METADATA',
    #     'CLOUD_PROVIDER_TAGS', 'LAST_VULN_SCAN_DATETIME', 'LAST_VM_SCANNED_DATE', 'LAST_VM_SCANNED_DURATION',
    #     'LAST_VM_AUTH_SCANNED_DATE', 'LAST_VM_AUTH_SCANNED_DURATION', 'LAST_COMPLIANCE_SCAN_DATETIME', 'OWNER',
    #     'COMMENTS', 'USER_DEF', 'ASSET_GROUP_IDS', 'ASSET_RISK_SCORE', 'ASSET_CRITICALITY_SCORE', 'ARS_FACTORS',
    #     'BATCH_DATE', 'BATCH_NUMBER', 'Row_Last_Updated'
    # ]

    # QWEB >= 10.23 release
    csv_columns = [
        'ID', 'ASSET_ID', 'IP', 'IPV6', 'TRACKING_METHOD', 'NETWORK_ID', 'DNS', 'DNS_DATA', 'CLOUD_PROVIDER',
        'CLOUD_SERVICE', 'CLOUD_RESOURCE_ID', 'EC2_INSTANCE_ID', 'NETBIOS', 'OS', 'QG_HOSTID', 'TAGS', 'METADATA',
        'CLOUD_PROVIDER_TAGS', 'LAST_VULN_SCAN_DATETIME', 'LAST_VM_SCANNED_DATE', 'LAST_VM_SCANNED_DURATION',
        'LAST_VM_AUTH_SCANNED_DATE', 'LAST_VM_AUTH_SCANNED_DURATION', 'LAST_COMPLIANCE_SCAN_DATETIME', 'OWNER',
        'COMMENTS', 'USER_DEF', 'ASSET_GROUP_IDS', 'ASSET_RISK_SCORE', 'TRURISK_SCORE', 'ASSET_CRITICALITY_SCORE', 'ARS_FACTORS', 'TRURISK_SCORE_FACTORS',
        'LAST_SCAP_SCAN_DATETIME', 'LAST_BOOT', 'SERIAL_NUMBER', 'HARDWARE_UUID', 'FIRST_FOUND_DATE', 'LAST_ACTIVITY', 'AGENT_STATUS', 'CLOUD_AGENT_RUNNING_ON',
        'BATCH_DATE', 'BATCH_NUMBER', 'Row_Last_Updated'
    ]


    return csv_columns


def host_list_csv_column_types():

    csv_columns = {
        'ID': 'INTEGER', 'ASSET_ID': 'INTEGER'
    }
    return csv_columns


def host_list_detection_host_csv_columns():  # Return list of csv columns
   # < !ELEMENT
   # HOST_LIST(HOST +) > <!ELEMENT
   # HOST(
   # ID, ASSET_ID?, IP?, IPV6?, TRACKING_METHOD?, NETWORK_ID?, OS?, OS_CPE?, DNS?, DNS_DATA?, CLOUD_PROVIDER?,
   # CLOUD_SERVICE?, CLOUD_RESOURCE_ID?, EC2_INSTANCE_ID?, NETBIOS?, QG_HOSTID?,
   # LAST_SCAN_DATETIME?, LAST_VM_SCANNED_DATE?, LAST_VM_SCANNED_DURATION?, LAST_VM_AUTH_SCANNED_DATE?,
   # LAST_VM_AUTH_SCANNED_DURATION?, LAST_PC_SCANNED_DATE?,
   # TAGS?, METADATA?, CLOUD_PROVIDER_TAGS?, DETECTION_LIST) >

   # csv_columns = [
   #     'ID', 'ASSET_ID', 'IP', 'IPV6', 'TRACKING_METHOD', 'NETWORK_ID', 'OS', 'OS_CPE', 'DNS', 'DNS_DATA',
   #     'CLOUD_PROVIDER', 'CLOUD_SERVICE', 'CLOUD_RESOURCE_ID', 'EC2_INSTANCE_ID', 'NETBIOS', 'QG_HOSTID',
   #     'LAST_SCAN_DATETIME', 'LAST_VM_SCANNED_DATE', 'LAST_VM_SCANNED_DURATION',
   #     'LAST_VM_AUTH_SCANNED_DATE', 'LAST_VM_AUTH_SCANNED_DURATION', 'LAST_PC_SCANNED_DATE',
   #     'TAGS', 'METADATA', 'CLOUD_PROVIDER_TAGS', 'BATCH_DATE', 'BATCH_NUMBER'
   # ]

    # QWEB < 10.23
    # csv_columns = [
    #                'ID', 'ASSET_ID', 'IP', 'IPV6', 'TRACKING_METHOD', 'NETWORK_ID', 'OS', 'OS_CPE', 'DNS', 'DNS_DATA',
    #                'NETBIOS', 'QG_HOSTID',
    #                'LAST_SCAN_DATETIME', 'LAST_VM_SCANNED_DATE', 'LAST_VM_SCANNED_DURATION',
    #                'LAST_VM_AUTH_SCANNED_DATE', 'LAST_VM_AUTH_SCANNED_DURATION', 'LAST_PC_SCANNED_DATE',
    #                'BATCH_DATE', 'BATCH_NUMBER', 'Row_Last_Updated'
    #                ]

    # QWEB >= 10.23
    csv_columns = ['ID', 'ASSET_ID', 'IP', 'IPV6', 'TRACKING_METHOD', 'NETWORK_ID', 'OS', 'OS_CPE', 'DNS', 'DNS_DATA',
                   'CLOUD_PROVIDER', 'CLOUD_SERVICE', 'CLOUD_RESOURCE_ID', 'EC2_INSTANCE_ID', 'NETBIOS', 'QG_HOSTID',
                   'LAST_SCAN_DATETIME', 'LAST_VM_SCANNED_DATE', 'LAST_VM_SCANNED_DURATION',
                   'LAST_VM_AUTH_SCANNED_DATE', 'LAST_VM_AUTH_SCANNED_DURATION', 'LAST_PC_SCANNED_DATE',
                   'TAGS', 'METADATA', 'CLOUD_PROVIDER_TAGS',
                   'BATCH_DATE', 'BATCH_NUMBER', 'Row_Last_Updated'
                   ]
    return csv_columns


def host_list_detection_host_csv_column_types():  # Return list of csv columns
    csv_columns = {
        'ID': 'INTEGER', 'ASSET_ID': 'INTEGER'
    }
    return csv_columns


def host_list_detection_qids_csv_columns():  # Return list of csv columns
    # < !ELEMENT
    # DETECTION_LIST(DETECTION +) > <!ELEMENT
    # DETECTION(
    # QID, TYPE, SEVERITY?, PORT?, PROTOCOL?, FQDN?, SSL?, INSTANCE?, RESULTS?, STATUS?,
    # FIRST_FOUND_DATETIME?, LAST_FOUND_DATETIME?, TIMES_FOUND?, LAST_TEST_DATETIME?, LAST_UPDATE_DATETIME?,
    # LAST_FIXED_DATETIME?, FIRST_REOPENED_DATETIME?, LAST_REOPENED_DATETIME?, TIMES_REOPENED?, SERVICE?,
    # IS_IGNORED?, IS_DISABLED?, AFFECT_RUNNING_KERNEL?, AFFECT_RUNNING_SERVICE?, AFFECT_EXPLOITABLE_CONFIG?,
    # LAST_PROCESSED_DATETIME?

    # QWEB < 10.23
    # csv_columns = [
    #                'ID', 'ASSET_ID', 'QID', 'TYPE', 'STATUS', 'PORT', 'PROTOCOL', 'SEVERITY', 'FQDN', 'SSL', 'INSTANCE',
    #                'LAST_PROCESSED_DATETIME', 'FIRST_FOUND_DATETIME', 'LAST_FOUND_DATETIME', 'TIMES_FOUND',
    #                'LAST_TEST_DATETIME', 'LAST_UPDATE_DATETIME', 'LAST_FIXED_DATETIME', 'FIRST_REOPENED_DATETIME',
    #                'LAST_REOPENED_DATETIME', 'TIMES_REOPENED', 'SERVICE', 'IS_IGNORED', 'IS_DISABLED',
    #                'AFFECT_RUNNING_KERNEL', 'AFFECT_RUNNING_SERVICE', 'AFFECT_EXPLOITABLE_CONFIG',
    #                'QDS', 'QDS_FACTORS', 'RESULTS',
    #                'BATCH_DATE', 'BATCH_NUMBER', 'Row_Last_Updated'
    #               ]

    # QWEB >= 10.23
    csv_columns = [
        'ID', 'ASSET_ID', 'UNIQUE_VULN_ID', 'QID', 'TYPE', 'SEVERITY', 'PORT', 'PROTOCOL', 'FQDN', 'SSL', 'INSTANCE',
        'STATUS', 'FIRST_FOUND_DATETIME', 'LAST_FOUND_DATETIME', 'QDS', 'QDS_FACTORS', 'TIMES_FOUND',
        'LAST_TEST_DATETIME', 'LAST_UPDATE_DATETIME', 'LAST_FIXED_DATETIME', 'FIRST_REOPENED_DATETIME',
        'LAST_REOPENED_DATETIME', 'TIMES_REOPENED', 'SERVICE', 'IS_IGNORED', 'IS_DISABLED',
        'AFFECT_RUNNING_KERNEL', 'AFFECT_RUNNING_SERVICE', 'AFFECT_EXPLOITABLE_CONFIG',
        'LAST_PROCESSED_DATETIME', 'ASSET_CVE', 'RESULTS',
        'BATCH_DATE', 'BATCH_NUMBER', 'Row_Last_Updated'
    ]
    return csv_columns


def host_list_detection_qids_csv_column_types():  # Return list of csv columns
    csv_columns = {
        'ID': 'INTEGER', 'ASSET_ID': 'INTEGER', 'QID': 'INTEGER', 'UNIQUE_VULN_ID': 'INTEGER',
        'TIMES_REOPENED': 'INTEGER', 'TIMES_FOUND': 'INTEGER'
    }
    return csv_columns


def asset_inventory_csv_columns():  # Return list of csv columns updated 0.6.111
    # Added 2022-12-16 - "sensor_lastPcScanDateAgent", "sensor_lastPcScanDateScanner"
    # Added 2022-12-16 - "sensor_lastVmScanDateAgent", "sensor_lastVmScanDateScanner"

    csv_columns = [
        'assetId', 'assetUUID', 'hostId', 'lastModifiedDate', 'agentId', 'createdDate', 'sensorLastUpdatedDate',
        'sensor_lastVMScanDate', 'sensor_lastComplianceScanDate', 'sensor_lastFullScanDate',
        'sensor_lastPcScanDateAgent', 'sensor_lastPcScanDateScanner',
        'sensor_lastVmScanDateAgent', 'sensor_lastVmScanDateScanner',
        'inventory_createdDate',
        'inventory_lastUpdatedDate', 'agent_lastActivityDate', 'agent_lastCheckedInDate', 'agent_lastInventoryDate',
        'assetType', 'address', 'dnsName', 'assetName', 'netbiosName', 'timeZone', 'biosDescription', 'lastBoot',
        'totalMemory', 'cpuCount', 'lastLoggedOnUser', 'domainRole', 'hwUUID', 'biosSerialNumber', 'biosAssetTag',
        'isContainerHost',
        'operatingSystem', 'hardware', 'userAccountListData', 'openPortListData', 'volumeListData',
        'networkInterfaceListData', 'softwareListData', 'provider', 'cloudProvider', 'agent', 'sensor', 'container',
        'inventory', 'activity', 'tagList', 'serviceList', 'lastLocation', 'criticality',
        'businessInformation', 'assignedLocation', 'businessAppListData',
        'riskScore', 'passiveSensor', 'domain', 'subdomain', 'whois', 'isp', 'asn',
        'processor', 'missingSoftware', 'BATCH_DATE', 'BATCH_NUMBER', 'Row_Last_Updated'
                   ]
    return csv_columns


def asset_inventory_csv_column_types():

    csv_columns = {
        'assetId': 'INTEGER', 'hostId': 'INTEGER'
    }
    return csv_columns


def asset_inventory_software_assetid_csv_columns():

    csv_columns = [
        'assetId', 'fullName'
    ]
    return csv_columns


def asset_inventory_software_assetid_csv_column_types():

    csv_columns = {
        'assetId': 'INTEGER'
    }
    return csv_columns


def asset_inventory_software_unique_csv_columns():
    csv_columns = [
        'fullName'
    ]
    return csv_columns

def asset_inventory_software_unique_csv_column_types():

    csv_columns = {
    }
    return csv_columns

def asset_inventory_software_os_unique_csv_columns():
    csv_columns = [
        'fullName', 'osName',
        'isIgnored', 'ignoredReason', 'category', 'gaDate', 'eolDate', 'eosDate',
        'stage', 'lifeCycleConfidence', 'eolSupportStage', 'eosSupportStage'
    ]
    return csv_columns

def asset_inventory_software_os_unique_csv_column_types():

    csv_columns = {
    }
    return csv_columns


def was_webapp_csv_columns():
    csv_columns = [
        'id', 'name', 'url', 'os', 'owner', 'scope', 'subDomain', 'domains', 'uris', 'attributes', 'defaultProfile',
        'defaultScanner', 'defaultScannerTags', 'scannerLocked', 'progressiveScanning', 'redundancyLinks',
        'maxRedundancyLinks', 'urlBlacklist', 'urlWhitelist', 'postDataBlacklist', 'logoutRegexList', 'authRecords',
        'dnsOverrides', 'useRobots', 'useSitemap', 'headers', 'malwareMonitoring', 'malwareNotification',
        'malwareTaskId', 'malwareScheduling', 'tags', 'comments', 'isScheduled', 'lastScan', 'createdBy',
        'createdDate', 'updatedBy', 'updatedDate', 'screenshot', 'proxy', 'config', 'crawlingScripts',
        'lastScanStatus', 'removeFromSubscription', 'reactivateIfExists', 'postmanCollection', 'swaggerFile',
        'BATCH_DATE', 'BATCH_NUMBER', 'Row_Last_Updated'
    ]
    return csv_columns


def was_webapp_csv_column_types():

    csv_columns = {
        'id': 'INTEGER'
    }
    return csv_columns


def was_finding_csv_columns():
    # "Finding": {
    #     "webApp": {
    #         "id": 78440423,
    #         "tags": {
    #             "list": [
    #                 {
    #                     "Tag": {
    #                         "name": "Web Application Assets",
    #                         "id": 7472465
    #                     }
    #                 }
    #             ],
    #             "count": 1
    #         },
    #         "url": "http://owaspbwa/bWAPP/login.php",
    #         "name": "bWAPP"
    #     },
    #     "id": 149802,
    #     "url": "http://owaspbwa/bWAPP/login.php",
    #     "lastDetectedDate": "2018-07-03T20:06:11Z",
    #     "qid": 0,
    #     "etl_workflow_validation_type": "VULNERABILITY",
    #     "status": "NEW",
    #     "timesDetected": 1,
    #     "potential": "false",
    #     "findingType": "BURP",
    #     "lastTestedDate": "2018-07-03T20:06:11Z",
    #     "firstDetectedDate": "2018-07-03T20:06:11Z",
    #     "isIgnored": "false",
    #     "severity": "5",
    #     "uniqueId": "e5028940-ffe9-4a6d-90c8-68724b96ed89"
    # }

    # csv_columns = [
    #     'id', 'webApp_id', 'webApp_name', 'webApp_tags', 'webApp_url',
    #     'url', 'lastDetectedDate', 'qid', 'etl_workflow_validation_type', 'status', 'timesDetected',
    #     'potential', 'findingType', 'lastTestedDate', 'firstDetectedDate', 'isIgnored',
    #     'severity', 'uniqueId'
    # ]
    # Note: group_0 and function_0 contain "group" and "function" data for DB Compatability.
    csv_columns = [
        'id', 'webApp_id', 'webApp_name', 'webApp_tags', 'webApp_url', 'uniqueId',
        'qid', 'name', 'potential', 'findingType', 'group_0',
        'cwe', 'owasp', 'wasc', 'param', 'function_0', 'content', 'resultList', 'severity',
        'originalSeverity', 'url', 'status', 'firstDetectedDate', 'lastDetectedDate',
        'timesDetected', 'webApp', 'patch', 'isIgnored', 'ignoredReason', 'ignoredBy',
        'ignoredDate', 'ignoredComment', 'reactivateIn', 'reactivateDate', 'externalRef',
        'severityComment', 'editedSeverityUser', 'editedSeverityDate', 'retest',
        'sslData', 'cvssV3', 'history', 'updatedDate',
        'BATCH_DATE', 'BATCH_NUMBER', 'Row_Last_Updated'
    ]
    return csv_columns


def was_finding_csv_column_types():

    csv_columns = {
        'webApp_id': 'INTEGER', 'id': 'INTEGER', 'severity': 'INTEGER', 'timesDetected': 'INTEGER', 'qid': 'INTEGER'
    }
    return csv_columns


def was_catalog_csv_columns():
    # {
    #     "Catalog": {
    #         "fqdn": "ks355837.kimsufi.com",
    #         "updatedDate": "2022-01-18T19:45:09Z",
    #         "id": 11403514,
    #         "source": "VM_SCAN",
    #         "operatingSystem": "Ubuntu / Linux 2.6.x",
    #         "port": "443",
    #         "createdDate": "2021-08-31T18:11:41Z",
    #         "status": "NEW",
    #         "ipAddress": "91.121.138.65",
    #         "updatedBy": {
    #             "firstName": "John Delaroderie",
    #             "id": 84004451,
    #             "lastName": "TAM-LAB",
    #             "username": "tamde_hd1"
    #         }
    #     }
    # },

    csv_columns = [
        'id', 'ipAddress', 'fqdn', 'port', 'operatingSystem', 'source', 'status',
        'createdDate', 'updatedDate', 'updatedBy',
        'BATCH_DATE', 'BATCH_NUMBER', 'Row_Last_Updated'
    ]
    return csv_columns


def was_catalog_csv_column_types():

    csv_columns = {
        'id': 'INTEGER'
    }
    return csv_columns


def status_table_csv_columns():  # Return list of csv columns

    csv_columns = [
        'STATUS_NAME', 'STATUS_DETAIL', 'LAST_BATCH_PROCESSED', 'Row_Last_Updated'
    ]
    return csv_columns


def status_table_csv_column_types():

    csv_columns = {
        'LAST_BATCH_PROCESSED': 'TEXT'
    }
    return csv_columns


def set_limit_open_files_to_hard_limit_for_multiprocessing_pipes(module_function="limit_open_files", logger_method=print):
    # Host List Detection accumulates pipes open during processing.
    # Until addressed, ensure open files is set to hard limit.
    limit_soft, limit_hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    logger_method(f"limit_open_files before: {module_function} limit_soft={limit_soft}, limit_hard={limit_hard}")
    resource.setrlimit(resource.RLIMIT_NOFILE, (limit_hard, limit_hard))
    limit_soft, limit_hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    logger_method(f"limit_open_files after:  {module_function} limit_soft={limit_soft}, limit_hard={limit_hard}")


def total_system_stats_cpu_ram_swap_disk(sys_stat: dict):
    global system_usage_counters
    system_usage_counters.append(sys_stat)


def log_system_stats_cpu_ram_swap_disk():
    global system_usage_counters
    system_stat = etld_lib_functions.log_system_information(
        data_directory=qetl_user_home_dir,
        logger_method=etld_lib_functions.logger.info)

    system_usage_counters.append(system_stat)

    etld_lib_functions.if_disk_space_usage_greater_than_90_log_warning(
        data_directory=qetl_user_home_dir,
        logger_method=etld_lib_functions.logger.warn)


def check_swap_space():
    etld_lib_functions.if_swap_space_total_is_low_log_warning(
        logger_method=etld_lib_functions.logger.warn
    )


def check_ram_space():
    etld_lib_functions.if_ram_space_size_is_low_log_warning(
        logger_method=etld_lib_functions.logger.warn
    )


def main():
    get_qetl_code_dir()
    set_qetl_code_dir_etld_cred_yaml_template_path()
    setup_user_home_directories()
    load_etld_lib_config_settings_yaml()
    setup_requests_module_tls_verify_status()

    setup_csv_distribution_vars()
    get_csv_distribution_config()

    setup_kb_vars()
    get_kb_user_config()

    setup_host_list_vars()
    get_host_list_user_config()

    setup_host_list_detection_vars()
    get_host_list_detection_user_config()

    setup_asset_inventory_vars()
    get_asset_inventory_user_config()

    setup_was_vars()
    get_was_user_config()

    setup_test_system_vars()

    set_limit_open_files_to_hard_limit_for_multiprocessing_pipes(logger_method=etld_lib_functions.logger.info)
    log_system_stats_cpu_ram_swap_disk()
    setup_completed()


if __name__ == '__main__':
    etld_lib_functions.main()
    main()


