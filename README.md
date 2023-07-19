# Tenant Transaction Data Processor

## Project Overview

This project is designed with the objective to normalize tenant transaction data for a real estate company. The company deals with Excel files supplied by its clients, each encompassing a comprehensive report of every tenant's transactions. 

Currently, the data housed within these Excel files is unnormalized, posing challenges for any modeling processes. Previously, the tedious task of manual normalization for each file was carried out by the company's owner. This manual process is not only time-consuming but also prone to errors and inconsistencies.

The chief goal of this project is to devise a system that can automate the normalization process, saving valuable time and reducing potential errors, while enhancing the consistency and reliability of the data.

## Features
1. **Excel File Processing:** The project is capable of reading and processing Excel files, which is the format of the input data.

## Getting Started

To clone the repository, set up the environment, and run the project on your local system, please follow the installation and usage instructions detailed in the subsequent sections.

### Setting Up a Python Virtual Environment
- This project requires **Python 3.10** or higher. Please make sure you have the correct version installed before proceeding. You can check your Python version using the following command:
```bash
python3 --version
```

- Before starting with the project, it is recommended to set up a Python virtual environment. Here is how you can do it:

```bash
# Create a new virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

### Create environment variables
- Create a `.env` file containing the following values
```
DATABASE_URL=postgresql://{db_user}:{db_password}@db_server/db_name
SQLALCHEMY_DATABASE_URI='sqlite:///app.db'
SECRET_KEY='AStrongRandomKey'
```
- `db_user` is your Postgres database username
- `db_password` is the Postgres user password
- `db_server` is the Postgres database server e.g `localhost`

### Install project requirements packages
Install the required Python packages by running the following command
```bash
pip install -r requirements.txt
```

### Create database tables
This stage consists of creating the required tables where the Excel file data will be stored.
To proceed, the following commands must be executed.
**Note: Make sure the database for this project has been created ***
```bash
# Generate the alembic migration files
flask db migrate -m "a simple description of changes made"

# Apply the changes to the database
flask db upgrade
```

### Running the application
To Run the application, execute the following command, which will read the Excel (`.xls`, `.xlsx`) file present in the `data` folder, process and insert the data in Postgresql database previously created.
**Note:

```bash
make load
```
To view the data loaded to the database, there is an API endpoint that exposes the data based on the tenant ID accessible on localhost through the API endpoint below
`/api/v1/tenants/{tenant_id}/transactions`

Where `{tenant_id}` id is an integer corresponding to the primary key of the tenant table.

### Running unit tests
To execute the unit tests, type the following command

`make test`

## Potential update
A new feature can be added to automate the data normalization by executing this program as a cronjob at a given interval(perhaps every hour) to avoid the manual process of always executing the file when there is new data available from the client. 


