#!/usr/bin/env python3
from pathlib import Path
import json
#from qualys_etl.etld_lib import etld_lib_credentials
from qualys_etl.etld_lib import etld_lib_authentication_objects
from qualys_etl.etld_lib import etld_lib_config
from qualys_etl.etld_lib import etld_lib_functions
from qualys_etl.etld_lib import etld_lib_extract_transform_load


def policy_compliance_extract(asset_last_updated, last_seen_assetid, batch_number_str,
                            qualys_headers_dict, cred_dict, file_info_dict) -> dict:

    begin_policy_compliance_04_extract(message=f"start batch: {batch_number_str}")
    bearer = cred_dict['bearer']
    page_size = 300

    # /rest/2.0/search/am/asset?assetLastUpdated=2021-06-01T00:00:00Z&lastSeenAssetId=0
    url = f"https://{cred_dict['gateway_fqdn_server']}/rest/2.0/search/am/asset"
    url = f"{url}?assetLastUpdated={asset_last_updated}&lastSeenAssetId={last_seen_assetid}&pageSize={page_size}"
    headers = {'X-Requested-With': 'qualysetl', 'Authorization': bearer, 'Content-Type': 'application/json'}
    etld_lib_functions.logger.info(f"api call     - {url}")

    json_file = Path(file_info_dict['next_file_path'])

    cred_dict = etld_lib_extract_transform_load.extract_qualys(
        try_extract_max_count=etld_lib_config.policy_compliance_try_extract_max_count,
        url=url,
        headers=headers,
        payload={},
        http_conn_timeout=etld_lib_config.policy_compliance_http_conn_timeout,
        chunk_size_calc=etld_lib_config.policy_compliance_chunk_size_calc,
        output_file=json_file,
        cred_dict=cred_dict,
        qualys_headers_multiprocessing_dict=qualys_headers_dict,
        batch_number_formatted=batch_number_str,
        extract_validation_type='json',
        compression_method=etld_lib_config.policy_compliance_open_file_compression_method)

    end_policy_compliance_04_extract(message=f"start batch: {batch_number_str}")
    return cred_dict  # For 401 Edge Case


def policy_compliance_extract_count(asset_last_updated, last_seen_assetid, batch_number_str, qualys_headers_dict, cred_dict, file_info_dict):

    begin_policy_compliance_04_extract(message=f"start extract count for asset_last_updated: {asset_last_updated}")
    bearer = cred_dict['bearer']
    url = f"https://{cred_dict['gateway_fqdn_server']}/rest/2.0/count/am/asset"
    url = f"{url}?assetLastUpdated={asset_last_updated}&lastSeenAssetId={last_seen_assetid}"
    headers = {'X-Requested-With': 'qualysetl', 'Authorization': bearer, 'Content-Type': 'application/json'}
    etld_lib_functions.logger.info(f"api call     - {url}")

    json_file = Path(file_info_dict['next_file_path'])

    cred_dict = etld_lib_extract_transform_load.extract_qualys(
        try_extract_max_count=etld_lib_config.policy_compliance_try_extract_max_count,
        url=url,
        headers=headers,
        payload={},
        http_conn_timeout=etld_lib_config.policy_compliance_http_conn_timeout,
        chunk_size_calc=etld_lib_config.policy_compliance_chunk_size_calc,
        output_file=json_file,
        cred_dict=cred_dict,
        qualys_headers_multiprocessing_dict=qualys_headers_dict,
        batch_number_formatted=batch_number_str,
        extract_validation_type='json')

    policy_compliance_log_count(json_file=json_file)
    end_policy_compliance_04_extract(message=f"start extract count for asset_last_updated: {asset_last_updated}")


def policy_compliance_log_count(json_file):
    try:
        with etld_lib_config.policy_compliance_open_file_compression_method(
                str(json_file), "rt", encoding='utf-8') as read_file:
            ai_count = json.load(read_file)
            if "responseCode" in ai_count.keys():
                if ai_count['responseCode'] == 'SUCCESS':
                    etld_lib_functions.logger.info(f"Asset Inventory Count: {ai_count['count']}")
                else:
                    raise Exception(f"Asset Inventory Count Failed, responseCode: {ai_count['responseCode']},"
                                    f" responseMessage: {ai_count['responseMessage']}")
    except Exception as e:
        etld_lib_functions.logger.error(f"Exception: {e}")
        etld_lib_functions.logger.error(f"Potential JSON File corruption or api error detected: {json_file}")
        exit(1)


def begin_policy_compliance_04_extract(message=""):
    etld_lib_functions.logger.info(f"start {message}")


def end_policy_compliance_04_extract(message=""):
    etld_lib_functions.logger.info(f"end   {message}")


def main(args=None):
    etld_lib_authentication_objects.qualys_authentication_obj.get_current_bearer_token()
    credentials_dict = etld_lib_authentication_objects.qualys_authentication_obj.get_credentials_dict()
    # TODO FOR TESTING, CREATE TEST BATCH OPTIONS HERE.
    policy_compliance_extract(cred_dict=credentials_dict)


if __name__ == "__main__":
    etld_lib_functions.main(my_logger_prog_name='policy_compliance_04_extract_from_qualys')
    etld_lib_config.main()
    #etld_lib_credentials.main()
    etld_lib_authentication_objects.main()
    main()



