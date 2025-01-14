# [Qualys API Best Practices Series](https://blog.qualys.com/tag/api-best-practices-series) 

## Release Notes: 

0.8.20 includes the following updates.  See Changelog for additional details.
   - Added QualysETL Automation for injecting schema/data into downstream databases for metrics, analysis and visualization in PowerBI, Tableau, etc. Databases Tested include Azure CosmosDB (PostgreSQL), PostgreSQL Open Source, Amazon Redshift, Snowflake, Mysql, Microsoft SQL Server.
   - Added Docker Beta to run QualysETL in a container 
   - Added QWEB 10.23 Updates - See [QWEB 10.23 release notification for details](https://www.qualys.com/docs/release-notes/qualys-cloud-platform-10.23-api-release-notes.pdf) 
   - Tested on Ubuntu 22.04 and Red Hat 9.x as they are the latest supported platforms.
   - The 0.8.x series supports VM, CSAM and WAS Data.
   - Next on the roadmap is Policy Compliance (PCRS) for Nov, 2023.
   - Please see the accompanying videos for additional guidance
     - Part 3 - Host List Detection. [Qualys API Best Practices Series](https://blog.qualys.com/tag/api-best-practices-series) 
     - Part 4 - CyberSecurity Asset Management. [Qualys API Best Practices Series](https://blog.qualys.com/tag/api-best-practices-series) 
   - The latest schema snapshots are in this document for reference.  To obtain the latest schema from QualysETL, please use the SQLite Database output from QualysETL.
   - See [Python Package Index for Qualys ETL](https://pypi.org/project/qualysetl/) for latest version of qualysetl.
   - See [Roadmap](#roadmap) for additional details on what's coming next.  
   - See [Quick Start](#quick-start) to get started now.
   
## Qualys Data Included in QualysETL:
1. **KnowledgeBase** - QID Definitions
2. **Host List** - Host Information
3. **Host List Detection** - Host Vulnerability Information
4. **CyberSecurity Asset Inventory** - Detailed Asset Inventory
5. **Web Application Scanning** - Web Applications and Web Application Vulnerability Findings.

## Key Benefits of QualysETL
1. No code solution to Extract/Transform/Load and Distribute Qualys Data with one command.
2. Provides XML, JSON, SQLITE and CSV Prepared for database load into MySQL, Postgres, SnowFlake, Amazon RedShift, etc.
3. Streaming Data option for immediate ingestion of Vulnerabilities or Asset Inventory batches into your downstream database.
4. Packaged and ready for ease of use.  Install and test within 5 minutes on your Ubuntu 22.04 system.
5. Open Source - Packaged under the Apache 2 license.

## Example: QualysETL Usage - qetl_manage_user
```text
    
    Please enter -u [ your /opt/qetl/users/ user home directory path ]

    Note: /opt/qetl/users/newuser is the root directory for your qetl userhome directory,
    Example:
             qetl_manage_user -u /opt/qetl/users/[your_user_name]
 
    usage: qetl_manage_user [-h] [-u qetl_USER_HOME_DIR] [-e etl_[module] ] [-e validate_etl_[module] ] [-c] [-t] [-i] [-d] [-r] [-l]
    
    Command to Extract, Transform and Load Qualys Data into various forms ( CSV, JSON, SQLITE3 DATABASE )
    
    optional arguments:
      -h, --help                show this help message and exit
      -u Home Directory Path,   --qetl_user_home_dir Home directory Path
                                   Example:
                                   - /opt/qetl/users/q_username
      -e etl_[module],          --execute_etl_[module] execute etl of module name. valid options are:
                                       -e etl_knowledgebase 
                                       -e etl_host_list 
                                       -e etl_host_list_detection
                                       -e etl_asset_inventory
                                       -e etl_was
                                       -e etl_test_system ( for a small system test of all ETL Jobs )
      -e validate_etl_[module], --validate_etl_[module] [test last run of etl_[module]].  valid options are:
                                       -e validate_etl_knowledgebase
                                       -e validate_etl_host_list 
                                       -e validate_etl_host_list_detection
                                       -e validate_etl_asset_inventory
                                       -e validate_etl_was
                                       -e validate_etl_test_system 
      -d YYMMDDThh:mm:ssZ,      --datetime      YYYY-MM-DDThh:mm:ssZ UTC. Get All Data On or After Date. 
                                                Ex. 1970-01-01T00:00:00Z acts as flag to obtain all data.
      -c, --credentials        update qualys api user credentials: qualys username, password or api_fqdn_server
      -t, --test               test qualys credentials
      -i, --initialize_user    For automation, create a /opt/qetl/users/[userhome] directory 
                               without being prompted.
      -l, --logs               detailed logs sent to stdout for testing qualys credentials
      -v, --version            Help and QualysETL version information.
      -r, --report             brief report of the users directory structure.
      -p, --prompt-credentials prompt user for credentials, also accepts stdin with credentials piped to program.
      -m, --memory-credentials get credentials from environment: 
                               Example: q_username="your userid", q_password=your password, q_api_fqdn_server=api fqdn, q_gateway_fqdn_server=gateway api fqdn
      -s, --stdin-credentials  send credentials in json to stdin. 
                               Example:
                               {"q_username": "your userid", "q_password": "your password", "q_api_fqdn_server": "api fqdn", "q_gateway_fqdn_server": "gateway api fqdn"}
      
    Example: ETL Host List Detection
    
    qetl_manage_user -u [path] -e etl_host_list_detection -d 1970-01-01T00:00:00Z
    
     - qetl_manage_user will download all knowledgebase, host list and host list detection vulnerability data,
       transforming/loading it into sqlite and optionally the corresponding distribution directory.
     
     Inputs: 
       - KnowledgeBase API, Host List API, Host List Detection API.
       - ETL KnowledgeBase
         - /api/2.0/fo/knowledge_base/vuln/?action=list
       - ETL Host List
         - /api/2.0/fo/asset/host/?action=list
       - ETL Host List Detection - Stream of batches immediately ready for downstream database ingestion.
         - /api/2.0/fo/asset/host/vm/detection/?action=list
     Outputs:
       - XML, JSON, SQLITE, AND Distribution_Directory of CSV BATCH FILES PREPARED FOR DATABASE INGESTION.
         - host_list_detection_extract_dir - contains native xml and json transform of data from qualys, compressed in uniquely named batches.
         - host_list_detection_distribution_dir - contains transformed/prepared data ready for use in database loaders such as mysql.
         - host_list_detection_sqlite.db - sqlite database will contain multiple tables:
           - Q_Host_List                            - Host List Asset Data from Host List API.
           - Q_Host_List_Detection_Hosts            - Host List Asset Data from Host List Detection API. 
           - Q_Host_List_Detection_QIDS             - Host List Vulnerability Data from Host List Detection API. 
           - Q_KnowledgeBase_In_Host_List_Detection - KnowledgeBase QIDs found in Q_Host_List_Detection_QIDS. 
         
   etld_config_settings.yaml notes:
       1. To Enable CSV Distribution, add the following keys to etld_config_settings.yaml and toggle on/off them via True or False
            kb_distribution_csv_flag: True                    # populates qetl_home/data/knowledgebase_distribution_dir
            host_list_distribution_csv_flag: True             # populates qetl_home/data/host_list_distribution_dir
            host_list_detection_distribution_csv_flag: True   # populates qetl_home/data/host_list_detection_distribution_dir
            asset_inventory_distribution_csv_flag: True       # populates qetl_home/data/asset_inventory_distribution_dir
            was_distribution_csv_flag: True                   # populates qetl_home/data/was_distribution_dir
              
            These files are prepared for database load, tested with mysql.  No headers are present.  
            Contact your Qualys TAM and schedule a call with David Gregory if you need assistance with this option.

```

## Example: ETL Host List Detection

```text
    qetl_manage_user -u [path] -e etl_host_list_detection -d 1970-01-01T00:00:00Z
    
     - qetl_manage_user will download all knowledgebase, host list and host list detection vulnerability data,
       transforming/loading it into sqlite and optionally the corresponding distribution directory.
     
     Inputs: 
       - KnowledgeBase API, Host List API, Host List Detection API.
       - ETL KnowledgeBase
         - /api/2.0/fo/knowledge_base/vuln/?action=list
       - ETL Host List
         - /api/2.0/fo/asset/host/?action=list
       - ETL Host List Detection - Stream of batches immediately ready for downstream database ingestion.
         - /api/2.0/fo/asset/host/vm/detection/?action=list
     Outputs:
       - XML, JSON, SQLITE, AND Distribution_Directory of CSV BATCH FILES PREPARED FOR DATABASE INGESTION.
         - host_list_detection_extract_dir - contains native xml and json transform of data from qualys, compressed in uniquely named batches.
         - host_list_detection_distribution_dir - contains transformed/prepared data ready for use in database loaders such as mysql.
         - host_list_detection_sqlite.db - sqlite database will contain multiple tables:
           - Q_Host_List                            - Host List Asset Data from Host List API.
           - Q_Host_List_Detection_Hosts            - Host List Asset Data from Host List Detection API. 
           - Q_Host_List_Detection_QIDS             - Host List Vulnerability Data from Host List Detection API. 
           - Q_KnowledgeBase_In_Host_List_Detection - KnowledgeBase QIDs found in Q_Host_List_Detection_QIDS. 

```
### Schema etl_host_list_detection - Extract from host_list_detection_sqlite.db file.

[![](https://user-images.githubusercontent.com/82658653/259297461-983d770b-125d-4942-b1ce-3c4495d4f9a7.png)](https://user-images.githubusercontent.com/82658653/259297461-983d770b-125d-4942-b1ce-3c4495d4f9a7.png)

## Example: ETL Asset Inventory (GAV/CSAM API)

```text
    qetl_manage_user -u [path] -e etl_asset_inventory -d 1970-01-01T00:00:00Z

     - qetl_manage_user will download all asset inventory data, transforming/loading them into sqlite.
         
     Inputs: 
       - Global Asset View/CyberSecurity Asset Management API V2.
       - ETL Asset Inventory - Stream of batches immediately ready for downstream database ingestion.
         - /rest/2.0/search/am/asset?assetLastUpdated=[date]
     Outputs:
       - JSON, SQLITE, AND Distribution_Directory of CSV BATCH FILES PREPARED FOR DATABASE INGESTION.
         - asset_inventory_extract_dir - contains json of data from qualys, compressed in uniquely named batches.
         - asset_inventory_distribution_dir - contains transformed/prepared data ready for use in database loaders such as mysql.
         - asset_inventory_sqlite.db - sqlite database will contain multiple tables:  
           *  Q_Asset_Inventory                  - Asset Inventory of Asset Last Updated -d 'DATE' to now 
           *  Q_Asset_Inventory_Software_Unique  - Unique List of Software
           *  Q_Asset_Inventory_Software_AssetId - Unique List of AssetId to Software 
    
```
### Schema etl_asset_inventory - Extract from asset_inventory_sqlite.db file.

[![](https://user-images.githubusercontent.com/82658653/259301160-7b4ec0d0-62c1-4340-bf89-5107221661ce.png)](https://user-images.githubusercontent.com/82658653/259301160-7b4ec0d0-62c1-4340-bf89-5107221661ce.png)

## Example: ETL Web Application Data (WAS API)

```text
    Example: 
    
    qetl_manage_user -u [path] -e etl_was -d 1970-01-01T00:00:00Z
    
     Inputs:
       - Web Application Scanning API
         - /qps/rest/3.0/search/was/catalog
         - /qps/rest/3.0/search/was/webapp
         - /qps/rest/3.0/get/was/webapp/<id>
         - /qps/rest/3.0/search/was/finding
     Outputs:
       - was_extract_dir - contains json of data from qualys, compressed in uniquely named batches.
       - was_distribution_dir - contains transformed/prepared data ready for use in database loaders such as mysql.
       - was_sqlite.db - sqlite database will contain multiple tables:  
         *  Q_WAS_WebApp   - Web Applications and Web Application Details
         *  Q_WAS_Finding  - Web Application Findings (Vulnerabilities)
         *  Q_WAS_Catalog  - WAS Module Catalog 
```
### Schema etl_was - Extract from was_sqlite.db file.

[![](https://user-images.githubusercontent.com/82658653/259300384-ca207348-77e2-4a0d-b2a0-6353075cb82a.png)](https://user-images.githubusercontent.com/82658653/259300384-ca207348-77e2-4a0d-b2a0-6353075cb82a.png)


## Table of contents
* [Quick Start](#quick-start)
   * [Install](#installation)
   * [Uninstall](#uninstall)
* [Qualys API Best Practices Series](#qualys-api-best-practices-series)
   * [Workflow Diagram](#workflow-diagram)
   * [Component Diagram](#component-diagram)
   * [Blueprint](#blueprint)
   * [Roadmap](#roadmap)
   * [Technologies](#technologies) 
* [ETL Examples](#etl-examples)
    * [ETL KnowledgeBase](#etl-knowledgebase)
    * [ETL Host List](#etl-host-list)
    * [ETL Host List Detection](#etl-host-list-detection)
    * [ETL Asset Inventory](#etl-asset-inventory)
    * [ETL Web_Application_Scanning](#etl-web-application-scanning-data)
* [Application Manager and Data](#application-manager-and-data)
    * [Host List Detection SQLite Database](#host-list-detection-sqlite-database)
    * [Data Formats](#data-formats)
    * [Logging](#logging)
    * [Application Monitoring](#application-monitoring)
* [Securing Your Application in the Data Center](#securing-your-application-in-the-data-center)
    * [Password Vault](#password-vault)
* [Example Run Logs](#example-run-logs)
    * [Uninstall and Install qetl](#uninstall-and-install-qetl)
    * [qetl_setup_python_env](#qetl_setup_python_env)  
    * [qetl_manage_user](#qetl_manage_user)
    * [qetl_manage_user Add User](#qetl_manage_user-add-user)
    * [qetl_manage_user ETL KnowledgeBase](#qetl_manage_user-etl-knowledgebase)
    * [Review ETL KnowledgeBase Data](#review-etl-knowledgebase-data)
* [License](#license)
* [ChangeLog](#changelog)


## Quick Start

Ubuntu 22.04 LTS is the primary OS to run QualysETL.
Red Hat 9.x latest is an alternative OS that has been tested.  Scroll past the Ubuntu Install for Red Hat 8.x instructions.
Contact your TAM and David Gregory for details.

### Prerequisites Python Module on Ubuntu 22.04
     1) Ubuntu 22.04 LTS
     2) Python 3.8.5 or Latest Stable Release
     3) On base 22.04 you'll need two additional packages.
        sudo apt-get install python3-venv  
        sudo apt install python3-pip
     4) Disk Space on Host.  
        - 100,000 hosts, expect ~400 Gigabytes for full copy of VM Data (Confirmed, Potential, Info Gathered)
        - KnowledgeBase - expect ~1 Gigabyte.
        - Host List - expect ~10 Gigabyte for 100K Hosts.
        - Host List Detection - expect ~300-400 Gigabytes for 100K Hosts.

### Installation

#### First Time Setup Activity on Ubuntu 22.04
 - Login as "non-root" user that will run qualysetl.
 - sudo root authorization required.
 - Create your /opt/qetl application directory
 - update apt package cache
 - Install python3-venv
 - Install python3-pip
 - Install sqlite3 
 - Install sqlite3 sql browser 

#### First Time Setup Instructions on Ubuntu 22.04
```bash
#!/usr/bin/env bash
# First Time Setup - Pre-create directory /opt/qetl
# Login as user that will execute qetl_manage_user
sudo mkdir /opt/qetl    
sudo chown $USERNAME /opt/qetl
sudo chgrp $USERNAME /opt/qetl
sudo apt update
sudo apt install -y python3-venv python3-pip sqlite3 sqlitebrowser
```

#### Alternative First Time Setup Activity on Red Hat 8.x
- Login as "non-root" user that will run qualysetl.
- sudo root authorization required.
- Create your /opt/qetl application directory
- Install python3.9
- Update alternatives to point python3 at python3.9
- NOTE: sqlitebrowser is not part of Red Hat distribution.  You may want to install sqlitebrowser from a trusted source, or select another sqlite workbench.

#### Alternative First Time Setup Instructions on Red Hat 8.x
```bash
#!/usr/bin/env bash
# First Time Setup - Pre-create directory /opt/qetl
# Login as user that will execute qetl_manage_user
sudo mkdir /opt/qetl    
sudo chown $USERNAME /opt/qetl
sudo chgrp $USERNAME /opt/qetl
sudo yum -y install python39
sudo alternatives --set python3  /usr/bin/python3.9
```

#### Install or Upgrade QualysETL activity on Ubuntu or Red Hat
- Login as "non-root" user that will run qualysetl.
- deactivate to exit any current python virtual environment you may be in.
- Install/Upgrade qualysetl into your /home/$USERNAME/.local python directory
- Create qualysetl python virtual environment in /opt/qetl/qetl_venv,
  installing all required modules in venv
- Execute qualysetl to see help screen


#### Install or Upgrade QualysETL Instructions on Ubuntu or Red Hat

```bash
#!/usr/bin/env bash
# Login as user that will execute qetl_manage_user
# Install Application in Python Virtual Environment /opt/qetl/qetl_venv
deactivate  2>/dev/null   # Ensure you are not in a python virtual environment, error is ok.
python3 -m pip install --upgrade qualysetl
~/.local/bin/qetl_setup_python_venv /opt/qetl
echo "Follow instructions output from qetl_setup_python_venv"
```

### Create your first qualysetl user
To setup your first user, you'll need your qualys api username, password and your api fqdn.

Example transcript of setting up a new user

```bash
qualysetl@ubuntu:~$ source /opt/qetl/qetl_venv/bin/activate
(qetl_venv) qualysetl@ubuntu:~$ qetl_manage_user -u /opt/qetl/users/quays_dt4

qetl_user_home_dir does not exist: /opt/qetl/users/quays_dt4/qetl_home
Create new qetl_user_home_dir? /opt/qetl/users/quays_dt4/qetl_home ( yes or no ): yes

qetl_user_home_dir created: /opt/qetl/users/quays_dt4/qetl_home

Current username: initialuser in config: /opt/qetl/users/quays_dt4/qetl_home/cred/.etld_cred.yaml
Update Qualys username? ( yes or no ): yes
Enter new Qualys username: quays_dt4
Current api_fqdn_server: qualysapi.qualys.com
Update api_fqdn_server? ( yes or no ): 
Enter new api_fqdn_server: qualysapi.qualys.com
Update password for username: quays_dt4
Update password? ( yes or no ): yes
Enter your Qualys password: 
You have updated your credentials.
  Qualys Username: quays_dt4
  Qualys api_fqdn_server: qualysapi.qualys.com


Would you like to test login/logout of Qualys? ( yes or no ): yes

Qualys Login Test for quays_dt4 at api_fqdn_server: qualysapi.qualys.com

Testing Qualys Login for quays_dt4 Succeeded at qualysapi.qualys.com
    with HTTPS Return Code: 200.

Thank you, exiting.

(qetl_venv) qualysetl@ubuntu:~$ 

```

### Execute your first ETL.
Your initial configuration limits the total hosts downloaded to 1000 hosts vm_processed_after 
utc.now - 1 day.  The initial configuration will only consume up to 2 connections.
You can test this to ensure you are able to download data before moving on to more data.
- Command - qetl_manage_user -u /opt/qetl/users/quays_dt4 -e etl_host_list_detection
- Ouputs: 
     - Full Knowledgebase on first run.
     - Host List vm_processed_after utc.now - 1 day limited to 1000 hosts for testing. 
     - Host List Detection driven by scope of Host List.

Transcript of command execution.  
```bash
qetl_manage_user -u /opt/qetl/users/quays_dt4 -e etl_host_list_detection
Starting etl_host_list_detection.  For progress see: /opt/qetl/users/quays_dt4/qetl_home/log/host_list_detection.log
Ending   etl_host_list_detection.  For results see: /opt/qetl/users/quays_dt4/qetl_home/log/host_list_detection.log
sqlitebrowser /opt/qetl/users/quays_dt4/qetl_home/data/host_list_detection_sqlite.db 
```
SQLite Browser displaying Knowledgebase, Host List, and Host List Detection. Note that the knowledgebase in this database 
only includes qids found in host list detection.  To see the full knowledgebase, open kb_sqlite.db.  Q_Host_List_Detection is a view of Q_Host_List ( PREFIX HL_ ), Q_Host_List_Detection_Hosts ( PREFIX HLDH_ ), Q_Host_List_Detectino_QIDS ( PREFIX HLDQ_ ).

[![](https://user-images.githubusercontent.com/82658653/149306161-378d3240-e817-427e-801b-4c0301743389.png)](https://user-images.githubusercontent.com/82658653/149306161-378d3240-e817-427e-801b-4c0301743389.png)


### Uninstall

Uninstall qualysetl activity on Ubuntu 22.04.
  - deactivate to exit any current python virtual environment you may be in.
  - optionally remove application/data:
    - python virtual environment: /opt/qetl/qetl_venv
    - qualysetl data directory: /opt/qetl/users
    - python3-venv 
    - python3-pip
    - sqlite3
    - sqlitebroswer
    
```bash
#!/usr/bin/env bash
deactivate  # If you are in a python virtual environment
python3 -m pip uninstall qualysetl
# Optionally remove python virtual env, pip, sqlite3, sqlitebrowser and users application data.
# cd /opt/qetl/
# rm -ir qetl_venv  # Optionally remove qetl_venv
# rm -ir users      # Optionally remove users directory with data
# sudo apt remove -y python3-venv python3-pip sqlite3 sqlitebrowser
```

 Uninstall qualysetl activity on Red Hat 8.x
   - deactivate to exit any current python virtual environment you may be in.
   - optionally remove application/data:
     - python virtual environment: /opt/qetl/qetl_venv
     - qualysetl data directory: /opt/qetl/users

```bash
#!/usr/bin/env bash
deactivate  # If you are in a python virtual environment
python3 -m pip uninstall qualysetl
# Optionally remove python virtual env and user data
# cd /opt/qetl/
# rm -ir qetl_venv  # Optionally remove qetl_venv
# rm -ir users      # Optionally remove users directory with data
```

- Jump to [ETL Examples](#etl-examples) to transform Qualys data into CSV, JSON and SQLite Databases.

## Qualys API Best Practices Series
The example code from the [Qualys API Best Practices Series](https://blog.qualys.com/tag/api-best-practices-series) 
is being hosted here to help customers with an example blueprint to automate transformation 
of data into their corporate data systems, further enhancing the visibility of outlier systems 
that are vulnerable.  

This example code has been enhanced with some exception processing, logging, and a single point of execution
creating an operational context within which to test/develop the code so customers can build automation 
into their remediation program. 

### Workflow Diagram
The workflow depicts the flow of etl for host list detection.  The key output is the sqlite database that is ready for distribution
- qetl_manage_user -u [userdir] -e etl_host_list_detection -d [datetime] - Resulting sqlite database ready for distribution.

[![](https://github.com/dg-cafe/qualysetl/assets/82658653/7efbf1a6-3f60-415a-ae65-628014374a33)](https://github.com/dg-cafe/qualysetl/assets/82658653/7efbf1a6-3f60-415a-ae65-628014374a33)

### Component Diagram
The component diagram depicts major system interoperability components that deliver data into the enterprise.

| Component             | Color  | Purpose                                                                                                                                                                                    |
|-----------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Execution Environment | Blue   | Host and Cloud where this application operates                                                                                                                                             |
| Application           | Grey   | Application context to identify Local Docker, Python Application, Host and/or Filesystems                                                                                                  |
| Input                 | Orange | Qualys data consumed by application                                                                                                                                                        |
| Execution             | Green  | Execution ETL of Qualys Data through various methods.  (The Python Execution Environment on Docker or Traditional Host)                                                                    |
| Data                  | Yellow | Host Data Folders that separate Application, and Subscription Data Users along with distribution pipelines representing the distribution of data to external sources, Cloud, Client, Other |
| Future                | Black  | TBD Future State Components such as GraphQL Server.                                                                                                                                        |

[![](https://user-images.githubusercontent.com/82658653/120926641-c1ea5800-c6ab-11eb-832b-1af03f77462a.png)](https://user-images.githubusercontent.com/82658653/120926641-c1ea5800-c6ab-11eb-832b-1af03f77462a.png)

### Blueprint
Customer have many options for Qualys API integration today.  Some customers realize they need to develop their own 
internal code to transform complex data, create custom metrics, create custom reports or ensure data is more accessible within their organizations for metrics and custom reporting.

As a result, Qualys decided on creating the API Best Practices Series to jumpstart clients with a blueprint of example code
to help them automate delivery of complex data into their enterprise.  

The overarching goal is to simplify our customers security stack and help them significantly reduce cost and 
complexity.

Key Goals and Solutions of this series are:

| Goal                                                                                   | Solution                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Automate Vulnerability Data accessibility, transformation of complex data for analysis | JSON, CSV, SQLite Database Formats of Qualys Data readily accessible to Analytical BI Tools for on-demand analysis or for downstream loading into Enterprise Data Storage.                   |
| A single query interface to Qualys data                                                | TBD Future GraphQL Server interface to data.                                                                                                                                                 |
| Automate Capturing Vulnerability Data into corporate processes                         | Blueprint of example code customers can customize to enhance their internal automation "API-First" strategy.                                                                                 |
| Automate Distribution of Vulnerability Data to Cloud Providers                         | Optional Distribution methods into cloud systems such as Amazon S3 Bucket                                                                                                                    |
| Automate Application Enhancements and Delivery                                         | Docker application instance for reliable CI/CD delivery of enhancements, as well as traditional host execution on Linux Platforms.                                                           |
| Provide Execution Flexibility, Work Load Management, Password Security                 | Blueprint for enterprise jobstream execution (Ex. Autosys), password vaults (Ex. Hashicorp), or simple command line execution from a Virtual Machine instance of Ubuntu running on a laptop. |
| Provide Continous Vulnerability Data Pipeline                                          | Blueprint for data transformation pipeline from Qualys to Enterprise Data Stores in various formats ( JSON, CSV, SQLite Database )                                                           |

## Roadmap
```
Capability                    | Target    | Description
----------                    | ------    | -----------
KnowledgeBase                 | June 2021 | Automate download and transform of KnowledgeBase into CSV, JSON and SQLite Database
Host List                     | June 2021 | Automate download and transform of Host List into CSV, JSON and SQLite Database
Host List Detection           | June 2021 | Automate download and transform of Host List Detection into CSV, JSON and SQLite Database
Python Virtual Env            | June 2021 | Encapsulate qetl Application into Python Virtual Environment at installation.
Asset Inventory(CSAM)         | Oct 2021  | Automate download and transform of GAV/CSAM V2 API into CSV, JSON and SQLite Database
Performance Enhancements      | Jan 2022  | Begin 0.7.x series with performance enhancements.  See change log for details.
Asset Inventory(CSAM)         | Aug 2022  | CSAM API Blog, Video, documentation updates for CSAM, additional edge cases for Qualys Maintenance Windows.
Host List ARS                 | Aug 2022  | Host List Asset Risk Score Added to QualysETL.
Host List Detection QDS       | Aug 2022  | Host List Detection Qualys Detection Score Added to QualysETL.
Web Application Scanning(WAS) | Dec 2022  | Begin 0.8.x series, including WAS Module and Distribution Option, data prepared for database loader.
Database Injection            | Aug 2023  | Methods to inject schema/data from QualysETL into your downstream databases. Ex. Azure Cosmos DB (PostgreSQL), Amazon RedShift, PostgreSQL Open Source, MySql Open Source, SnowFlake, Microsoft SQL Server.  Contact your Qualys TAM to schedule a call with David Gregory if you wish to use this feature. 
Visualization Use Case        | Aug 2023  | Use QualysETL to build your downstream databases for use with PowerBI, Tableau, Etc. Contact your Qualys TAM to schedule a call with David Gregory if you wish to use this feature. 
QWEB 10.23 Updates            | Aug 2023  | Delivered additional fields for Host List and Host List Detection. For details see:  See [QWEB 10.23 release notification for details](https://www.qualys.com/docs/release-notes/qualys-cloud-platform-10.23-api-release-notes.pdf) 
Web Application Scanning(WAS) | Aug 2023  | Updated timing in WAS for long running jobs.
Docker Image                  | Aug 2023  | Contact your TAM to schedule a call with David Gregory.  Encapsulate Python Application into distributable docker image for ease os operation and upgrade.
Web Application Scanning(WAS) | Sept 2023 | Blog and Final Updates to WAS Module. 
Policy Compliance             | Nov 2023  | Delayed to include PCRS. Automate download and transform of Policy Compliance Posture, Policy, Controls. 
Other Modules                 | 2024      | Container Security, FIM and other modules targeted for 2024 TBD.
```

## Technologies
Project tested with:
1. Ubuntu version: 22.04 
2. Redhat version: 8.x/9.x latest
3. SQLite3 version: 3.31.1
4. Python version: 3.8.5 
5. Qualys API: latest

## ETL Examples
- Create XML, JSON, CSV and SQLite3 Database Formats of Qualys Data.

### ETL Configuration 
- Configuration file: /opt/qetl/users/[quser]/qetl_home/config/etld_config_settings.yaml
- Ensure you set these configurations:
  - host_list_detection_concurrency_limit: 2   
     Set this to appropriate qualys concurrency limit value after 
     reviewing the [Qualys Limits Guide](https://www.qualys.com/docs/qualys-api-limits.pdf) 
     https://www.qualys.com/docs/qualys-api-limits.pdf with your TAM for Questions. 

```bash
(qetl_venv) qualysetl@ubuntu:~/.local/bin$ more /opt/qetl/users/qualysetl/qetl_home/config/etld_config_settings.yaml 

# This file is generated by qetl_manage_user only on first invocation.
# File generated by qetl_manage_user on: $DATE
#
# YAML File of available configuration options for Qualys API Calls and future options.
# Ensure you set these configurations:
#
#     1) host_list_detection_concurrency_limit: 2
#         - Set this to appropriate qualys concurrency limit value after reviewing the
#           [Qualys Limits Guide] https://www.qualys.com/docs/qualys-api-limits.pdf with your TAM for Questions.
#           Note: if you exceed the endpoints concurrency limit,
#                 the application will reset the concurrency limit to X-ConcurrencyLimit-Limit - 1
#
# kb_last_modified_after: 'default'                  # Leave at default.  Knowledgebase is auto-incremental
#                                                      to full knowledgebase.
# kb_export_dir: 'default'                           # Leave at default until future use is developed.
# kb_payload_option: 'default'                       # Leave at default until future use is developed.
# kb_distribution_csv_flag: True                     # True/False Populates qetl_home/data/knowledgebase_distribution_dir
# kb_distribution_csv_max_field_size: 1000000        # Maximum field size allowed in distribution_csv file
#
# host_list_vm_processed_after: 'default'            # Leave at default until future use is developed.
# host_list_payload_option: 'default'                # Leave at default until future use is developed.
# host_list_payload_option: {{'show_ars': '1', 'show_ars_factors': '1'}}  # Contact your TAM to enable TruRisk
# host_list_export_dir: 'default'                    # Leave at default until future use is developed.
# host_list_distribution_csv_flag: True              # True/False Populates qetl_home/data/host_list_distribution_dir
# host_list_distribution_csv_max_field_size: 1000000 # Maximum field size allowed in distribution_csv file

#
# host_list_detection_payload_option: 'default'      # Leave at default until future use is developed.
# host_list_detection_payload_option: {{'show_qds': '1', 'show_qds_factors': '1'}} # Contact your TAM to enable TruRisk.
# host_list_detection_export_dir: 'default'          # Leave at default until future use is developed.
# host_list_detection_vm_processed_after: 'default'  # Leave at default until future use is developed.
# host_list_detection_concurrency_limit: 2           # Reset based on your subscription api concurrency limits
# host_list_detection_multi_proc_batch_size: 1000    # Leave at 1000
# host_list_detection_distribution_csv_flag: True    # True/False Populates qetl_home/data/host_list_detection_distribution_dir
# host_list_detection_distribution_csv_max_field_size: 1000000 # Maximum field size allowed in distribution_csv file
#
# asset_inventory_payload_option: 'default'          # Leave at 'default' until future use is developed.
# asset_inventory_export_dir: 'default'              # Leave at 'default' until future use is developed.
# asset_inventory_asset_last_updated: 'default'      # Leave at 'default' until future use is developed.
# asset_inventory_distribution_csv_flag: True        # True/False Populates qetl_home/data/asset_inventory_distribution_dir
# asset_inventory_distribution_csv_max_field_size: 1000000 # Maximum field size allowed in distribution_csv file
#
# requests_module_tls_verify_status: True            # Recommend leaving at True to protect application against
#                                                      man-in-middle attacks. False will set Python3 requests module
#                                                      verify option to False and requests will accept any TLS
#                                                      certificate presented by the server, and will ignore hostname
#                                                      mismatches and/or expired certificates, which will make your
#                                                      application vulnerable to man-in-the-middle (MitM) attacks
#                                                      This option is useful for development testing only when you
#                                                      are behind a reverse proxy, ex. Data Loss Prevention solution,
#                                                      and you haven't installed the trusted certificates yet.

requests_module_tls_verify_status: True

kb_last_modified_after: 'default'
kb_export_dir: 'default'
kb_payload_option: 'default'
kb_distribution_csv_flag: True

host_list_vm_processed_after: 'default'
host_list_export_dir: 'default'
host_list_distribution_csv_flag: True

host_list_detection_payload_option: 'default'
host_list_detection_export_dir: 'default'
host_list_detection_vm_processed_after: 'default'
host_list_detection_concurrency_limit: 2
host_list_detection_multi_proc_batch_size: 1000
host_list_detection_distribution_csv_flag: True

asset_inventory_payload_option: 'default'
asset_inventory_export_dir: 'default'
asset_inventory_asset_last_updated: 'default'
asset_inventory_distribution_csv_flag: True

was_distribution_csv_flag: True
```

### ETL KnowledgeBase
KnowledgeBase ETL - Incremental Update to Knowledgebase.  CSV, JSON, SQLite are full knowledgebase.  XML is incremental.
   - note the knowledgebase will rebuild itself every 30-90 days to ensure gdbm is reorganized.
```bash
qetl_manage_user -u /opt/qetl/users/quser -e etl_knowledgebase 
```

### ETL Host List
Host List ETL - Download Host List based on date
  - if no date is used, Host List will auto increment from last run 
    ( max LAST_VULN_SCAN_DATETIME ) or if no sqlite database exists
    it download start incremental pull from utc minus 1 day. 
```bash
qetl_manage_user -u /opt/qetl/users/quser -e etl_host_list -d [YYYY-MM-DDThh:mm:ssZ]
```
   
See [Application Manager and Data](#application-manager-and-data) for location of your qetl_home directory.
   
### ETL Host List Detection
Host List Detection ETL - Includes KnowledgeBase and Host List so do not run ETL Host List or ETL KnowledgeBase while Host List Detection ETL is runnning..
  - if no date is used, The Host List Driver will auto increment from last run
      ( max LAST_VULN_SCAN_DATETIME ) or if no sqlite database exists
      it download start incremental pull from utc minus 1 day. 
```bash
qetl_manage_user -u /opt/qetl/users/quser -e etl_host_list_detection -d [YYYY-MM-DDThh:mm:ssZ]
```

### ETL Asset Inventory
Asset Inventory (GAV/CSAM API) ETL - Includes CyberSecurity Asset Inventory API (CSAM) or its subset Global Asset View API (GAV).
- if no date is used, The Asset Inventory will be pulled from UTC - one day. 
```bash
qetl_manage_user -u /opt/qetl/users/quser -e etl_asset_inventory -d [YYYY-MM-DDThh:mm:ssZ]
```

### ETL Web Application Scanning Data
Web Application Scanning (WAS API) ETL - Includes Web Applications, Web Application Findings and the Web Application Catalog.
```bash
qetl_manage_user -u /opt/qetl/users/quser -e etl_was -d [YYYY-MM-DDThh:mm:ssZ]
```

### ETL Test System
Test System ETL - Small system test to validate modules are all working.  
* log/test_system.log will contain all results.  

Executes Programs:
1. etl_knowledgebase - updates knowledgebase up to date. 
2. etl_host_list ( 75 hosts )
3. etl_host_list_detection ( 75 hosts )
4. etl_asset_inventory ( 900 hosts )
4. etl_was ( subset of applications )
```bash
qetl_manage_user -u /opt/qetl/users/quser -e etl_test_system
```

## Application Manager and Data

### qetl_manage_user application
- qetl_manage_user is your entry point to manage ETL of Qualys Data.

[![](https://user-images.githubusercontent.com/82658653/213870402-d5bf448f-9c2f-4c8a-b36b-54fce35818af.png)](https://user-images.githubusercontent.com/82658653/213870402-d5bf448f-9c2f-4c8a-b36b-54fce35818af.png)

### Host List Detection SQLite Database
- qetl_manage_user -u [userdir] -e etl_host_list_detection -d [datetime] - Resulting sqlite database ready for distribution.

[![](https://user-images.githubusercontent.com/82658653/120927089-a1bb9880-c6ad-11eb-8b83-98c3e7643473.png)](https://user-images.githubusercontent.com/82658653/120927089-a1bb9880-c6ad-11eb-8b83-98c3e7643473.png)


### Host List Detection SQLite Tables
- qetl_manage_user -u [userdir] -e etl_host_list_detection -d [datetime] - Resulting sqlite database ready for distribution.

[![](https://user-images.githubusercontent.com/82658653/190963226-dee51f36-7f32-492a-9cb6-5acb906e4d7d.png)](https://user-images.githubusercontent.com/82658653/190963226-dee51f36-7f32-492a-9cb6-5acb906e4d7d.png)

### Environment
   - Python virtual environment 
   - Managed by qetl_manage_user
   - Example options for qetl Home Directories:
       - Prod: /opt/qetl/users/[user_name]/qetl_home
       - Test: /usr/local/test/opt/qetl/users/[user_name]/qetl_home
       - Dev:  $HOME/opt/qetl/users/[user_name]/qetl_home
    
### Application Directories

| Path                                           | Description                                                                       |
|------------------------------------------------|-----------------------------------------------------------------------------------|
| opt/qetl/users/                                | Directory of All Users                                                            |
| opt/qetl/users/[user]/qetl_home                | Parent directory path for a user                                                  |
| [user]/qetl_home                               | User Home Directory                                                               |
| qetl_home/bin                                  | User bin directory for customer to host scripts they create.                      |
| qetl_home/cred                                 | Credentials Directory                                                             |
| qetl_home/cred/.etld_lib_credentials.yaml      | Credentials file in yaml format.                                                  |
| qetl_home/cred/.qualys_cookie                  | Cookie file used for Qualys session management.                                   |
| qetl_home/config                               | Application Options Configuration Directory                                       |
| qetl_home/config/etld_lib_config_settings.yaml | Application Options                                                               |
| qetl_home/log                                  | Logs - Directory of all run logs                                                  |
| qetl_home/log/kb.log                           | LOG KnowledgeBase Run Logs                                                        |
| qetl_home/log/host_list.log                    | LOG - Host List Run Logs                                                          |
| qetl_home/log/host_list_detection.log          | LOG - Host List Detection Run Logs                                                |
| qetl_home/log/asset_inventory.log              | LOG - GAV/CSAM Asset Inventory Run Logs                                           |
| qetl_home/log/was.log                          | LOG - Web Application Scanning(WAS) Run Logs                                      |
| qetl_home/data                                 | Application Data - Directory containing all csv, xml, json, sqlite database data. |
| qetl_home/data/kb_sqlite.db                    | Database - Cumulative Knowledgebase SQLite Database                               |
| qetl_home/data/host_list_sqlite.db             | Database - vm_last_processed Host List SQLite Database                            |
| qetl_home/data/host_list_detection_sqlite.db   | Database - vm_last_processed Host List Detection SQLite Database                  |
| qetl_home/data/asset_inventory_sqlite.db       | Database -lastScanDate Asset Inventory SQLite Database                            |
| qetl_home/data/was_sqlite.db                   | Database - WebApp lastScan.date SQLite Database                                   |
| qetl_home/data/knowledgebase_extract_dir       | Extract - latest *.json.gz, *.xml.gz files                                        |
| qetl_home/data/host_list_extract_dir           | Extract - latest *.json.gz, *.xml.gz files                                        |
| qetl_home/data/host_list_detection_extract_dir | Extract - vm_last_processed Host List Detection XML Data Dir                      |
| qetl_home/data/asset_inventory_extract_dir     | Extract - Asset Inventory Extracts of last scan date of asset in JSON Format.     |
| qetl_home/data/was_extract_dir                 | Extract - Web Application Scanning (WAS) JSON Data Dir                            |
| qetl_home/data/knowledgebase_distribution_dir       | Distribution - latest *.csv.gz files if option set in etld_config.settings.yaml   |
| qetl_home/data/host_list_distribution_dir           | Distribution - latest *.csv.gz files if option set in etld_config.settings.yaml   |
| qetl_home/data/host_list_detection_distribution_dir | Distribution - latest *.csv.gz files if option set in etld_config.settings.yaml   |
| qetl_home/data/asset_inventory_distribution_dir     | Distribution - latest *.csv.gz files if option set in etld_config.settings.yaml   |
| qetl_home/data/was_distribution_dir                 | Distribution - latest *.csv.gz files if option set in etld_config.settings.yaml   |


### Data Formats 
Data Formats created in qetl_home/data:

| Format          | Description                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| JSON            | [Java Script Object Notation](https://datatracker.ietf.org/doc/html/rfc7159) useful for transfer of data between systems                                                                                                                                                                                                                                                                      |
| CSV             | [Comma Separated Values](https://datatracker.ietf.org/doc/html/rfc4180) useful for transfer of data between systems<br>Formatted to help import data into various BI or Database Tools:  Excel, Apache Open Office, Libre Office, Tableau, Microsoft PowerBI, SQL Database Loader                                                                                                             |
| XML             | [Extensible Markup Language](https://datatracker.ietf.org/doc/html/rfc3470) useful for transfer of data between systems                                                                                                                                                                                                                                                                       |
| SQLite Database | [SQLite Database](https://www.sqlite.org/about.html): SQLite Database populated with Qualys Data, Useful as a self-contained SQL Database of Qualys Data for Analysis, Useful as an intermediary transformation into your overall Enterprise ETL Process, SQLite is an in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine |


### Logging

Logging fields are pipe delimited with some formatting for raw readability.  You can easily import this data into excel, 
 a database for analysis or link this data to a monitoring system.

| Format                      | Description                                                                                                                              |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| YYYY-MM-DD hh:mm:ss,ms      | UTC Date and Time.  UTC is used to match internal date and time within Qualys data.                                                      |
| Logging Level               | INFO, ERROR, WARNING, etc.  Logging levels can be used for troubleshooting or remote monitoring for ERROR/WARNING log entries.           |
| Module Name: YYYYMMDDHHMMSS | Top Level qetl Application Module Name that is executing, along with date to uniquely identify all log entries associated with that job. |
| User Name                   | Operating System User executing this application.                                                                                        |
| Function Name               | qetl Application Function Executing.                                                                                                     |
| Message                     | qetl Application Messages describing actions, providing data.                                                                            |


See [Application Directories](#application-directories) for details of each log file.
```bash
cd qetl_home/log
head -3 kb.log
(qetl_venv) qualysetl@ubuntu:/opt/qetl/qetl_venv/bin$ cat /opt/qetl/users/qualys_user/qetl_home/log/kb.log | nl 
     1	2021-05-28 01:26:03,836 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_logging_stdout                | LOGGING SUCCESSFULLY SETUP FOR STREAMING
     2	2021-05-28 01:26:03,836 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_logging_stdout                | PROGRAM: ['/home/dgregory/opt/qetl/qetl_venv/bin/qetl_manage_user', '-u', '/opt/qetl/users/qualys_user', '-e', 'etl_knowledgebase']
     3	2021-05-28 01:26:03,897 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | check_python_version                | Python version found is: ['3.8.5 (default, Jan 27 2021, 15:41:15) ', '[GCC 9.3.0]']
     4	2021-05-28 01:26:03,897 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | get_sqlite_version                  | SQLite version found is: 3.31.1.
     5	2021-05-28 01:26:03,898 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | set_qetl_code_dir                   | parent qetl code dir - /home/dgregory/opt/qetl/qetl_venv/lib/python3.8/site-packages
```

### Application Monitoring
- To monitor the application for issues, the logging format includes a logging level.  
- Monitoring for ERROR will help identify issues and tend to the overall health of the applicaiton operation.

## Securing Your Application in the Data Center
Follow your corporate procedures for securing your application.  A key recommendation is to use a password vault
or remote invocation method that passes the credentials at run time so the password isn't stored on the system.

### Password Vault
QualysETL provides options to inject credentials at runtime via qetl_manage_user, so your credentials are not stored on disk.  
qetl_manage_user options to inject credentials at runtime are:
1) -p, --prompt-credentials prompt user for credentials, also accepts stdin with credentials piped to program.
2) -m, --memory-credentials get credentials from environment: q_username, q_password, q_api_fqdn_server
3) -s, --stdin-credentials  send credentials in json to stdin. 
         Example:
         {"q_username": "your userid", "q_password": "your password", "q_api_fqdn_server": "api fqdn", "q_gateway_fqdn_server": "gateway api fqdn"}

Qualys recommends customers move to a password vault of their choosing to operate this applications credentials.
By creating functions to obtain credentials from your corporations password vault, you can improve 
the security of your application by separating the password from the machine, injecting the credentials at runtime.  

One way customers can do this is through a work load management solution, where the external work load management
system ( Ex. Autosys ) schedules jobs injecting the required credentials to QualysETL application at runtime.  This eliminates
the need to store credentials locally on your system.

If you are unfamiliar with password vaults, here is one example from Hashicorp.
- [Hashicorp Products Vault](https://www.hashicorp.com/products/vault)
- [Hashicorp Getting Started](https://learn.hashicorp.com/tutorials/vault/getting-started-intro?in=vault/getting-started)

## Example Run Logs

### Uninstall and Install qetl

#### Uninstall Run Log

- Make sure you are not in your Python Virtual Environment when running uninstall.  
  Notice the command prompt does not include (qetl_env).  That means you have deactivated the Python3 Virtual Environment

```bash
(qetl_venv) qualysetl@ubuntu:~$ deactivate

qualysetl@ubuntu:~/.local/bin$ python3 -m pip uninstall qualysetl
Found existing installation: qualysetl 0.6.30
Uninstalling qualysetl-0.6.30:
  Would remove:
    /home/dgregory/.local/bin/qetl_setup_python_venv
    /home/dgregory/.local/lib/python3.8/site-packages/qualys_etl/*
    /home/dgregory/.local/lib/python3.8/site-packages/qualysetl-0.6.30.dist-info/*
Proceed (y/n)? y
  Successfully uninstalled qualysetl-0.6.30
qualysetl@ubuntu:~/.local/bin$ 

```

#### Install

- Make sure you are not in your Python Virtual Environment when installing this software.  
  Notice the command prompt does not include (qetl_env).

```bash
(qetl_env) qualysetl@ubuntu:~$ deactivate
qualysetl@ubuntu:~$ python3 -m pip install qualysetl
Collecting qualysetl
  Downloading qualysetl-0.6.30-py3-none-any.whl (79 kB)
     |████████████████████████████████| 79 kB 1.8 MB/s 
Installing collected packages: qualysetl
Successfully installed qualysetl-0.6.30
qualysetl@ubuntu:~$ 
```

### qetl_setup_python_env

```bash
qualysetl@ubuntu:~/.local/bin$ ./qetl_setup_python_venv /opt/qetl
Start qetl_setup_python_venv - Fri Jan 21 07:07:22 PST 2022
  1) test_os_for_required_commands
  2) test_for_pip_connectivity
  3) prepare_opt_qetl_env_dirs

    usage:       qetl_setup_python_venv [/opt/qetl] [test|prod] [version number]
                 qetl_setup_python_venv [-h] for help

    description:

        Create a python3 virtual environment and install the qualysetl
        application into that environment for usage.  This isolates the
        qualysetl application dependencies to the python3 virtual environment.
        See https://pypi.org/project/qualysetl/ for first time setup and
        installation instructions.

    options:

        qetl_setup_python_venv [/opt/qetl] [test|prod] [version number]

        1) [/opt/qetl]        - root directory where application and data
                                will be stored.
                              - You must be root to create this directory.
                              - See https://pypi.org/project/qualysetl/ for
                                first time setup/installation instructions.
        2) [test|prod]        - obtain QualysETL from test or prod pypi
                                instance.
        3) [version number]   - obtain version number of qualysetl.


    examples:
            1) qetl_setup_python_venv /opt/qetl
               - Ensure you have /opt/qetl directory created before running
                 this program.
               - Creates QualysETL Environment.  See directory information
                 below.

            2) qetl_setup_python_venv /opt/qetl prod 0.6.131
               - will install version 0.6.131 of qualysetl from pypi.org into
                 your /opt/qetl/qetl_venv directory.

            3) qetl_setup_python_venv /opt/qetl test 0.6.131
               - will install version 0.6.131 of qualysetl from test.pypi.org
                 into your /opt/qetl/qetl_venv directory.

    directory information:
             /opt/qetl            - root directory for Application and Data
             /opt/qetl/qetl_venv  - application directory for Qualys ETL
                                    Python Virtual Environment
             /opt/qetl/users      - data directory containing results of
                                    QualysETL execution.

    files:
        See https://dg-cafe.github.io/qualysetl/#application-manager-and-data


    container notes:

            1) For container deployment, ex docker, application and data
               are separated for container deployment.

               Container Application - /opt/qetl/qetl_venv should installed into the container image.
               Persistent Data       - /opt/qetl/users should be mapped to the underlying host
                                       system for persistent storage of application data.


Create qetl Python Environment? /opt/qetl/qetl_venv prod:latest
Do you want to create your python3 virtual environment for qetl? ( yes or no ) yes

ok, creating python3 virtual /opt/qetl/qetl_venv


  4) create_qetl_python_venv - will run for about 1-2 minutes

     1	    Package         Version  
     2	    --------------- ---------
     3	    boto3           1.17.97  
     4	    botocore        1.20.97  
     5	    certifi         2021.5.30
     6	    chardet         4.0.0    
     7	    idna            2.10     
     8	    jmespath        0.10.0   
     9	    oschmod         0.3.12   
    10	    pip             20.0.2   
    11	    pkg-resources   0.0.0    
    12	    python-dateutil 2.8.1    
    13	    PyYAML          5.4.1    
    14	    qualysetl       0.6.35   
    15	    requests        2.25.1   
    16	    s3transfer      0.4.2    
    17	    setuptools      57.0.0   
    18	    six             1.16.0   
    19	    urllib3         1.26.5   
    20	    wheel           0.36.2   
    21	    xmltodict       0.12.0   


     1	    Name: qualysetl
     2	    Version: 0.6.35
     3	    Summary: Qualys API Best Practices Series - ETL Blueprint Example Code within Python Virtual Environment
     4	    Home-page: https://dg-cafe.github.io/qualysetl/
     5	    Author: David Gregory
     6	    Author-email: dgregory@qualys.com, dave@davidgregory.com
     7	    License: Apache
     8	    Location: /opt/qetl/qetl_venv/lib/python3.8/site-packages
     9	    Requires: 
    10	    Required-by: 

   Success! Your python virtual environment for qetl is: /opt/qetl/qetl_venv

   Your python3 venv separates your base python installation from the qetl python requirements
   and is your entry to executing the qetl_manage_user application.  Your base qetl installation has
   moved to your python virtual environment: /opt/qetl/qetl_venv

   !!! save these commands as they are your entry to run the qetl application
   
       1) source /opt/qetl/qetl_venv/bin/activate
       2) /opt/qetl/qetl_venv/bin/qetl_manage_user ( Your entry point to operating qualysetl ) 

   Next steps:

    Enter your python3 virtual environment and begin testing qualys connectivity.

       1) source /opt/qetl/qetl_venv/bin/activate
       2) /opt/qetl/qetl_venv/bin/qetl_manage_user

End   qetl_setup_python_venv - Thu 17 Jun 2021 08:40:04 PM PDT
qualysetl@ubuntu:~/.local/bin$
```
### qetl_manage_user
You can execute qetl_manage_user to see options available.  To operate the qetl_manage_user
application you'll first enter the python3 virtual environment, then execute qetl_manage_user.

```bash
(qetl_venv) qualysetl@ubuntu:~/.local/bin$ qetl_manage_user 
    
    usage: qetl_manage_user [-h] [-u qetl_USER_HOME_DIR] [-e etl_[module] ] [-e validate_etl_[module] ] [-c] [-t] [-i] [-d] [-r] [-l]
    
    Command to Extract, Transform and Load Qualys Data into various forms ( CSV, JSON, SQLITE3 DATABASE )
    
    optional arguments:
      -h, --help                show this help message and exit
      -u Home Directory Path,   --qetl_user_home_dir Home directory Path
                                   Example:
                                   - /opt/qetl/users/q_username
      -e etl_[module],          --execute_etl_[module] execute etl of module name. valid options are:
                                       -e etl_knowledgebase 
                                       -e etl_host_list 
                                       -e etl_host_list_detection
                                       -e etl_asset_inventory
                                       -e etl_was
                                       -e etl_test_system ( for a small system test of all ETL Jobs )
      -e validate_etl_[module], --validate_etl_[module] [test last run of etl_[module]].  valid options are:
                                       -e validate_etl_knowledgebase
                                       -e validate_etl_host_list 
                                       -e validate_etl_host_list_detection
                                       -e validate_etl_asset_inventory
                                       -e validate_etl_was
                                       -e validate_etl_test_system 
      -d YYMMDDThh:mm:ssZ,      --datetime      YYYY-MM-DDThh:mm:ssZ UTC. Get All Data On or After Date. 
                                                Ex. 1970-01-01T00:00:00Z acts as flag to obtain all data.
      -c, --credentials        update qualys api user credentials: qualys username, password or api_fqdn_server
      -t, --test               test qualys credentials
      -i, --initialize_user    For automation, create a /opt/qetl/users/[userhome] directory 
                               without being prompted.
      -l, --logs               detailed logs sent to stdout for testing qualys credentials
      -v, --version            Help and QualysETL version information.
      -r, --report             brief report of the users directory structure.
      -p, --prompt-credentials prompt user for credentials, also accepts stdin with credentials piped to program.
      -m, --memory-credentials get credentials from environment: 
                               Example: q_username="your userid", q_password=your password, q_api_fqdn_server=api fqdn, q_gateway_fqdn_server=gateway api fqdn
      -s, --stdin-credentials  send credentials in json to stdin. 
                               Example:
                               {"q_username": "your userid", "q_password": "your password", "q_api_fqdn_server": "api fqdn", "q_gateway_fqdn_server": "gateway api fqdn"}
      
      etld_config_settings.yaml notes:
         1. To Enable CSV Distribution, add the following keys to etld_config_settings.yaml and toggle on/off them via True or False
              kb_distribution_csv_flag: True                    # populates qetl_home/data/knowledgebase_distribution_dir
              host_list_distribution_csv_flag: True             # populates qetl_home/data/host_list_distribution_dir
              host_list_detection_distribution_csv_flag: True   # populates qetl_home/data/host_list_detection_distribution_dir
              asset_inventory_distribution_csv_flag: True       # populates qetl_home/data/asset_inventory_distribution_dir
              was_distribution_csv_flag: True                   # populates qetl_home/data/was_distribution_dir
              
              These files are prepared for database load, tested with mysql.  No headers are present.  
              Contact your Qualys TAM and schedule a call with David Gregory if you need assistance with this option.
            
```

### qetl_manage_user Add User
To add a new user, execute qetl_manage_user -u [opt/users/your_new_user].  See example run log below.

```bash
qualysetl@ubuntu:~$ source /opt/qetl/qetl_venv/bin/activate
(qetl_venv) qualysetl@ubuntu:~$ qetl_manage_user

        
    
Please enter -u [ your /opt/qetl/users/ user home directory path ]
    Note: /opt/qetl/users/newuser is the root directory for your qetl userhome directory, 
         enter a new path including the opt/qetl/users/newuser 
         in the path you have authorization to write to.
         the prefix to your user directory opt/qetl/users is required.
         Example:
            1) /opt/qetl/users/newuser

        
        usage: qetl_manage_user [-h] [-u QETL_USER_HOME_DIR] [-e EXECUTE_ETL_MODULE] [-d DATETIME] [-c] [-t] [-l] [-p] [-s] [-m] [-r]
        
        Command to Extract, Transform and Load Qualys Data into various forms ( CSV, JSON, SQLITE3 DATABASE )
        
        optional arguments:
          -h, --help            show this help message and exit
          -u QETL_USER_HOME_DIR, --qetl_user_home_dir QETL_USER_HOME_DIR
                                Please enter -u option
          -e EXECUTE_ETL_MODULE, --execute_etl_module EXECUTE_ETL_MODULE
                                Execute etl_knowledgebase, etl_host_list, etl_host_list_detection, etl_asset_inventory, etl_test_system
          -d DATETIME, --datetime DATETIME
                                YYYY-MM-DDThh:mm:ssZ UTC. Get All Data On or After Date. Ex. 1970-01-01T00:00:00Z acts as flag to obtain all data.
          -c, --credentials     update qualys api user credentials stored on disk: qualys username, password or api_fqdn_server
          -t, --test            test qualys credentials
          -l, --logs            detailed logs sent to stdout for test qualys credentials
          -p, --prompt_credentials
                                prompt user for credentials
          -s, --stdin_credentials
                                read stdin credentials json {"q_username":"your userid", "q_password":"your password", "q_api_fqdn_server":"api fqdn", "q_gateway_fqdn_server":"gateway api fqdn"}
          -m, --memory_credentials
                                Get credentials from environment variables in memory: q_username, q_password, q_api_fqdn_server, and optionally add q_gateway_fqdn_server. Ex. export q_username=myuser
          -r, --report          Brief report of the users directory structure.

     
    
(qetl_venv) qualysetl@ubuntu:~$ qetl_manage_user -u /opt/qetl/users/qqusr_dt4

qetl_user_home_dir does not exist: /opt/qetl/users/qqusr_dt4/qetl_home
Create new qetl_user_home_dir? /opt/qetl/users/qqusr_dt4/qetl_home ( yes or no ): yes

qetl_user_home_dir created: /opt/qetl/users/qqusr_dt4/qetl_home


Current username: initialuser in config: /opt/qetl/users/qqusr_dt4/qetl_home/cred/.etld_cred.yaml
Update Qualys username? ( yes or no ): yes
Enter new Qualys username: qqusr_dt4
Current api_fqdn_server: qualysapi.qualys.com
Update api_fqdn_server? ( yes or no ): no
Update password for username: qqusr_dt4
Update password? ( yes or no ): yes
Enter your Qualys password:
You have updated your credentials.
  Qualys Username: qqusr_dt4
  Qualys api_fqdn_server: qualysapi.qualys.com


Would you like to test login/logout of Qualys? ( yes or no ): yes

Qualys Login Test for qqusr_dt4 at api_fqdn_server: qualysapi.qualys.com

Testing Qualys Login for qqusr_dt4 Succeeded at qualysapi.qualys.com
    with HTTPS Return Code: 200.

Thank you, exiting.

(qetl_venv) qualysetl@ubuntu:~/opt/qetl/qetl_venv/bin$ 
```

### qetl_manage_user ETL KnowledgeBase

```bash
(qetl_venv) qualysetl@ubuntu:~/opt/qetl/qetl_venv/bin$ qetl_manage_user -u /opt/qetl/users/qualys_user -e etl_knowledgebase
Starting etl_knowledgebase.  For progress see your /opt/qetl/users/qualys_user/qetl_home log directory
End      etl_knowledgebase.  For progress see your /opt/qetl/users/qualys_user/qetl_home log directory

(qetl_venv) qualysetl@ubuntu:~/opt/qetl/qetl_venv/bin$ cat /opt/qetl/users/qualys_user/qetl_home/log/kb.log | nl 
     1	2021-05-28 01:26:03,836 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_logging_stdout                | LOGGING SUCCESSFULLY SETUP FOR STREAMING
     2	2021-05-28 01:26:03,836 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_logging_stdout                | PROGRAM: ['/home/dgregory/opt/qetl/qetl_venv/bin/qetl_manage_user', '-u', '/opt/qetl/users/qualys_user', '-e', 'etl_knowledgebase: 20210528012603']
     3	2021-05-28 01:26:03,897 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | check_python_version                | Python version found is: ['3.8.5 (default, Jan 27 2021, 15:41:15) ', '[GCC 9.3.0]']
     4	2021-05-28 01:26:03,897 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | get_sqlite_version                  | SQLite version found is: 3.31.1.
     5	2021-05-28 01:26:03,898 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | set_qetl_code_dir                   | parent qetl code dir - /home/dgregory/opt/qetl/qetl_venv/lib/python3.8/site-packages
     6	2021-05-28 01:26:03,898 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | set_qetl_code_dir                   | child qetl code dir  - /home/dgregory/opt/qetl/qetl_venv/lib/python3.8/site-packages/qualys_etl
     7	2021-05-28 01:26:03,898 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | set_qetl_code_dir                   | etld_lib              - /home/dgregory/opt/qetl/qetl_venv/lib/python3.8/site-packages/qualys_etl/etld_lib
     8	2021-05-28 01:26:03,898 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | set_qetl_code_dir                   | etld_templates        - /home/dgregory/opt/qetl/qetl_venv/lib/python3.8/site-packages/qualys_etl/etld_templates
     9	2021-05-28 01:26:03,898 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | set_qetl_code_dir                   | etld_knowledgebase    - /home/dgregory/opt/qetl/qetl_venv/lib/python3.8/site-packages/qualys_etl/etld_knowledgebase
    10	2021-05-28 01:26:03,898 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | set_qetl_code_dir                   | etld_host_list        - /home/dgregory/opt/qetl/qetl_venv/lib/python3.8/site-packages/qualys_etl/etld_host_list
    11	2021-05-28 01:26:03,900 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_user_home_directories         | parent user app dir  - /opt/qetl/users/qualys_user
    12	2021-05-28 01:26:03,900 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_user_home_directories         | user home directory  - /opt/qetl/users/qualys_user/qetl_home
    13	2021-05-28 01:26:03,900 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_user_home_directories         | qetl_user_root_dir   - User root dir       - /opt/qetl/users
    14	2021-05-28 01:26:03,900 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_user_home_directories         | qetl_user_home_dir   - qualys user         - /opt/qetl/users/qualys_user/qetl_home
    15	2021-05-28 01:26:03,900 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_user_home_directories         | qetl_user_data_dir   - xml,json,csv,sqlite - /opt/qetl/users/qualys_user/qetl_home/data
    16	2021-05-28 01:26:03,900 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_user_home_directories         | qetl_user_log_dir    - log files           - /opt/qetl/users/qualys_user/qetl_home/log
    17	2021-05-28 01:26:03,900 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_user_home_directories         | qetl_user_config_dir - yaml configuration  - /opt/qetl/users/qualys_user/qetl_home/config
    18	2021-05-28 01:26:03,900 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_user_home_directories         | qetl_user_cred_dir   - yaml credentials    - /opt/qetl/users/qualys_user/qetl_home/cred
    19	2021-05-28 01:26:03,900 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_user_home_directories         | qetl_user_bin_dir    - etl scripts         - /opt/qetl/users/qualys_user/qetl_home/bin
    20	2021-05-28 01:26:03,902 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | load_etld_lib_config_settings_yaml       | etld_config_settings.yaml - kb_last_modified_after: default 
    21	2021-05-28 01:26:03,902 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | load_etld_lib_config_settings_yaml       | etld_config_settings.yaml - kb_export_dir: default 
    22	2021-05-28 01:26:03,902 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | load_etld_lib_config_settings_yaml       | etld_config_settings.yaml - host_list_vm_processed_after: default 
    23	2021-05-28 01:26:03,902 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | load_etld_lib_config_settings_yaml       | etld_config_settings.yaml - host_list_payload_option: notags 
    24	2021-05-28 01:26:03,902 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_kb_vars                       | knowledgeBase config - /opt/qetl/users/qualys_user/qetl_home/config/etld_config_settings.yaml
    25	2021-05-28 01:26:03,902 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_kb_vars                       | kb_export_dir is direct from yaml
    26	2021-05-28 01:26:03,902 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_kb_vars                       | kb_last_modified_after utc.now minus 7 days - 2021-05-21T00:00:00Z
    27	2021-05-28 01:26:03,902 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_host_list_vars                | host list config - /opt/qetl/users/qualys_user/qetl_home/config/etld_config_settings.yaml
    28	2021-05-28 01:26:03,902 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_host_list_vars                | host_list_vm_processed_after utc.now minus 7 days - 2021-05-27T00:00:00Z
    29	2021-05-28 01:26:03,902 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | setup_host_list_vars                | host_list_payload_option yaml - notags
    30	2021-05-28 01:26:03,906 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | spawn_etl_in_background                             | Job PID 247944 kb_etl_workflow job running in background.
    31	2021-05-28 01:26:03,907 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_start_wrapper                    | __start__ kb_etl_workflow ['/home/dgregory/opt/qetl/qetl_venv/bin/qetl_manage_user', '-u', '/opt/qetl/users/qualys_user', '-e', 'etl_knowledgebase: 20210528012603']
    32	2021-05-28 01:26:03,907 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_start_wrapper                    | data directory: /opt/qetl/users/qualys_user/qetl_home/data
    33	2021-05-28 01:26:03,907 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_start_wrapper                    | config file:    /opt/qetl/users/qualys_user/qetl_home/config/etld_config_settings.yaml
    34	2021-05-28 01:26:03,907 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_start_wrapper                    | cred yaml file: /opt/qetl/users/qualys_user/qetl_home/cred/.etld_cred.yaml
    35	2021-05-28 01:26:03,907 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_start_wrapper                    | cookie file:    /opt/qetl/users/qualys_user/qetl_home/cred/.etld_cookie
    36	2021-05-28 01:26:03,907 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_extract_wrapper                  | start knowledgebase_extract xml from qualys with kb_last_modified_after=2021-05-21T00:00:00Z
    37	2021-05-28 01:26:03,907 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | knowledgebase_extract                          | start
    38	2021-05-28 01:26:03,909 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | get_cred                            | Found your subscription credentials file:  /opt/qetl/users/qualys_user/qetl_home/cred/.etld_cred.yaml
    39	2021-05-28 01:26:03,909 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | get_cred                            |      username:         quays93
    40	2021-05-28 01:26:03,909 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | get_cred                            |      api_fqdn_server:  qualysapi.qg2.apps.qualys.com
    41	2021-05-28 01:26:03,909 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | get_cred                            |  ** Warning: Ensure Credential File permissions are correct for your company.
    42	2021-05-28 01:26:03,909 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | get_cred                            |  ** Warning: Credentials File: /opt/qetl/users/qualys_user/qetl_home/cred/.etld_cred.yaml
    43	2021-05-28 01:26:03,909 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | get_cred                            |  ** Permissions are: -rw------- for /opt/qetl/users/qualys_user/qetl_home/cred/.etld_cred.yaml
    44	2021-05-28 01:26:03,909 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | knowledgebase_extract                          | api call    - https://qualysapi.qg2.apps.qualys.com/api/2.0/fo/knowledge_base/vuln/
    45	2021-05-28 01:26:03,909 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | knowledgebase_extract                          | api options - {'action': 'list', 'details': 'All', 'show_disabled_flag': '1', 'show_qid_change_log': '1', 'show_supported_modules_info': '1', 'show_pci_reasons': '1', 'last_modified_after': '2021-05-21T00:00:00Z'}
    46	2021-05-28 01:26:03,909 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | knowledgebase_extract                          | cookie      - False
    47	2021-05-28 01:26:05,717 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_file_info                       | input file - https://qualysapi.qg2.apps.qualys.com/api/2.0/fo/knowledge_base/vuln/ size:  change time: 
    48	2021-05-28 01:26:05,718 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_file_info                       | output file - /opt/qetl/users/qualys_user/qetl_home/data/kb.xml size: 728.51 kilobytes change time: 2021-05-27 21:26:05 local timezone
    49	2021-05-28 01:26:05,718 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | knowledgebase_extract                          | end
    50	2021-05-28 01:26:05,718 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_extract_wrapper                  | end knowledgebase_extract xml from qualys
    51	2021-05-28 01:26:05,719 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_shelve_wrapper           | start kb_shelve xml to shelve
    52	2021-05-28 01:26:05,719 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_shelve_wrapper           | input file:  /opt/qetl/users/qualys_user/qetl_home/data/kb.xml
    53	2021-05-28 01:26:05,719 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_shelve_wrapper           | output file: /opt/qetl/users/qualys_user/qetl_home/data/kb_shelve
    54	2021-05-28 01:26:05,719 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_shelve                           | start
    55	2021-05-28 01:26:05,744 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_dbm_info                        | dbm etl_workflow_validation_type - dbm.gnu - /opt/qetl/users/qualys_user/qetl_home/data/kb_shelve
    56	2021-05-28 01:26:05,815 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_shelve                           | count qualys qid added to shelve: 137 for /opt/qetl/users/qualys_user/qetl_home/data/kb_shelve
    57	2021-05-28 01:26:05,815 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_file_info                       | input file - /opt/qetl/users/qualys_user/qetl_home/data/kb.xml size: 728.51 kilobytes change time: 2021-05-27 21:26:05 local timezone
    58	2021-05-28 01:26:05,815 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_dbm_info                        | dbm etl_workflow_validation_type - dbm.gnu - /opt/qetl/users/qualys_user/qetl_home/data/kb_shelve
    59	2021-05-28 01:26:05,815 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_file_info                       | output file - /opt/qetl/users/qualys_user/qetl_home/data/kb_shelve size: 632.00 kilobytes change time: 2021-05-27 21:26:05 local timezone
    60	2021-05-28 01:26:05,815 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_shelve                           | end
    61	2021-05-28 01:26:05,815 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_shelve_wrapper           | end   kb_shelve xml to shelve
    62	2021-05-28 01:26:05,815 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_json_wrapper                  | start kb_load_json transform Shelve to JSON
    63	2021-05-28 01:26:05,815 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_json_wrapper                  | input file:   /opt/qetl/users/qualys_user/qetl_home/data/kb_shelve
    64	2021-05-28 01:26:05,815 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_json_wrapper                  | output File:  /opt/qetl/users/qualys_user/qetl_home/data/kb.json
    65	2021-05-28 01:26:05,815 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_load_json                             | start
    66	2021-05-28 01:26:05,840 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_load_json                             | count qid loaded to json: 137
    67	2021-05-28 01:26:05,841 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_file_info                       | input file - /opt/qetl/users/qualys_user/qetl_home/data/kb_shelve size: 632.00 kilobytes change time: 2021-05-27 21:26:05 local timezone
    68	2021-05-28 01:26:05,841 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_dbm_info                        | dbm etl_workflow_validation_type - dbm.gnu - /opt/qetl/users/qualys_user/qetl_home/data/kb_shelve
    69	2021-05-28 01:26:05,841 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_file_info                       | output file - /opt/qetl/users/qualys_user/qetl_home/data/kb.json size: 645.81 kilobytes change time: 2021-05-27 21:26:05 local timezone
    70	2021-05-28 01:26:05,841 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_load_json                             | end
    71	2021-05-28 01:26:05,841 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_json_wrapper                  | end   kb_load_json transform Shelve to JSON
    72	2021-05-28 01:26:05,841 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_csv_wrapper                   | start kb_load_csv - shelve to csv
    73	2021-05-28 01:26:05,841 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_csv_wrapper                   | input file:   /opt/qetl/users/qualys_user/qetl_home/data/kb_shelve
    74	2021-05-28 01:26:05,841 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_csv_wrapper                   | output file: /opt/qetl/users/qualys_user/qetl_home/data/kb.csv
    75	2021-05-28 01:26:05,841 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_csv_wrapper                   | output file: /opt/qetl/users/qualys_user/qetl_home/data/kb_cve_qid_map.csv  cve -> qid map in csv format
    76	2021-05-28 01:26:05,841 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_create_csv_from_shelve           | start
    77	2021-05-28 01:26:05,864 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_create_csv_from_shelve           | count rows written to csv: 137
    78	2021-05-28 01:26:05,864 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_file_info                       | input file - /opt/qetl/users/qualys_user/qetl_home/data/kb_shelve size: 632.00 kilobytes change time: 2021-05-27 21:26:05 local timezone
    79	2021-05-28 01:26:05,864 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_dbm_info                        | dbm etl_workflow_validation_type - dbm.gnu - /opt/qetl/users/qualys_user/qetl_home/data/kb_shelve
    80	2021-05-28 01:26:05,864 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_file_info                       | output file - /opt/qetl/users/qualys_user/qetl_home/data/kb.csv size: 387.65 kilobytes change time: 2021-05-27 21:26:05 local timezone
    81	2021-05-28 01:26:05,864 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_create_csv_from_shelve           | end
    82	2021-05-28 01:26:05,867 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_create_cve_qid_shelve            | count rows written to cve to qid shelve: 334
    83	2021-05-28 01:26:05,868 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_file_info                       | input file - /opt/qetl/users/qualys_user/qetl_home/data/kb_shelve size: 632.00 kilobytes change time: 2021-05-27 21:26:05 local timezone
    84	2021-05-28 01:26:05,868 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_dbm_info                        | dbm etl_workflow_validation_type - dbm.gnu - /opt/qetl/users/qualys_user/qetl_home/data/kb_shelve
    85	2021-05-28 01:26:05,868 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_file_info                       | output file - /opt/qetl/users/qualys_user/qetl_home/data/kb_cve_qid_map_shelve size: 44.00 kilobytes change time: 2021-05-27 21:26:05 local timezone
    86	2021-05-28 01:26:05,868 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_csv_wrapper                   | end   kb_load_csv - shelve to csv
    87	2021-05-28 01:26:05,868 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_cve_qid_csv_wrapper           | start kb_load_cve_qid_csv transform Shelve to CSV
    88	2021-05-28 01:26:05,868 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_cve_qid_csv_wrapper           | input file:  /opt/qetl/users/qualys_user/qetl_home/data/kb_cve_qid_map_shelve
    89	2021-05-28 01:26:05,868 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_cve_qid_csv_wrapper           | output file: /opt/qetl/users/qualys_user/qetl_home/data/kb_cve_qid_map.csv
    90	2021-05-28 01:26:05,868 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_cve_qid_csv_report               | Start
    91	2021-05-28 01:26:05,869 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_cve_qid_csv_report               | Count of CVE rows written: 334
    92	2021-05-28 01:26:05,869 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_cve_qid_csv_report               | End
    93	2021-05-28 01:26:05,869 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_cve_qid_csv_wrapper           | end   kb_load_cve_qid_csv transform Shelve to CSV
    94	2021-05-28 01:26:05,869 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_sqlite_wrapper                | start kb_load_sqlite transform Shelve to Sqlite3 DB
    95	2021-05-28 01:26:05,869 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_sqlite_wrapper                | input file:   /opt/qetl/users/qualys_user/qetl_home/data/kb.csv
    96	2021-05-28 01:26:05,869 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_sqlite_wrapper                | output file: /opt/qetl/users/qualys_user/qetl_home/data/kb_load_sqlite.db
    97	2021-05-28 01:26:05,869 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_load_sqlite                           | start
    98	2021-05-28 01:26:05,884 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | bulk_insert_csv_file                | Count rows added to table: 137
    99	2021-05-28 01:26:05,884 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_file_info                       | input file - /opt/qetl/users/qualys_user/qetl_home/data/kb.csv size: 387.65 kilobytes change time: 2021-05-27 21:26:05 local timezone
   100	2021-05-28 01:26:05,884 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | log_file_info                       | output file - /opt/qetl/users/qualys_user/qetl_home/data/kb_load_sqlite.db size: 520.00 kilobytes change time: 2021-05-27 21:26:05 local timezone
   101	2021-05-28 01:26:05,884 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_load_sqlite                           | end
   102	2021-05-28 01:26:05,884 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_to_sqlite_wrapper                | end   kb_load_sqlite transform Shelve to Sqlite3 DB
   103	2021-05-28 01:26:05,884 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_distribution_wrapper             | start kb_distribution
   104	2021-05-28 01:26:05,884 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_dist                             | start
   105	2021-05-28 01:26:05,884 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | copy_results_to_external_target     | no actions taken.  etld_config_settings.yaml kb_export_dir set to: default
   106	2021-05-28 01:26:05,885 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_dist                             | end
   107	2021-05-28 01:26:05,885 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_distribution_wrapper             | end   kb_distribution
   108	2021-05-28 01:26:05,885 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_end_wrapper                      | runtime for kb_etl_workflow in seconds: 1.9780801669985522
   109	2021-05-28 01:26:05,885 | INFO     | etl_knowledgebase: 20210528012603    | dgregory        | kb_end_wrapper                      | __end__ kb_etl_workflow ['/home/dgregory/opt/qetl/qetl_venv/bin/qetl_manage_user', '-u', '/opt/qetl/users/qualys_user', '-e', 'etl_knowledgebase: 20210528012603']
```

### Review ETL KnowledgeBase Data

```bash
(qetl_venv) qualysetl@ubuntu:/opt/qetl/users/qualys_user/qetl_home/data$ cd /opt/qetl/users/qualys_user/qetl_home/data/
(qetl_venv) qualysetl@ubuntu:/opt/qetl/users/qualys_user/qetl_home/data$ ls kb_sqlite.db knowledgebase_extract_dir
     1	kb_sqlite.db
     2  kb_utc_run_datetime_2022-01-13T07:29:49Z_utc_last_modified_after_2021-12-14T00:00:00Z_batch_000001.json.gz  
     3  kb_utc_run_datetime_2022-01-13T07:29:49Z_utc_last_modified_after_2021-12-14T00:00:00Z_batch_000001.xml.gz

```

## License
[Apache License](http://www.apache.org/licenses/LICENSE-2.0)

    Copyright 2021  David Gregory and Qualys Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

## ChangeLog
Beginning with 0.6.98 a change log will be maintained here.

```
Version | Date of Change      | Description of Changes
------- | --------------      | ----------------------
0.6.98  | 2021-08-06 10:00 ET | minor update to order of python virtual env package install. Install Script: qetl_setup_python_venv
0.6.99  | 2021-08-06 11:30 ET | minor update, added module chardet.
0.6.100 | 2021-08-10 12:00 ET | minor documentation update.
0.6.101 | 2021-08-11 12:00 ET | minor update to asset_inventory gateway selection.
0.6.102 | 2021-08-13 12:00 ET | minor update to documentation.
0.6.103 | 2021-08-26 18:00 ET | minor update to allow host list detection to continue to run for up to 1 day.
0.6.104 | 2021-08-27 18:00 ET | update to address encoding error in complex data.
0.6.105 | 2021-09-09 12:00 ET | updated roadmap, and updated retry after receiving 409 (concurrency) or 202 (duplicate operation), sleep 2 min and retry.
0.6.106 | 2021-09-29 12:00 ET | Minor update to allow sqlite 3.26.
0.6.107 | 2021-09-29 20:00 ET | Minor update to adding ability to show tags in Host List.  If host_list_show_tags: '1' is added to etld_config_settings.yaml, then the host list will include qualys tags.
0.6.108 | 2021-10-01 20:00 ET | Updated documentation to include Red Hat 8.4 instructions.
0.6.109 | 2021-10-02 12:00 ET | Updated documentation to include Asset Inventory (GAV/CSAM V2) API.
0.6.112 | 2021-11-07 12:00 ET | Updated etl_asset_inventory to include new fields: criticality, businessInformation, assignedLocation, businessAppListData.  Updated retry and program max run time sanity checks.  Updated Asset Inventory Logging to include count of assets prior to executing download. Updated Host List to include cloud meta data. 
0.6.113 | 2021-11-16 12:00 ET | Updated file change sanity check to 20 min of inactivity.
0.6.117 | 2021-11-18 06:00 ET | Updated http wait time from 30 sec to 5 min. Added counters to asset inventory csv logging. Reverse Sort to add newest assets to shelve in asset_inventory_shelve without overwriting dups.
0.6.118 | 2021-11-18 06:00 ET | Updated performance reading shelve database in asset inventory process. Tested 1.5 Million hosts successfully.
0.6.119 | 2021-11-24 06:00 ET | Updated asset inventory features to include presenting JSON in csv cells instead of indexed list, as well as feature to not truncate data.  To enable these feature, edit your etld_config_settings.yaml to include 'asset_inventory_present_csv_cell_as_json: True' and edit your etld_config_settings.yaml to include: asset_inventory_csv_truncate_cell_limit: False
0.6.123 | 2021-12-01 19:00 ET | Part 1) Updated asset inventory features to include tables Q_Asset_Inventory_Software_Assetid (Asset ID to Software) and Q_Asset_Inventory_Software_Unique ( unique list of software and lifecycle info found in asset inventory ).  These tables are useful to create views of unique software, unique software -> server.
0.6.123 | 2021-12-01 19:00 ET | Part 2) Updated qetl_manage_user credential handling to support -p prompt for cred, -s accept json creds from stdin, -m accept creds exported to environment. 
0.6.124 | 2021-12-02 09:00 ET | Minor update to improve exception handling in extract 
0.6.126 | 2021-12-04 19:00 ET | Minor update to help and version options for qetl_manage_user 
0.6.130 | 2021-12-09 12:00 ET | Part 1) Added feature present JSON in csv cells to etl_knowledgebase, etl_host_list, etl_host_list_detection, etl_asset_inventory. To enable these feature, edit your etld_config_settings.yaml to include 'kb_present_csv_cell_as_json: True', 'host_list_present_csv_cell_as_json: True' 'host_list_detection_present_csv_cell_as_json: True', 'asset_inventory_present_csv_cell_as_json: True' 
0.6.130 | 2021-12-09 12:00 ET | Part 2) Added feature "no truncation" if truncate cell limit is 0 in etl_knowledgebase, etl_host_list, etl_host_list_detection, etl_asset_inventory. To enable this feature, edit your etld_config_settings.yaml to update: 'asset_inventory_csv_truncate_cell_limit: 0' 'kb_csv_truncate_cell_limit: 0' 'host_list_csv_truncate_cell_limit: 0' 'host_list_detection_csv_truncate_cell_limit: 0'.  
0.6.130 | 2021-12-09 12:00 ET | Part 3) Added feature to allow customers in development to set Python3 requests verify=False.  This setting is not recommended as it can result in a man-in-the-middle (MitM) attack.  To enable Python3 requests verify=False, edit your etld_config_settings.yaml and add the setting 'requests_module_tls_verify_status: False'.  Default is True. When set to False logging will include warning messages about insecurity of the setting.  We recommend repairing certificate chain instead of setting this option to False.  Defaults to True, requiring requests to verify the TLS certificate at the remote end. If verify is set to False, requests will accept any TLS certificate presented by the server, and will ignore hostname mismatches and/or expired certificates, which will make your application vulnerable to man-in-the-middle (MitM) attacks. Only set this to False for testing. 
0.6.130 | 2021-12-09 12:00 ET | Part 4) Minor updates to improve progress counters in logging, minor update to asset inventory logging to include batch number. 
0.6.131 | 2021-12-09 13:00 ET | Minor updates to formatting of ReadMe.
0.7.6 | 2022-01-12 16:00 ET | Begin 0.7.x series to include major update in performance and updates to db schemas.  See below for changes.  Please test before replacing 0.6.x series.
0.7.6 | 2022-01-12 16:00 ET | changes to 0.7.x series:  1) All extract data is loaded into their respective extract directories.  knowledgebase_extract_dir, host_list_extract_dir, host_list_detection_extract_dir, asset_inventory_extract_dir.  All files are gzip compressed.
0.7.6 | 2022-01-12 16:00 ET | changes to 0.7.x series:  2) CSV Files are no longer auto generated.  use sqlite3 -csv -header sqlite_file.db "select * from TABLE_NAME" > OUTPUTFILE.csv to generate your csv files post process.
0.7.6 | 2022-01-12 16:00 ET | changes to 0.7.x series:  3) All xml files are converted to json files in their respective extract directories.
0.7.6 | 2022-01-12 16:00 ET | changes to 0.7.x series:  4) host_list_detection_sqlite.db schema has been updated.  Please review tables to create the views of data you require.  Q_Host_List_Detection is now a view of Q_Host_List, Q_Host_List_Detection_HOSTS, and Q_Host_List_Detection_QIDS.  Each field in view Q_Host_List_Detection is prefixed with the source of their data ( HL_ = Q_Host_List, HLDH_ = Q_Host_List_Detection_Hosts, HLDQ_ = Q_Host_List_Detection_QIDS. host_list_detection_sqlite.db can be used to update a central database of all historical data post process. 
0.7.6 | 2022-01-12 16:00 ET | changes to 0.7.x series:  5) host_list_sqlite.db schema has been updated.  Please review tables to create the views of data you require.
0.7.6 | 2022-01-12 16:00 ET | changes to 0.7.x series:  6) kb_load_sqlite.db has been renamed kb_sqlite.db
0.7.6 | 2022-01-12 16:00 ET | changes to 0.7.x series:  7) kb_sqlite.db schema has been updated.  Please review tables to create the views of data you require.
0.7.6 | 2022-01-12 16:00 ET | changes to 0.7.x series:  8) asset_inventory_sqlite.db schema has been updated.  Please review tables to create the views of data you require.
0.7.6 | 2022-01-12 16:00 ET | changes to 0.7.x series:  9) -e etl_test_system will execute a sampling of all etl programs with the resulting log in log/test_system.log.  ERRORS in this log indicate an unhealthy system.
0.7.6 | 2022-01-12 16:00 ET | changes to 0.7.x series: 10) There is no csv cell truncation as all csv cells with nested data are now json objects instead of flat lists. 
0.7.6 | 2022-01-12 16:00 ET | changes to 0.7.x series: 11) A new CVE view of knowledgebase is available Q_KnowledgeBase_CVE_LIST.
0.7.7 | 2022-01-13 10:00 ET | Minor updates to test_system to get 75 hosts.
0.7.8 | 2022-01-13 15:00 ET | Minor updates to documenation prior to pypi.org launch.
0.7.9 | 2022-01-14 15:00 ET | Minor updates to documenation.
0.7.10 | 2022-01-15 02:00 ET | Update to asset inventory workflow to optimize data load.
0.7.11 | 2022-01-15 14:00 ET | Q_Knowledgebase_CVE_LIST view bug fix.
0.7.13 | 2022-01-20 19:00 ET | Update to allow for test or prod install of specific qualysetl version.  Also, improvements in exception processing across modules and preliminary work on WAS.
0.7.14 | 2022-01-21 09:00 ET | Updated etl_asset_inventory to ensure gzip compression is default.  Update documentation from Red Hat 8.4 to Red Hat 8.5 which is the current 8.x series of Red Hat.
0.7.15 | 2022-01-21 09:00 ET | Updated help documentation for qetl_setup_python_venv.
0.7.16 | 2022-02-09 15:00 ET | Updated etl_asset_inventory for GAV only customer processing.
0.7.17 | 2022-03-25 12:00 ET | Updated etl_asset_inventory enhancements to retry exception processing for malformed json and http error codes.
0.7.18 | 2022-03-25 12:00 ET | Updated Roadmap
0.7.19 | 2022-03-26 12:00 ET | Updated retry limits for etl_asset_inventory.
0.7.20 | 2022-03-27 15:00 ET | Updated etl_asset_inventory auth token refresh.
0.7.40 | 2022-08-02 18:00 ET | Updated etl_asset_inventory auth token refresh for edge case during maintenance window (http 503). Also, updated Road Map.
0.7.40 | 2022-08-02 18:00 ET | Updated http_conn_timeout default for all modules to address long running queries.
0.7.40 | 2022-08-02 18:00 ET | Updated Host List to include ASSET_RISK_SCORE, ASSET_CRITICALITY_SCORE, ARS_FACTORS.  Edit etld_config_settings.yaml to include: host_list_payload_option: {'show_ars': '1', 'show_ars_factors': '1'} to enable capturing data.  Your subscription must have ARS enabled.  Contact your TAM and dgregory@qualys.com if this option does not work for you.
0.7.40 | 2022-08-02 18:00 ET | Updated Host List Detection to include QDS, QDS_FACTORS  Edit etld_config_settings.yaml to include: host_list_detection_payload_option: {'show_qds': '1', 'show_qds_factors': '1'} to enable capturing data.  Your subscription must have ARS enabled.  Contact your TAM and dgregory@qualys.com if this option does not work for you.
0.7.41 | 2022-08-30 18:00 ET | Updated Host List Detection to enable host_list_detection_multi_proc_batch_size for values less than 2000 hosts.
0.7.42 | 2022-08-31 06:00 ET | Updated ulimit for open files to accomdate multiprocessing pipes in host list detection for large jobs.
0.7.44 | 2022-08-31 11:00 ET | Updated to ensure root user cannot install or execute qualysetl 
0.7.45 | 2022-08-31 21:00 ET | Documention Updates - Asset Inventory Schema Image along with removing old comments from etld_config_settings.yaml template.
0.7.46 | 2022-09-01 16:00 ET | Add ram, disk, swap, cpu info to logging at beginning of job.  
0.7.47 | 2022-09-02 09:00 ET | Add SYS stat for ram, disk, swap, cpu to logging throughout job run.  
0.7.48 | 2022-09-18 09:00 ET | GAV/CSAM Fields added to SQL Database - domainRole,riskScore,passiveSensor,domain,subdomain,whois,isp,asn.  
0.7.48 | 2022-09-18 09:00 ET | GAV/CSAM Documentation of Schema updated with additional fields added to SQL Database:  domainRole,riskScore,passiveSensor,domain,subdomain,whois,isp,asn
0.7.48 | 2022-09-18 09:00 ET | Host List Detection Documentation of Schema updated with additional fields added to SQL Database - Q_Host_List: ASSET_RISK_SCORE, ASSET_CRITICALITY_SCORE, ARS_FACTORS
0.7.48 | 2022-09-18 09:00 ET | Host List Detection Documentation of Schema updated with additional fields added to SQL Database - Q_Host_List_Detection_QIDS: QDS, QDS_FACTORS
0.7.49 | 2022-09-19 03:00 ET | Documentation Update minor.
0.7.50 | 2022-09-19 04:00 ET | Documentation Update minor.
0.7.51 | 2022-10-05 15:00 ET | Added update to counters in logs, added retest if gateway 401 encountered.
0.7.56 | 2022-11-04 05:00 ET | Added -e etl_was to qetl_manage_user options to extract WAS Applications, Findings and Catalog.
0.7.56 | 2022-11-04 05:00 ET | Updated STATUS_TABLE for all modules. STATUS_COUNT renamed LAST_BATCH_PROCESSED, STATUS_DETAILS json updated to include details of which etl workflow updated the table along with workflow log timestamp to correlate the logs with the database update.
0.7.56 | 2022-11-04 05:00 ET | Updated base64 routine to correct error when processing complex passwords.
0.8.00 | 2022-12-05 05:00 ET | Major update, be sure to test before going to production.
0.8.00 | 2022-12-05 05:00 ET | Updates:  1) qetl_manage_user -e etl_was has been added to provide you with Web Application Scanning data including WebApps, Findings and Catalog.
0.8.00 | 2022-12-05 05:00 ET | Updates:  2) qetl_manage_user -e validate_etl_[etl name] will scan etl_[etl_name] log for errors and report success or fail.
0.8.00 | 2022-12-05 05:00 ET | Updates:         - Example: qetl_manage_user -u /opt/qetl/users/youruser -e validate_etl_host_list_detection
0.8.00 | 2022-12-05 05:00 ET | Updates:         - Example: qetl_manage_user -u /opt/qetl/users/youruser -e validate_etl_asset_inventory
0.8.00 | 2022-12-05 05:00 ET | Updates:         - Example: qetl_manage_user -u /opt/qetl/users/youruser -e validate_etl_was
0.8.00 | 2022-12-05 05:00 ET | Updates:  3) qetl_manage_user -i -u /opt/qetl/users/[your new qetl user] will automatically initialize user directory without prompting.  This is useful when automating run of QualysETL on new systems/docker images as no prompts are provided.
0.8.00 | 2022-12-05 05:00 ET | Updates:         - Example: qetl_manage_user -i -u /opt/qetl/users/testuser will automatically create the -u directory structure without prompting.  
0.8.00 | 2022-12-05 05:00 ET | Updates:  4) distribution - when enabled, all tables from ETL are prepared for database load.
0.8.00 | 2022-12-05 05:00 ET | Updates:         Edit etld_config_settings.yaml adding the following keys:
0.8.00 | 2022-12-05 05:00 ET | Updates:         - kb_distribution_csv_flag: True
0.8.00 | 2022-12-05 05:00 ET | Updates:         - host_list_distribution_csv_flag: True
0.8.00 | 2022-12-05 05:00 ET | Updates:         - host_list_detection_distribution_csv_flag: True
0.8.00 | 2022-12-05 05:00 ET | Updates:         - asset_inventory_distribution_csv_flag: True
0.8.00 | 2022-12-05 05:00 ET | Updates:         - was_distribution_csv_flag: True
0.8.00 | 2022-12-05 05:00 ET | Updates:         Tested with the following MySQL options:
0.8.00 | 2022-12-05 05:00 ET | Updates:         -     Bash Script Example: 
0.8.00 | 2022-12-05 05:00 ET | Updates:         -         export TABLE_NAME=QETL.Q_KnowledgeBase
0.8.00 | 2022-12-05 05:00 ET | Updates:         -         zcat [Q_KnowledgeBase.*.csv.gz] | mysql -v -e "LOAD DATA LOCAL INFILE '/dev/stdin' INTO TABLE ${TABLE_NAME} CHARACTER SET UTF8 FIELDS TERMINATED BY ',' ESCAPED BY '\\\\' LINES TERMINATED BY '\\n';COMMIT;"
0.8.00 | 2022-12-05 05:00 ET | Updates:     The default max_size for each field in distribution is 1000000 characters. To adjust this to meet your database field limits, edit etld_config_settings.yaml and add the following key/value pairs for each etl you want to customize max_field size for in distribution files.
0.8.00 | 2022-12-05 05:00 ET | Updates:         - kb_distribution_csv_max_field_size: 2000000 
0.8.00 | 2022-12-05 05:00 ET | Updates:         - host_list_distribution_csv_max_field_size: 2000000
0.8.00 | 2022-12-05 05:00 ET | Updates:         - host_list_detection_distribution_csv_max_field_size: 2000000
0.8.00 | 2022-12-05 05:00 ET | Updates:         - asset_inventory_distribution_csv_max_field_size: 2000000
0.8.00 | 2022-12-05 05:00 ET | Updates:         - was_distribution_csv_max_field_size: 2000000
0.8.00 | 2022-12-05 05:00 ET | Updates:     For long running jobs etl_host_list_detection and etl_asset_inventory, these both generate distribution files through multiprocessing, so files are prepared for downstream ingestion as they are read from Qualys.
0.8.00 | 2022-12-05 05:00 ET | Updates:          - Use this feature to immediately begin streaming Qualys Data to your downstream system by inserting distribution files into your downstream system as each batch is created.
0.8.00 | 2022-12-05 05:00 ET | Updates:          - Each distribution file is the product of integrity testing and load to SQLite prior exporting to distribution batch file for downstream processing..
0.8.00 | 2022-12-05 05:00 ET | Updates:  5) BATCH_DATE, BATCH_NUMBER added to Q_Asset_Inventory for tracability back to original batch json data used for loading table
0.8.00 | 2022-12-05 05:00 ET | Updates:  6) BATCH_NUMBER should always be stored as a text field.
0.8.00 | 2022-12-05 05:00 ET | Updates:  7) Removed Q_Host_List_Detection view.  Table Views can be injected into database post process to meet customer requirements.
0.8.01 | 2022-12-06 05:00 ET | Minor Documentation Updates.
0.8.02 | 2022-12-06 05:00 ET | Minor Documentation Updates.
0.8.05 | 2022-12-06 05:00 ET | Updated to allow for csv quoting and dialect customization.  The following are defaults that can be adjusted in etld_config_settings.yaml.
0.8.05 | 2022-12-09 05:00 ET |     csv_distribution_python_csv_quoting = 'csv.QUOTE_NONE'
0.8.05 | 2022-12-09 05:00 ET |     csv_distribution_python_csv_dialect_delimiter = '\t'
0.8.05 | 2022-12-09 05:00 ET |     csv_distribution_python_csv_dialect_doublequote = False
0.8.05 | 2022-12-09 05:00 ET |     csv_distribution_python_csv_dialect_escapechar = '\'
0.8.05 | 2022-12-09 05:00 ET |     csv_distribution_python_csv_dialect_lineterminator = '\n'
0.8.05 | 2022-12-09 05:00 ET |     csv_distribution_python_csv_dialect_quotechar = None
0.8.05 | 2022-12-09 05:00 ET |     csv_distribution_python_csv_dialect_skipinitialspace = False
0.8.05 | 2022-12-09 05:00 ET |     csv_distribution_python_csv_dialect_strict = False
0.8.05 | 2022-12-09 05:00 ET |   The csv_distribution_python options above are tested with mysql load options in bash shell:
0.8.05 | 2022-12-09 05:00 ET |     zcat [table file].csv.gz | mysql $PORT_OPT -v -e "LOAD DATA LOCAL INFILE '/dev/stdin' INTO TABLE ${TABLE_NAME} CHARACTER SET UTF8 FIELDS TERMINATED BY '\\t' ESCAPED BY '\\\\' LINES TERMINATED BY '\\n';"
0.8.05 | 2022-12-09 05:00 ET |   SEE Log for options that are selected for your csv_distribution run to validate the options meet your needs.
0.8.10 | 2022-12-16 09:00 ET | Internal enhancements to authentication, replacing etld_lib_credentials with etld_lib_authentication_objects.
0.8.10 | 2022-12-16 09:00 ET | Added etld_config_settings.yaml option was_catalog_start_greater_than_last_id=[ID NUM], resulting in pulling only catalog entries greater_than_last_id entered.
0.8.10 | 2022-12-16 09:00 ET | Added transform to asset inventory table, from sensor json, new table fields: "sensor_lastPcScanDateAgent", "sensor_lastPcScanDateScanner", "sensor_lastVmScanDateAgent", "sensor_lastVmScanDateScanner" added to SQLite Schema.
0.8.11 | 2022-12-20 14:00 ET | Updated first time setup of user to allow for updating user/password from template.
0.8.14 | 2023-01-23 09:00 ET | Updated WAS to iterate / include over 1000 findings in a web application.
0.8.20 | 2023-08-08 23:00 ET | Added experimental support for Host List Detection ASSET_CVE field.  Contact your Technical Account Manager and David Gregory to enable ASSET_CVE.  See [QWEB 10.23 release notification for details](https://www.qualys.com/docs/release-notes/qualys-cloud-platform-10.23-api-release-notes.pdf) 
0.8.20 | 2023-08-08 23:00 ET | Added Database Injection - Methods to inject schema/data from QualysETL into your downstream databases. Ex. Azure Cosmos DB (PostgreSQL), Amazon RedShift, PostgreSQL Open Source, MySql Open Source, SnowFlake, Microsoft SQL Server.  Contact your Qualys TAM to schedule a call with David Gregory if you wish to use this feature. 
0.8.20 | 2023-08-08 23:00 ET | Visualization Use Case -  Use QualysETL to build your downstream databases for use with PowerBI, Tableau, Etc. Contact your Qualys TAM to schedule a call with David Gregory if you wish to use this feature. 
0.8.20 | 2023-08-08 23:00 ET | QWEB 10.23 Updates - Delivered additional fields for Host List and Host List Detection. For details see:  See [QWEB 10.23 release notification for details](https://www.qualys.com/docs/release-notes/qualys-cloud-platform-10.23-api-release-notes.pdf) 
0.8.20 | 2023-08-08 23:00 ET | Web Application Scanning(WAS) - Updated timing in WAS for long running jobs.
0.8.20 | 2023-08-08 23:00 ET | Docker Image Testing - Contact your TAM to schedule a call with David Gregory.  Encapsulate Python Application into distributable docker image for ease os operation and upgrade.
```