# PADE-Python Project Documentation

- Point of contact: [John Bowyer](mailto:zfi4@cdc.gov)
- Organizational unit: OCIO
- Related projects: EDC
- Related investments:  Pending Public Release
- Governance status: Pending Public Release
- Program official:  [Erik Knudsen](mailto:knu1@cdc.gov)

## Getting Started

## Set up Local development environment for Python - with remote spark

### Check if Python is installed

Run in bash or powershell

1. Check Python Version

        ```sh
        python3 --version
        ```
        
        or
        
        ```sh
        python --version
        ```

    - Ensure it is python 3.9.9

### Install Python 3.9

#### Run Install Python on Ubuntu or WSL (Primary)

        ```sh
        sudo apt update
        sudo apt install python3.9
        ```

Update Path

        ```sh
        nano ~/.bashrc
        export PATH="/usr/bin/python3.9:$PATH"
        source ~/.bashrc
        ```
  
#### Run Install Python on windows

Run Application

        Download: https://www.python.org/ftp/python/3.9.9/python-3.9.9-embed-amd64.zip
        Install as a non global user

### Install Pip

#### Run Install Pip on Ubuntu or WSL (Primary)

        ```sh
        sudo apt update
        sudo apt-get install python3-pip
        ```

#### Run Install Pip on Windows

        ```sh
        py -m ensurepip --upgrade
        ```

### Install Virtual Environment

#### Run Install Virtual Environment on Ubuntu or WSL (Primary)

See [Virtual Environment Set Reference Article](https://www.freecodecamp.org/news/virtualenv-with-virtualenvwrapper-on-ubuntu-18-04/)

If first virtual environment on desktop

1. Open Terminal in home directory

        ```sh
        cd $HOME
        ```

2. Create Directory for virtual environment

```sh
mkdir .virtualenv
```

3. Ensure Pip is installed

```sh
sudo apt install python3-pip
```

4. Validate pip is installed

```sh
pip3 --version
```

5. Install virtualenv via pip3.

```sh
pip3 install virtualenv
```

6. Validate virtualenv location

```sh
which virtualenv
```

7. Install 3.9 venv

```sh
sudo apt install python3.9-venv
```

8. Install Virtual Environments Wrapper

```sh
pip install virtualenvwrapper
pip3 install virtualenvwrapper
```

9. Update path

```sh
export PATH="$HOME/.local/bin:$PATH"
export PATH="/usr/bin:$PATH"
echo WORKON_HOME="~/.virtualenvs" | sudo tee -a $HOME/.bashrc
echo VIRTUALENVWRAPPER_VIRTUALENV="$HOME/.local/bin/virtualenv" | sudo tee -a $HOME/.bashrc
echo "VIRTUALENVWRAPPER_PYTHON=$(which python3)" | sudo tee -a $HOME/.bashrc
echo "source $HOME/.local/bin/virtualenvwrapper.sh" | sudo tee -a $HOME/.bashrc
source $HOME/.bashrc
```

If second or later virtual environment on desktop

1. Make Virtual Envs

```sh
mkvirtualenv OCIO_PADE_DEV
mkvirtualenv EZDX_FOODNET_DEV
mkvirtualenv OCIO_PADE_DEV
mkvirtualenv OD_DATALAKE_DEV
mkvirtualenv OD_NHANES_DEV
mkvirtualenv NDSP_PERTUSSIS_DEV
mkvirtualenv NDSP_PERTUSSIS_QA
mkvirtualenv NDSP_PERTUSSIS_ONBOARD
mkvirtualenv NDSP_PERTUSSIS_PROD
```

2. If existing environment configured - deactivate

```sh
deactivate
sudo pip uninstall nodeenv
pip install nodeenv
workon {virtualenv name}
nodeenv -p
```

Example

```sh
deactivate
cd $HOME
# cleanup any existing node
sudo rm -rf node-v18.12.1-linux-x64.tar.xz
sudo rm -rf /usr/local/bin/npm /usr/local/share/man/man1/node* ~/.npm
sudo rm -rf /usr/local/lib/node*
sudo rm -rf /usr/local/bin/node*
sudo rm -rf /usr/local/include/node*
sudo apt-get purge nodejs npm
sudo apt autoremove
sudo pip uninstall nodeenv
```

3. Activate new virtual env

```sh
deactivate
cd $HOME
# cleanup any existing node
sudo rm -rf node-v18.12.1-linux-x64.tar.xz
# sudo rm -rf /usr/local/bin/npm /usr/local/share/man/man1/node* ~/.npm
# sudo rm -rf /usr/local/lib/node*
# sudo rm -rf /usr/local/bin/node*
# sudo rm -rf /usr/local/include/node*
sudo apt-get purge nodejs npm
sudo apt autoremove
sudo pip uninstall nodeenv
workon VIRTUAL_ENV
# EXAMPLE:
workon OCIO_PADE_DEV
cd $VIRTUAL_ENV
# install node
wget https://nodejs.org/dist/v18.12.1/node-v18.12.1-linux-x64.tar.xz
tar -xf node-v18.12.1-linux-x64.tar.xz
sudo mv node-v18.12.1-linux-x64/bin/* ./bin/
sudo mv node-v18.12.1-linux-x64/lib/node_modules/ ./lib/node_modules/
# Verify installation using
node -v
npm -v
npm install npm@9.1.1
pip install --upgrade pip
pip install nodeenv
cd $VIRTUAL_ENV/lib/node_modules/npm
nodeenv -p
cd $VIRTUAL_ENV/lib
npm install @mermaid-js/mermaid-cli --registry=https://registry.npmjs.org
cdvirtualenv bin
echo "export PATH='$PATH:$VIRTUAL_ENV/lib/node_modules/.bin'" | sudo tee -a activate
source activate
# Test client
mmdc -h
```

### Remove local Virtual Environment

#### Run remove virtual environment on Ubuntu or WSL (Primary)

Run

```sh
deactivate
rmvirtualenv OCIO_PADE_DEV
```

For global

```sh
sudo rm -rf venv
```

For local

```sh
rm -rf OCIO_PADE_DEV
```

## Run Unit Test Coverage Report

### Run Unit Test Coverage Report on Ubuntu or WSL (Primary)

Run the following command

```sh
cd data_ecosystem_services
pytest --cov-report html tests/
```

## Set up Local development environment for Docker

### Install Docker without License on Ubuntu or WSL (Primary)

Reference 1: [Install Docker Engine without Docker Desktop](https://dev.to/bowmanjd/install-docker-on-windows-wsl-without-docker-desktop-34m9)
Reference 2: [Install Docker for WSL](https://docs.docker.com/engine/install/ubuntu/)

Option 1: Convenience Script

Docker provides a convenience script at [Docker Script](https://get.docker.com) to install Docker into development environments non-interactively. The convenience script isn't recommended for production environments, but it's useful for creating a provisioning script tailored to your needs.

1. Run command

```sh
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

    Note: You will have to wait 20 seconds

2. Build and Run Image

```sh
cd .devcontainerlocal
sudo docker build -t OCIO_PADE_DEV .
sudo docker run -it --rm --name OCIO_PADE_DEV OCIO_PADE_DEV
```

Option 2: Manual Install

1. Check that you have WSL version 2

```sh
wsl --set-default-version 2
```

2. Remove any old docker images

```sh
sudo apt remove docker docker-engine docker.io containerd runc
```

3. Install/Upgrade dependencies

```sh
sudo apt-get update
sudo apt-get install \
ca-certificates \
curl \
gnupg \
lsb-release
```

4. Add Docker's official GPG key

```sh
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

5. Add Docker's stable repository

 ```sh
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

6. Install Docker Engine and Docker Compose

 ```sh
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

7. Verify Docker Install

 ```sh
sudo docker run hello-world
```

### Install Docker without Desktop License on Windows

Docker CLI is required for managing images. It is available for install at

## Set up Local development environment for EcPaas

### Install Openshift

The OC Client is used to manage all resources in a project and can be downloaded from

1. Install [OC Client](https://web-ecpaas-resources.services-dev.cdc.gov/index.html)

The OCP Web sh can also be used to perform most of the project administration tasks. Additional OC information is available at [OpenShift Client](https://docs.openshift.com/online/cli_reference/get_started_cli.html#cli)

### Install OpenShift Postgres Setup

- [Connection instruction](https://cdc.sharepoint.com/:w:/r/teams/NCCDPHPDDTOpsCenterITDEV/Shared%20Documents/General/Documentation/DDT%20Ops%20-%20Connecting%20to%20Postgres.docx?d=w47a87ba54d764f63999fb7c99ecd6794&csf=1&web=1&e=i4jzdc)

### OpenShift Client Postgres connection

Steps to follow:

- [Login to ARO *RedHat Open Shift](https://oauth-openshift.apps.ecpaas-dev.cdc.gov/oauth/authorize?client_id=sh&redirect_uri=https://sh-openshift-sh.apps.ecpaas-dev.cdc.gov/auth/callback&response_type=code&scope=user:full&state=765b71ff)
- [OpenShift login](https://oauth-openshift.apps.ecpaas-dev.cdc.gov/oauth/authorize?client_id=sh&redirect_uri=https://sh-openshift-sh.apps.ecpaas-dev.cdc.gov/auth/callback&response_type=code&scope=user:full&state=765b71ff)
- connect to pod nccdphp-postgresql-test-26-xppw8

Run

```sh
 oc
```

- Login to: [Openshift](https://sh-openshift-sh.apps.ecpaas-dev.cdc.gov/)
- Select AAD to log in.
- Once logged in, Select "Copy Login command"
- top right menu. This opens another login screen,
- select AAD
- click "Open token"
- Copy login token to cmd oc screen
- Run login command
- Change to correct project:

```sh
oc project "ddt-ops-center"
```

- Port-forward using

```sh
oc port-forward nccdphp-postgresql-test-32-btxvk 5432
```

- (if the pod has changed, find the correct pod name using the commands below)Get list of pods using:

```sh
oc get po
oc get po|grep post (if you are using git bash as your shell)
oc get po| findstr "post" (select only PostgreSQL pods)
```

- While this is running connect via Azure Data Studio
Credentials sent seperately

### OpenShift Client Postgres connection Troubleshooting

- if stuck on forwarding
- click on server name in azure data studio

## Set up Local development environment for Node Web Applications

Install Node on Windows

1. Run [Node 18.12.1 Installation MSI](https://nodejs.org/dist/v18.12.1/node-v18.12.1-x64.msi)
2. Run Update Node to latest version

```sh
npm install -g npm
```

### Install Poetry

#### Run Install Poetry on Ubuntu or WSL (Primary)

Reference: [StackOverflow: Poetry with Docker](https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker)

1. Install Poetry

```sh
cd $VIRTUAL_ENV
curl -sSL https://install.python-poetry.org | python3 -
```

2. Copy poetry to local bin

```sh
cp $VIRTUAL_ENV/bin/poetry ~/.local/bin
```

#### Run Install Poetry on Windows

```sh
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### Activate Virtual Environment

#### Run activate virutal environment

```sh
workon EZDX_FOODNET_DEV
workon OCIO_PADE_DEV
workon OD_DATALAKE_DEV
workon NDSP_PERTUSSIS_DEV
workon NDSP_PERTUSSIS_QA
workon NDSP_PERTUSSIS_ONBOARD
workon NDSP_PERTUSSIS_PROD
```

### Update Libraries with Poetry

#### Prerequisites for Run Update Libraries on Ubuntu or WSL

1. Clone Repository DAVT
2. Open Repository in VS Code
3. Set Python environment to a virtual environment such OCIO_PADE_DEV
4. Open Terminal in WSL

#### Run Update Libraries on Ubuntu or WSL (Primary)

```sh
cd _templates/data_ecosystem_services
poetry update
```

#### Run Update Libraries on Windows

```sh
cd "C:\Users\jcbow\OneDrive - CDC\DAVT Analytics\davt-dev-jcbowyer"
poetry update
```

#### VS Code Python Settings

1. Go to VS Code -> File -> Preferences -> Settings -> Workspace Settings -> Python Configuration
2. Click Edit in settings.json
3. Search for each of the following settings to update
4. Add this line to your settings: "python.linting.pep8Args": ["--max-line-length=120"],
5. Add this line to your settings: "python.linting.pep8Args": ["--ignore=E402,F841,F401,E302,E305"],
6. Add this line to your settings: "python.analysis.typeCheckingMode": "basic"

#### VS Code Markdown Settings

For the markdown all in one exension

1. Set markdown.extension.toc.levels to 2..6 to skip header


## Set up Local Environment .NET Core for Web API Dev

## Developer/Data Engineer Project Quick Start

1. Decide on two part name of project
    - Root Project: Example: ocio
    - Individual Project: Example: pade
2. Get access to center SharePoint and set up clone initial SharePoint lists if this is the first DAVT project in the center
   - codes/value_sets
   - columns
   - datasets
   - environments
   - jobs
   - pipelines
   - projects
   - reports
   - users
   - user_roles
3. Create GitHub repository in GitHub CDCEnt organization named {root_project}_{individual_project}: Example: ocio_pade
4. Clone GitHub repository to local machine and open in VSCode
5. Create docs directory in root of project and copy standard files
   - conf.py
   - davt_t.docx
   - davt_t.pptx
   - index.rst
   - lua_word.lua
   - lua_pdf.lua
   - lua_html_pptx.lua
   - lua_md.lua
6. Request top level a storage container in EDAV if this is the first EDAV project in the center
7. Configure top level project folder in EDAV storage container
    - Set up top level foder: example:
      - ocio_pade
    - Set up dev and qa subfolders: example:
      - ocio_pade/dev
    - Set up ingress, archive and config subfolders: example:
      - ocio_pade/dev/ingress
      - ocio_pade/dev/archive
      - ocio_pade/dev/config

## Developer/Data Engineer Troubleshoot Problems and Errors

### Problem: Java: Windows ignores JAVA_HOME

Symptom:   Windows ignores JAVA_HOME

Resolution:

The Java installer will put a copy of java.exe (but no libraries) in the C:\Program Files (x86)\Common Files\Oracle\Java\javapath directory and add that directory to the beginning of the PATH variable.

If you don"t use a full path, the copy of java.exe to run is found by using the PATH system variable. Since this directory doesn"t contain the DLLs of a particular Java runtime version, one is located one by looking at the registry.

So, you either need to modify the registry, or replace the javapath entry with the version of Java you want in your PATH system (not user) variable.

Recommend setting registry

        Computer\HKEY_CURRENT_USER\Environment\JAVA_HOME
        C:\apps\Java\jdk1.8.0_333

Reference:  [Stack Overflow](https://stackoverflow.com/questions/5492937/windows-ignores-java-home-how-to-set-jdk-as-default)

### Problem: Node: Unable to remove existing node_modules

Problem: Unable to remove existing local node_modules

Solution:

Run Command

```sh
cd path_with_modules
find . -name 'node_modules' -type d -prune -exec rm -rf '{}' +
```

Problem: Unable to remove all existing global node_modules

Solution:

Run Command

```sh
npm ls -gp --depth=0 | awk -F/ '/node_modules/ && !/\/npm$/ {print $NF}' | xargs npm -g rm
```

### Problem: Python: Unable to remove existing python packages

Problem: Unable remove existing python packages

Solution:  Run from elevated command prompt to removes all local packages in your environment

```sh
pip freeze | xargs pip uninstall -y
```

### Problem: NPM Won't Run After Upgrade

Problem: NPM Won't Run After Upgrade using a manual install

Reference: [Stack Overflow](https://stackoverflow.com/questions/8935341/npm-wont-run-after-upgrade/8935401#8935401)

Solution:

If npm is no longer installed in /usr/bin/npm, then chances are good bash(1) has hashed the executable name. The hashing saves repeated searches of all directories in your PATH every time you execute common programs. Since programs almost never change directories, this is usually a great idea.  To fix this isue, remove the hash by running the following command:

```sh
hash -r.
```

### Problem: WSL: Ubuntu: Unable to reset WSL root password in Ubuntu

Symptom:  Unable to reset WSL root password in Ubuntu

Reference:  [AskUbuntu](https://askubuntu.com/questions/931940/unable-to-change-the-root-password-in-windows-10-wsl)

Solution:

1. Open cmd.exe
2. Type:

```sh
wsl -u root
```

3. Change the password:

```sh
passwd username
```

4. Type:

```sh
exit
```

5. Type:

```sh
wsl
```

6. Confirm the new password works:

```sh
sudo echo hi
spark.conf.set("spark.databricks.pyspark.enablePy4JSecurity", "false")
```

### Error: Azure B2C: The subscription is not registered to use namespace 'Microsoft.AzureActiveDirectory'.

Symptom: Receive error when creating an Azure B2C tenant: The subscription is not registered to use namespace 'Microsoft.AzureActiveDirectory'.  See https://aka.ms/rps-not-found for how to register subscriptions.

Reference: [Blog](https://adamstorr.azurewebsites.net/blog/subscription-is-not-registered-to-use-namespace-Microsoft.AzureActiveDirectory)

Resolution:

1. Login to azure. Start up a shell and type the following command.

    ``` az
    az login
    ```

    This will start up a browser and you will need to log into Azure.

2. Get subscription list.  If you have one subscription then the default will be selected. If not then you will need to check your subscriptions and then set the right one.  Using the account list command you can get a list of your subscriptions.

    ```az
    az account list
    ```

    You will get a list of subscriptions that you have access to.  You can then set the subscription you want to work on.

3. Set the subscription to work on.

    ```az
    az account set --subscription "ZFI4-PERSONAL-DEV"
    ```

4. Register the namespace provider

    ```az
    az provider register --namespace Microsoft.AzureActiveDirectory
    ```

### Error: Azure: ClientSecret: Secret should be an Azure Active Directory application's client secret

Symptom:  Receive error: secret should be an Azure Active Directory application's client secret when calling function: credential = ClientSecretCredential(tenant_id, client_id, client_secret)

Resolution:

        - If running from local jupyter notebook ensure you have set the local python environment for your project: Example: OD_NHANES_DEV
        - Use the client secret of the service principal, not the client secret of the app registration.
        - Ensure that the client secret of the service principal is set in the system environment variable for your application: Example: DAVT_OD_NHANES_DEV_AZURE_CLIENT_SECRET

### Error: Databricks: Spark: Cannot find catalog plugin class for catalog "spark_catalog": org.apache.spark.sql.delta.catalog.DeltaCatalog

Problem: org.apache.spark.SparkException: Cannot find catalog plugin class for catalog "spark_catalog": org.apache.spark.sql.delta.catalog.DeltaCatalog

Resolution:

From your virtual environment.  You can select using workon venv_name

Run

```sh
pyspark --packages io.delta:delta-core_2.12:1.0.0 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
```

or

Copy io.delta:delta-core_2.12:1.0.0 JAR file to $SPARK_HOME/lib and restart

This should make error go away.

Reference: [Stack Overflow](https://stackoverflow.com/questions/69862388/how-to-run-spark-sql-thrift-server-in-local-mode-and-connect-to-delta-using-jdbc)

### Error: Databricks: Error in SQL statement: SecurityException: User does not have permission SELECT on any file

Symptom: Table creation fails in Databricks with security exception: Error in SQL statement: SecurityException: User does not have permission SELECT on any file.

Reference: [Databricks KB](https://kb.databricks.com/en_US/security/table-create-security-exception)

Solution:

Run the following command:

```sql
GRANT SELECT ON ANY FILE TO `user1`
```

Warning

It is important to understand the security implications of granting ANY FILE permissions on a filesystem. You should only grant ANY FILE to privileged users. Users with lower privileges on the cluster should never access data by referencing an actual storage location. Instead, they should access data from tables that are created by privileged users, thus ensuring that Table ACLS are enforced.

In addition, if files in the Databricks root and data buckets are accessible by the cluster and users have MODIFY privileges, the admin should lock down the root.

### Error: Databricks: Spark: Illegal character in path

Problem: Spark illegal character in path

Resolution:

run

```sh
spark-class org.apache.spark.deploy.master.Master
```

then

```sh
spark-shell --master spark://ip_and_port_from_step_above
```

example

```sh
spark-shell --master spark://192.168.86.27:7077
```

Reference: [Stack Overflow](https://stackoverflow.com/questions/69669524/spark-illegal-character-in-path)

### Error: Databricks: Spark: Cannot find catalog plugin class

Symptom:  Receive error: Cannot find catalog plugin class for catalog "spark_catalog"

Resolution:

Copy delta-core_2.13-2.1.0 JAR file to $SPARK_HOME/lib and restart, this error goes away.

### Error: Databricks: Spark: WARN ProcfsMetricsGetter

Symptom:  Receive errror:  Encountering "WARN ProcfsMetricsGetter: Exception when trying to compute pagesize" error when running Spark

Resolution

Adding PYTHONPATH environment variable with value as:

```sh
%SPARK_HOME%\python;%SPARK_HOME%\python\lib\py4j-<version>-src.zip;%PYTHONPATH%
```

Reference:  [Stack Overflow](https://stackoverflow.com/questions/60257377/encountering-warn-procfsmetricsgetter-exception-when-trying-to-compute-pagesi)

### Error: Databricks: Spark: py4j: Constructor public com.databricks.backend.daemon.dbutils.FSUtilsParallel(org.apache.spark.SparkContext) is not whitelisted

Problem: Error: py4j.security.Py4JSecurityException: Constructor public com.databricks.backend.daemon.dbutils.FSUtilsParallel(org.apache.spark.SparkContext) is not whitelisted when connecting from Databricks to ADSL from Datascience Cluster

Reference: [Databricks Community Q and A](https://community.databricks.com/s/question/0D53f00001OFuWLCA1/can-you-help-with-this-error-please-issue-when-using-a-new-high-concurrency-cluster)

Solution:

Update function setup_spark_configuration in environment_metadata class

```sh
spark.conf.set("spark.databricks.pyspark.enablePy4JSecurity", "false")
```

### Error: Databricks: SQL: Table creation fails with security exception

Problem: Table creation fails with security exception

Reference: [Databricks KB](https://kb.databricks.com/en_US/security/table-create-security-exception)

Solution:

```sql
GRANT SELECT ON ANY FILE TO `user1`
```

Warning

It is important to understand the security implications of granting ANY FILE permissions on a filesystem. You should only grant ANY FILE to privileged users. Users with lower privileges on the cluster should never access data by referencing an actual storage location. Instead, they should access data from tables that are created by privileged users, thus ensuring that Table ACLS are enforced.

In addition, if files in the Databricks root and data buckets are accessible by the cluster and users have MODIFY privileges, the admin should lock down the root.

### Error: Docker: ERROR: failed to solve: error getting credentials - err: docker-credential-desktop.exe resolves to executable in current directory (./docker-credential-desktop.exe), out:

Symptom: During Docker Build Receive ERROR: failed to solve: error getting credentials - err: docker-credential-desktop.exe resolves to executable in current directory (./docker-credential-desktop.exe), out:

Reference: [Stack Overflow](https://github.com/docker/docker-credential-helpers/issues/60)

Solution:

1. Run command:

    ``` sh
        code ~/.docker/config.json
    ```

2. Change credsStore to credStore

3. Save

### Error: Docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?

Symptom: Receiving error: "Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running? " when trying to run a docker build command

Reference: [Stack Overflow](https://stackoverflow.com/questions/44678725/cannot-connect-to-the-docker-daemon-at-unix-var-run-docker-sock-is-the-docker)

Solution:

Run command:

```sh
sudo dockerd
```

### Error: Docker: During connect receive message: This error may indicate that the docker daemon is not running

Symptom:  Receive error: error during connect: This error may indicate that the docker daemon is not running.: when attempting to run docker image

Reference: [Stack Overflow](https://stackoverflow.com/questions/40459280/docker-cannot-start-on-windows)

Details:

- The error is related to message: In the default daemon configuration on Windows, the docker client must be run elevated to connect

Resolution with Docker Desktop:

1. Verify that Docker Desktop application is running. If not, launch it: that will run the docker daemon (just wait few minutes).
2. If the error still persists, you can try to switch Docker daemon type, as explained below:

Resolution with Powershell:

1. Open Powershell as administrator
2. Launch command: & 'C:\Program Files\Docker\Docker\DockerCli.exe' -SwitchDaemon

Resolution with CMD:

1. Open cmd as administrator
2. Launch command: "C:\Program Files\Docker\Docker\DockerCli.exe" -SwitchDaemon

### Error: Git: remote: error: File x is 296.35 MB; this exceeds GitHub's file size limit of 100.00 MB

Symptom: Receive error: git push origin dev-zfi4:dev-zfi4
remote: warning: File pade/pade_ocio_ingress/ehr/encounters.csv is 87.59 MB; this is larger than GitHub's recommended maximum file size of 50.00 MB
remote: error: Trace: 2c8fbfed93d4f4c52468dde090cd8d14a1a311d13a6aa58ea35cb9cb8c5d2577
remote: error: See http://git.io/iEPt8g for more information.
remote: error: File pade/pade_ocio_ingress/ehr/observations.csv is 296.35 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
To https://github.com/cdcent/data-ecosystem-services.git
 ! [remote rejected] dev-zfi4 -> dev-zfi4 (pre-receive hook declined)

Reference: [Stack Overflow](https://stackoverflow.com/questions/33330771/git-lfs-this-exceeds-githubs-file-size-limit-of-100-00-mb)

Solution:

```sh
git filter-branch --tree-filter 'rm -rf path/to/your/file' HEAD
git push
```

### Error: Git: Support for password authentication was removed. Please use a personal access token instead

Symptom:  Receive error: Support for password authentication was removed. Please use a personal access token instead. when trying to push to a remote repository

Reference: [Stack Overflow](https://stackoverflow.com/questions/68775869/message-support-for-password-authentication-was-removed-please-use-a-personal)

Solution:

For Ubuntu:

For Linux, you need to configure the local GIT client with a username and email address,

```sh
git config --global user.name "your_github_user_id"
git config --global user.email "your_github_email"
git config -l
```

### Error: Git: Tag: Would clobber existing tag

Symptom:  CICD or VS Code Tag give error "would clobber existing tag"

Solution:

Run Git

```sh
git fetch --tags -f
```

Then pull again.

Reference: [Stack Overflow](https://stackoverflow.com/questions/58031165/how-to-get-rid-of-would-clobber-existing-tag)

### Error: Git: fatal: mmap failed: Invalid argument

Symptom: Receiving error: Git fatal: mmap failed: Invalid argument

Reference: [Stack overflow](https://stackoverflow.com/questions/60322637/git-fatal-mmap-failed-invalid-argument)

Solution:

1. Log into OneDrive
2. Finish synch

### Error: Java: Gateway process exited before sending its port number

Problem:  "Java gateway process exited before sending its port number"

Resolution:

On All OS:

Check that the following environment variable is set where 1 is the number of processors

```sh
export PYSPARK_SUBMIT_ARGS="--master spark:192.168.86.27:7077"
```

or

```sh
export PYSPARK_SUBMIT_ARGS="--master local[1] pyspark-shell"
```

On Ubuntu: install openjdk-8-jdk package

```sh
sudo apt-get install openjdk-8-jdk-headless -qq
```

On MacOs: run:

```sh
java -version
```

Verify Resolution In Python:

```python
from pyspark import SparkContext
sc = SparkContext.getOrCreate()

# check that it really works by running a job
# example from http://spark.apache.org/docs/latest/rdd-programming-guide.html#parallelized-collections
data = range(10000)
distData = sc.parallelize(data)
distData.filter(lambda x: not x&1).take(10)
```

OR

Reference: [Stack Overflow](https://stackoverflow.com/questions/31841509/pyspark-exception-java-gateway-process-exited-before-sending-the-driver-its-po)

### Error: Java: Maven: javax.net.ssl.SSLHandshakeException: PKIX path building failed

Symptom:   Server access error at url [Maven URL](https://repo1.maven.org/maven2/io/delta/delta-core_2.12/1.0.0/delta-core_2.12-1.0.0.pom) (javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target)

Resolution:

Run:

From cli change dir to jre\bin

1. First of all you copy the URL that you are connecting to and paste it in your browser. Just paste the url in the address bar and press enter.
   Example: [Maven Repo](https://repo1.maven.org/maven2)
2. Now click on the lock button on the left of the url to see Certificate (valid)
3. Click on View Certificate to open up the following popup
4. Click on the Certification Path tab, where you will see the certificate chain
5. Double click on the parent certificate
6. Check keystore (file found in C:\apps\jdk-8.0.342.07-hotspot\jre\lib\security directory)
    a. cd C:\apps\jdk-8.0.342.07-hotspot\bin
    b. keytool -list -keystore cacerts
    c. Password is changeit
    d. Download and save all certificates in chain from needed server.
7. Remove "read-only" attribute on file ..\lib\security\cacerts),
8. Copy repo1.maven.org.crt to "C:\apps\Java\jdk1.8.0_333\lib\security\repo1.maven.org.crt" and "C:\Users\zfi4\OneDrive - CDC\DAVT Analytics\davt-dev-jcbowyer\_templates\certs\repo1.maven.org.crt"
9. Add certificates

```sh
keytool -import -alias repo1_maven_org -keystore C:\apps\jdk-8.0.342.07-hotspot\jre\lib\security\cacerts -file  "C:\Users\zfi4\OneDrive - CDC\DAVT Analytics\davt-dev-jcbowyer\_templates\certs\repo1.maven.org.crt"

keytool -import -alias repo_spark_packages_org -keystore C:\apps\jdk-8.0.342.07-hotspot\jre\lib\security\cacerts -file  "C:\Users\zfi4\OneDrive - CDC\DAVT Analytics\davt-dev-jcbowyer\_templates\certs\repos.spark-packages.org.crt"
```

10. Run the keytool command again to verify that your private root certificate was adde

```sh
keytool -list -keystore C:\apps\Java\jdk1.8.0_333\lib\security\cacerts
```

Reference: [Stack Overflow](https://stackoverflow.com/questions/9210514/unable-to-find-valid-certification-path-to-requested-target-error-even-after-c)
Reference: [Java Samples](http://www.java-samples.com/showtutorial.php?tutorialid=210)

### Error: Logic Apps: O365 User Name and Password Entry Window Disappears on SharePoint Connector Setup

The pop-up window for user name and password entry may close immediately when Cached Credentials expired.

1. Try deleting your cached O365 credentials in Credentials Manager.
2. If clearing O365 casched credentials does not work, try deleting certificates.
3. If neither deleting you cached O365 credentials nor deleting ceritifates works, try deleting the identities folder that may still be cached:

- Close all office applications
- Press Win+R and type regedit to open Registry Editor
- From Registry Editor, browse to: KEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common\Identity\Identities
- Delete the identities folder.
- Open Office and sign in again to check if the same problem will occur.

### Error: Logic Apps: Save logic app failed: 'Execute_JavaScript_Code' of type 'JavaScriptCode'

Symptom:  Receive Error:  Failed to save logic app logic-sps-list-export-all-environments. The workflow must be associated with an integration account to use the workflow run action 'Execute_JavaScript_Code' of type 'JavaScriptCode'.

Reference: [Stack Overflow](https://stackoverflow.com/questions/57013675/using-execute-javascript-code-action-in-azure-logic-app-error-about-integrati)

Resolution:  To run the inline code action you need an integration account. These have some different pricing tiers. You only need to create it and then on the Logic App Workflow settings associate it.

### Error: Mermaid: Expecting 'NEWLINE', 'SPACE', 'GRAPH', got 'ALPHA'

Problem: Mermaid raises error Expecting 'NEWLINE', 'SPACE', 'GRAPH', got 'ALPHA' when it encounters bracket.

Reference: [GitHub](https://github.com/mermaidjs/mermaid.cli/issues/68)

The issue seems to be, that mermaid.cli ships with an old version of mermaid.min.js which doesn't support these kinds of node types/attributes.

Resolution:

Explicitly install mermaid and then copy dist/mermaid.min.js into the mermaid.cli folder within node_modules

Version is avaialble at [unpkg.com-mermaid](https://unpkg.com/mermaid@latest/dist/mermaid.min.js)

### Error: Node: NPM: PhantomJS not found on PATH

Symptom:  Receiving error: "PhantomJS not found on PATH" when running npm install

Reference: [StackOverflow](https://stackoverflow.com/questions/18218134/warning-phantomjs-not-found)

Solution:

1. Run command

```sh
sudo npm uninstall phantomjs
```

2. Run command

```sh
sudo npm install phantomjs -g
```

3. If fails global install try local install

```sh
sudo npm install phantomjs -s
```

### Error: Python: Virtualenv - workon command not found

Symptom: workon command not found

Reference:  [StackOverflow](https://stackoverflow.com/questions/34611394/virtualenv-workon-command-not-found)

Details:

The workon command is not available if you have restarted the shell.

If you want this to work with each shell, you'll need to add these to your ~/.bashrc file

Solution:

1. Run

```sh
export PATH="$HOME/.local/bin:$PATH"
echo "export WORKON_HOME=$HOME/.virtualenvs" | sudo tee -a $HOME/.bashrc
echo "VIRTUALENVWRAPPER_PYTHON='/usr/lib/python3.9'" | sudo tee -a $HOME/.bashrc
echo "source $HOME/.local/bin/virtualenvwrapper.sh" | sudo tee -a $HOME/.bashrc
source $HOME/.bashrc
```

### Error: Puppeteer: can't launch chromium, missing shared library libgbm.so

Symptom: Receiving error: "Error: Failed to launch the browser process! /usr/bin/chromium: error while loading shared libraries: libgbm.so.1: cannot open shared object file: No such file or directory"

Details:  Puppeteer is a Node library which provides a high-level API to control headless Chrome or Chromium over the DevTools Protocol. It can also be configured to use full (non-headless) Chrome or Chromium.  It is not launching when running mermaid-cli.

Reference: [GitHub](https://github.com/actions/runner-images/issues/732)

Solution:

Add the lgm package to the Dockerfile/Setup process

```sh
sudo apt-get update
sudo apt-get install -y libgbm-dev
```

### Error: Python: Current Python version (3.8.10) is not allowed by the project (^3.9).

Symptom: Error: Python: Current Python version (3.8.10) is not allowed by the project (^3.9). Current Python version (3.8.10) is not allowed by the project (^3.9). Please change python executable via the "env use" command.

Reference: [Stack Overflow](https://stackoverflow.com/questions/60580113/change-python-version-to-3-x)

Details:  Please change python executable via the "env use" command.

Solution:

1. You can get the path to your Python version by running

```sh
which python3.9
```

2. To update your environment to latest path run

```sh
poetry env use /usr/bin/python3.9
```

### Error: React: NodeJS: Ubuntu: Error: EACCES: permission denied, mkdir '/usr/local/lib/node_modules/node-sass/build'

Symptom: Receiving Error when running npm link command:  Error: EACCES: permission denied, mkdir '/usr/local/lib/node_modules/node-sass/build'

Reference: [Stack Overflow](https://stackoverflow.com/questions/49679808/error-eacces-permission-denied-mkdir-usr-local-lib-node-modules-node-sass-b)

Details: EACCES: permission denied, mkdir '/usr/local/lib/node_modules/node-sass/build'

Solution:

Change the ownership of folder node_modules, because you use sudo npm install -g node-sass, so its ownership is set to root.


```sh
sudo chown -R root:$(whoami) /usr/local/lib/node_modules/
sudo chmod -R 775 /usr/local/lib/node_modules/
```

### Error: Sphinx: WARNING: dot command 'dot' cannot be run (needed for graphviz output), check the graphviz_dot setting

Symptom: Receiving error: "WARNING: dot command 'dot' cannot be run (needed for graphviz output), check the graphviz_dot setting" when building HTML Sphinx documentation

Reference: [Stack Overflow](https://stackoverflow.com/questions/63503855/warning-dot-command-dot-cannot-be-run)
Reference: [Blog](https://osxdaily.com/2014/08/14/add-new-path-to-path-command-line/)

Details: The problem could be referred to an incorrect configuration of "dot" executable from GraphViz PATH.

Solution:

Adding the PATH using the export command, such as:

```sh
export PATH=$PATH:~/opt/bin
```

### Error: Ubuntu: InRelease is not valid yet (invalid for another 1d 21h 40min 43s). Updates for this repository will not be applied.

Symptom:  Ubuntu: InRelease is not valid yet (invalid for another 1d 21h 40min 43s). Updates for this repository will not be applied. occurs when running sudo apt-get update

Reference: [StackOverflow](https://askubuntu.com/questions/1059217/getting-release-is-not-valid-yet-while-updating-ubuntu-docker-container)

Details: Occurs when the system clock in Ubuntu is not Correct

Solution: Run the following command to fix the issue:

```sh
sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"
sudo apt update
```

### Error: Ubuntu: System has not been booted with systemd as init system (PID 1). Can't operate. Failed to connect to bus: Host is down

Symptom:  Receiving error: "System has not been booted with systemd as init system (PID 1). Can't operate. Failed to connect to bus: Host is down" when running : sudo systemctl daemon-reload

Reference: [Github Gist](https://gist.github.com/alyleite/ca8b10581dbecd722d9dcc35b50d9b2b)

Solution: Run the following command to fix the issue:

```sh
sudo apt-get update && sudo apt-get install -yqq daemonize dbus-user-session fontconfig
sudo daemonize /usr/bin/unshare --fork --pid --mount-proc /lib/systemd/systemd --system-unit=basic.target
exec sudo nsenter -t $(pidof systemd) -a su - $LOGNAME
```

### Error: Ubuntu: APT: Release file for [Ubuntu File](http://security.ubuntu.com/ubuntu/dists/focal-security/InRelease) is not valid yet

Symptom:  Receiving error: "Release file for [Ubuntu File](http://security.ubuntu.com/ubuntu/dists/focal-security/InRelease) is not valid yet" during apt-get update

Reference: [How2Shout](https://www.how2shout.com/linux/fix-inrelease-is-not-valid-yet-invalid-for-another-h-min-s-updates-for-this-repository-will-not-be-applied/)

Solution:

1. Check your date and time settings. If they are not correct, then you can fix them by running the following command:

```sh
sudo dpkg-reconfigure tzdata
```

### Error: VS Code Ubuntu/Docker/Web Server: Failed to bind to address already in use

Symptom:  Deploying a project to a local web server return error message: VS Code Ubuntu/Docker/Web Server: Failed to bind to address already in use

Reference: [Stack Overflow](https://stackoverflow.com/questions/52649979/failed-to-bind-to-address-already-in-use-error-with-visual-studio-mac-api)

Solution:

1. Determine which ports are blocked

    ``` sh
    lsof -i: <port number>
    ```

    example:

    ``` sh
    lsof -i: 5001
    ```
2. Kill the process that is blocking the port

    ``` sh
    kill -9 <process number>
    ```

    example:

    ``` sh
    kill -9 1600
    ```

### Error: Ubuntu: APT: Permission Denied when calling apt-get update from WSL

Symptom:  Permission Denied when calling apt-get updatee from WSL

Details:

1. Run wsl command from ubuntu
2. Receive Error

      Reading package lists... Done
      E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)
      E: Unable to lock directory /var/lib/apt/lists/

Reference: [AskUbuntu](https://askubuntu.com/questions/162879/how-to-fix-could-not-open-lock-file-because-permission-denied)

This line says you are not authorized to install/update. You need to be root to do it....

Resolution with WSL:

Add sudo before apt-get or you can do sudo -s to be root.

```sh
sudo apt-get update
```

or

Run the following command to promote the current terminal to run as root until the terminal is closed.

```sh
sudo -s
apt-get update
```

### Error: Ubuntu: ImportError: No module named pip ' right after installing pip

Symptom: Receive error: "ImportError: No module named pip" right after installing pip

Reference: [Stack Overflow](https://stackoverflow.com/questions/32639074/why-am-i-getting-importerror-no-module-named-pip-right-after-installing-pip)

Details: /home/jcbow/.virtualenvs/OCIO_PADE_DEV/bin/python: No module named pip

Resolution:

First, ensure that python is included in the PATH variable, then run
Then run the following

```sh
python -m ensurepip
```

### Error: Ubuntu: Failed to call method: org.freedesktop.DBus.Properties.Get: object_path= /org/freedesktop/UPower: org.freedesktop.DBus.Error.ServiceUnknown

Problem: When browsing https://127.0.0.1:5000 receive error: SSL: Handshake failed. while not logged into ZScaler

Solution: 

Here are the steps you can follow to fix this error:

1. Check if the UPower daemon is installed on your system by running the following command in the terminal:

```bash
systemctl status upower.service
```

If the command output shows that the UPower service is not running or is not installed, you can install it using the package manager for your system (e.g. apt-get for Ubuntu/Debian, dnf for Fedora, pacman for Arch Linux, etc.).

2. Install the UPower daemon using the package manager. For example, on Ubuntu/Debian, you can run the following command:

```bash
sudo apt-get install upower
```

This command installs the upower package, which provides the UPower daemon.

3. After installing the UPower daemon, start the service using the following command:

```bash
sudo systemctl start upower.service
```

4. Verify that the UPower daemon is now running by checking the status using the following command:

```bash
systemctl status upower.service
```

5. Restart your Flask application and try again. The error message should no longer appear.

Note that the specific steps for installing and starting the UPower daemon may vary depending on your system and distribution. You may need to consult the documentation or package manager for your system to find the appropriate package and commands to install and start the UPower daemon.

### Error: Ubuntu: SSL: Handshake failed error when browsing local web site in google-chrome from Ubuntu

Problem:  When browsing https://127.0.0.1:5000 receive error: SSL: Handshake failed. when logged into ZScaler

[39102:39117:0503/091443.791015:ERROR:ssl_client_socket_impl.cc(992)] handshake failed; returned -1, SSL error code 1, net_error -202
[39102:39117:0503/091447.197078:ERROR:ssl_client_socket_impl.cc(992)] handshake failed; returned -1, SSL error code 1, net_error -202
[39102:39117:0503/091447.998238:ERROR:ssl_client_socket_impl.cc(992)] handshake failed; returned -1, SSL error code 1, net_error -202
[39062:39086:0503/091448.177119:ERROR:cert_issuer_source_aia.cc(134)] AiaRequest::OnFetchCompleted got error -301
[39062:39086:0503/091448.178211:ERROR:cert_issuer_source_aia.cc(134)] AiaRequest::OnFetchCompleted got error -301
[42678:42704:0503/093402.088689:ERROR:cert_verify_proc_builtin.cc(677)] CertVerifyProcBuiltin for clientservices.googleapis.com failed:
----- Certificate i=2 (CN=NCA-DPI1,OU=ITSO,O=Centers for Disease Control and Prevention,L=Atlanta,ST=Georgia,C=US) -----
ERROR: No matching issuer found

[39062:39086:0503/091448.178351:ERROR:cert_verify_proc_builtin.cc(677)] CertVerifyProcBuiltin for optimizationguide-pa.googleapis.com failed:
----- Certificate i=2 (CN=NCA-DPI1,OU=ITSO,O=Centers for Disease Control and Prevention,L=Atlanta,ST=Georgia,C=US) -----
ERROR: No matching issuer found

Solution:  

1. Verify that your Python installation has a valid CA bundle that can be used to verify the SSL/TLS certificate. You can do this by running the following command in your terminal:

```bash
python -c "import ssl; print(ssl.get_default_verify_paths())"
```

This should print out the paths to the CA bundle and the OpenSSL configuration file used by Python. If the paths are not found or are invalid, you may need to update your Python installation or install a valid CA bundle.

Path should return

```bash
/usr/lib/ssl/certs
```

2. Download the missing CA certificate from the server that issued the certificate. You can use the openssl s_client command to retrieve the certificate, like this:

```bash
cd $HOME
openssl s_client -showcerts -connect clientservices.googleapis.com:443 </dev/null 2>/dev/null | openssl x509 -outform PEM > clientservices.googleapis.com.crt
openssl s_client -showcerts -connect optimizationguide-pa.googleapis.com:443 </dev/null 2>/dev/null | openssl x509 -outform PEM >  optimizationguide-pa.googleapis.com.crt
openssl s_client -showcerts -connect safebrowsing.googleapis.com.com:443 </dev/null 2>/dev/null | openssl x509 -outform PEM >  safebrowsing.googleapis.com.crt
openssl s_client -showcerts -connect accounts.google.com:443 </dev/null 2>/dev/null | openssl x509 -outform PEM >  accounts.google.com.crt
openssl s_client -showcerts -connect update.googleapis.com:443 </dev/null 2>/dev/null | openssl x509 -outform PEM >  update.googleapis.com.crt
openssl s_client -showcerts -connect www.google.com:443 </dev/null 2>/dev/null | openssl x509 -outform PEM >  www.google.com.crt
 dns.google
```

3. Install the CA certificate in your system's trusted CA store by copying it to the /usr/local/share/ca-certificates/ directory:
    
```bash
sudo cp clientservices.googleapis.com.crt /usr/local/share/ca-certificates/
sudo cp optimizationguide-pa.googleapis.com.crt /usr/local/share/ca-certificates/
sudo cp  safebrowsing.googleapis.com.crt /usr/local/share/ca-certificates/
sudo cp accounts.google.com.crt /usr/local/share/ca-certificates/
sudo cp update.googleapis.com.crt /usr/local/share/ca-certificates/
sudo cp www.google.com.crt /usr/local/share/ca-certificates/
```

4. Update the CA bundle by running the following command:

```bash
sudo update-ca-certificates
```


### Error: Ubuntu: CURL: SSL: Certificate problem: unable to get local issuer certificate when installing docker

Symptom:  Receive error: curl: (60) SSL certificate problem: unable to get local issuer certificate when installing docker

Reference: [Stack Overflow](https://stackoverflow.com/questions/72167566/wsl-docker-curl-60-ssl-certificate-problem-unable-to-get-local-issuer-certi)

Details:

The problem may be related to the way the firewall is handling certificates. The certificate of the firewall may be untrusted/unknown from within the wsl environment.

Resolution:

Option 1:

1. If logged into zscaler, log out
2. Try Again

Option 2:

Export the firewall certificate.

1. Export the firewall certificate from the windows certmanager (certmgr.msc).
2. The certificate may be located at "Trusted Root Certification Authorities\Certifiactes"
3. Export the certificate ZScaler Root CA as a DER coded x.509 and save it under e.g. "_templates/certs/zscaler.cer".

Configure WSL.

        open wsl terminal from VS Code : should default to Ubuntu: directory "/Users/zfi4/OneDrive - CDC/DAVT Analytics/davt-dev-jcbowyer"

```sh
wsl
openssl x509 -inform DER -in _templates/certs/zscaler.cer -out ./zscaler.crt
sudo cp zscaler.crt /usr/local/share/ca-certificates/
sudo update-ca-certificates
```

### Error: Ubuntu: Python installation error: ImportError: No module named apt_pkg

Problem: Python installation error: ImportError: No module named apt_pkg occurs when running sudo apt-get update

Reference: [Stack Overflow](https://stackoverflow.com/questions/13708180/python-dev-installation-error-importerror-no-module-named-apt-pkg)

Solution:

    ```sh
    sudo apt remove python3-apt
    sudo apt autoremove
    sudo apt autoclean
    sudo apt install python3-apt
    ```

### Error: Ubuntu: NPM can't find module "semver" error in Ubuntu 19.04

Problem: NPM can't find module "semver" error in Ubuntu 19.04 when installing nodejs upgrade

Reference: [AskUbuntu](https://askubuntu.com/questions/1152570/npm-cant-find-module-semver-error-in-ubuntu-19-04)

Solution:

Run the following commands to uninstall node:

```sh
cd $HOME
sudo rm -rf /usr/local/bin/npm /usr/local/share/man/man1/node* ~/.npm
sudo rm -rf /usr/local/lib/node*
sudo rm -rf /usr/local/bin/node*
sudo rm -rf /usr/local/include/node*
sudo apt-get purge nodejs npm
sudo apt autoremove
```

Run the following commands to reinstall node:

```sh
workon OCIO_PADE_DEV
cd $VIRTUAL_ENV
rm -rf /usr/local/bin/npm /usr/local/share/man/man1/node* ~/.npm
rm -rf /usr/local/lib/node*
rm -rf /usr/local/bin/node*
rm -rf /usr/local/include/node*

# install node with nvm - node version manager
# wget https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh
# chmod +x install.sh
# ./install.sh
# source ~/.bashrc
# nvm list-remote

# install node with wget
wget https://nodejs.org/dist/v18.12.1/node-v18.12.1-linux-x64.tar.xz
tar -xf node-v18.12.1-linux-x64.tar.xz
rsync -av  node-v18.12.1-linux-x64/bin/* ./bin
rsync  -av  node-v18.12.1-linux-x64/lib/node_modules/ ./lib/node_modules/
cd $VIRTUAL_ENV/bin

hash -r

# Verify installation using
node -v
npm -v

npm install puppeteer
npm install npm@9.1.2
npm install  @mermaid-js/mermaid-cli

sudo apt-get update
sudo apt-get install -y libgbm-dev
```

### Error: VSCode: End of line character is invalid

Symptom: Receiving error: "End of line character is invalid"

Reference: [Boot.dev Blog](https://blog.boot.dev/clean-code/line-breaks-vs-code-lf-vs-crlf/#:~:text=At%20the%20bottom%20right%20of,has%20the%20correct%20line%20breaks.)

Solution for One File:

Unless you work on a Windows-only team, the answer is almost always to change all your code to the Unix default of LF.

1. Open VS Code and go the the bottom right of the screen in VS Code
2. Click the button that says LF or CRLF and change to LF (most all cases)

Soulution for All New Files:

For Workspace Tab

1. Open VS Code
2. Open File Menu > Preferences > Settings
3. Search for CRLF
4. Change Files: EOL Setting to LF

For User Tab

1. Open VS Code
2. Open File Menu > Preferences > Settings
3. Search for CRLF
4. Change Files: EOL Setting to LF

Solution for All Existing Files

1. Download VS Code Exntension: [Change LF to CRLF](https://marketplace.visualstudio.com/items?itemName=stkb.rewrap)

### Problem: WSL: Github clone fails: "fatal: unable to access 'https://github.com/cdcent/data-ecosystem-services.git': Could not resolve host: github.com':"

Symptom: Trying to clone a github repository and receive error: "fatal: unable to access Could not resolve host: github.com "

Reference: [Stack Overflow](https://stackoverflow.com/questions/20370294/git-could-not-resolve-host-github-com-error-while-cloning-remote-repository-in)

Resolution:

Option 1:

1. Restart Wifi

Option 2:

1. Run terminal command in WSL:

```sh
git config --global --unset https.proxy
```

2. Restart Terminal in WSL:

Option 3:

1. Log Off ZScaler
2. Try again

Option 4:

1. Log Back into ZScaler
2. Try again

Option 5:

Fix wrong/empty /etc/resolv.conf file.

To view contents of /etc/resolv.conf file:

```sh
code  /etc/resolv.conf
```

To fix:

```sh
sudo rm /etc/resolv.conf
sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
sudo bash -c 'echo "[network]" > /etc/wsl.conf'
sudo bash -c 'echo "generateResolvConf = false" >> /etc/wsl.conf'
sudo chattr +i /etc/resolv.conf
```

### Problem: WSL: "Logon failure: the user has not been granted the requested logon type at this computer."

Symptom: Trying to connect to WSL from Windows Terminal and receive error: "Logon failure: the user has not been granted the requested logon type at this computer."

Reference: [Stack Overflow](https://stackoverflow.com/questions/62681041/ubuntu-18-04-on-wsl2-logon-failure-the-user-has-not-been-granted-the-requeste)

Solution:

1. Open Powershell as Administrator
2. Run the following command:

```sh
Get-Service vmcompute | Restart-Service
```

### Problem: WSL: Windows: Shell Script keeps exiting unexpectedly

Symptom:  WSL windows keeps exiting unexpectedly

Reference: [SuperUser](https://superuser.com/)

Details:

1. Examine your wsl -l -v output
2. It may show that the docker-desktop-data instance got set as the default when you uninstalled Ubuntu.
3. Docker-desktop-data is not a bootable instance, since it has no /init in it.

Resolution with Powershell or CMD:

```sh
wsl --set-default Ubuntu-20.04
```
