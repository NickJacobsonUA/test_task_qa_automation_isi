Importing Libraries:

pytest, 
webdriver, 
By, 
Service as ChromeService, 
ChromeDriverManager, 
WebDriverWait, 
expected_conditions as EC, 
ActionChains, 
dataclass, 

Notice: All the libraries can be installed by using them in a way:
from ____ import ____ or via:
>pip install "library name"

To import ChromeDriverManager type in terminal: 
> pip install webdriver_manager


Allure reports software setting:

1. Install "Scoop" via Powershell (Windows)
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

or Install "Homebrew" for iOS/Linux

> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"


2. Install Java version 8 or above for your OS(make sure you set the JAVA_HOME variable while installing)


3. Run in terminal
> scoop install allure

4. Make sure allure works by running the command
>allure --version

5. Setting the folder for your reports and start the tests:
>pytest --alluredir=tests\allure_results .\tests\alerts_test.py

6. After the tests are over you can find the reports in the folder you previously set. 


7. To generate the allure reports (encrypted ones aren't readable) run in terminal:
> allure serve .\tests\allure_results\

8. You will be automatically redirected to the Allure PebPage with the results

