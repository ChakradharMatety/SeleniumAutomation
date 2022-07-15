behave -f allure_behave.formatter:AllureFormatter -o reports/ features
allure serve reports

pytest -v -s --alluredir="C:\Users\dell\PycharmProjects\pythonProject\allureReports" pyTest\test_three.py
allure serve allureReports
allure serve allureReports C:\Users\dell\PycharmProjects\pythonProject\allureReports


