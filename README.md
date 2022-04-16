# CSI2132 - DCSM Project

This project is being developed for the CSI2132 course offered at the university of Ottawa.

The DCMS web app is a Flask REST API which allows the user to post, retrieve, modify and delete users and patients in the database.
It also allows the user to create appointments and retrieve required patient/procedure information.

This repository also contains the front end code for the project. 

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#dev-environment">Dev Environment</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

Listed below are the frameworks and database used for this project.

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [PostgreSQL](https://www.postgresql.org/docs/)
* [PyTest](https://docs.pytest.org/en/stable/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

The `requirements.txt` file contains all the necessary frameworks and libraries. To download the prerequisites, run the following command (uses `pip`):
  ```sh
  pip install -r requirements.txt
  ```

If any new requirements have been installed, run the following command (uses `pip`) to add them to the `requirements.txt` file:
  ```sh
  pip freeze > requirements.txt
  ```
  
### Dev Environment
- `python -v` 3.9 or greater
- To clone the repo: `git clone https://github.com/amirfanous/DCMS-CSI2132`
- Change the current working directory to the local project root and run (only required for the first time):
    - Mac: `python3 -m venv venv`
    - Windows: `python -m venv venv`
- To start the virtual environment:
    - Mac: `source venv/bin/activate`
    - Windows: `source venv/scripts/activate`
- Set the environment variables for the database:
  - `'DB_NAME' = "dfkjl7dui72stg"`
  - `'DB_USERNAME' = "pmhsdddzxbeguh"`
  - `'DB_PASSWORD' = *contact repo owner for password*`
  
- To run the app: `python3 app.py`



<!-- CONTACT -->
## Contact

Shahir Mikhail - [LinkedIn](https://linkedin.com/in/shahirmikhail) - shahir.mikhail@gmail.com

