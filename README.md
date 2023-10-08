# QA Automation of API requests with Pytest 

## Introduction

This QA Automation project uses Pytest to automate the testing of a API routes of a web application. Pytest is a popular testing framework in Python. This project aims to demonstrate how to set up and use Pytest for automated testing of API routes for web applications.

## Important

Unfrotrunately there is no posibility to run tests and get real tests results, since the access for the tested web application was already revoked. So this is mostly for demontrative and educational purposes.
Someone might find helpfull concepts and information in this project.
You can clone or fork the repository to access the code and use it for your own projects. 

## Project Structure

The project is organized into the following directories and files:

- `.github/workflows`: Contains Github Actions config files.
- `apis`: Contains the structure of api requests and their data devided by groups (based on routes).
- `notifications`: Contains file with the allure report configuration. In this case Telegram is used to get allure reports.
- `tests/`: Contains the test scripts written using Pytest.
- `allure-notifications-4.2.1.jar`: This is java plugin that allows to push tests results as an Allure report in the visual form to different messengers. More info here: https://github.com/qa-guru/allure-notifications
- `conftest.py`: Contains pytest fixtures. More info here: https://docs.pytest.org/en/7.4.x/how-to/fixtures.html
- `constants.py`: Contains sensitive data that is used in the testing process. Hided as env variables.
- `pytest:ini`: Pytest configuration file that helps to set your test environment.
- `README.md`: Documentation for the project. File that you are currently reading.
- `requirements.txt`: Lists the project dependencies.

## Test process explanation

The testing on the remote machine is completed via running GitHub Actions file
Check `.github/workflows/pytest.yml` file to understand the process.

1. Install Python and Project dependencies.
2. In this case VPN is used to access the web app, so VPN config Installation and Conncetion happen.
3. Then we run our tests.
4. Get allure history from the other branch (where allure reports hosted).
5. Deploy Allure report with the tests' results to the different branch (gh-pages).
6. Install Java for running .jar file later.
7. Overrite telegram.json file with the json containing chat_id and and telegram_token.
8. Run allure-notifications file to push test report in telegram group.


Thanks for checking this repo and feel free to reach me if you have any questions!