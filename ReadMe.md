##**Overview**
This document contains upload photo functionallity in kumu dev, prod, and staging environments
###**Pre-requisites**
1. Pycharm - 
2. Python - Coding language used
3. Allure 
4. Behave - BDD framework tool
5. brew 
6. Terminal
###**Installation of requirements**
    `pip install -r requirements.txt`
    
###**Test Workflow**
1. The test photo can be found/changed in **Upload.feature** file.
2. Environment and otp secret key are set on terminal.
3. Reports can be generated using **Allure**

### Execution steps via terminal

To run script and generate allure reports:

`behave -D env=dev -D otp_secret=<kumu secrect key> features/Upload.feature --no-capture --no-color -f allure_behave.formatter:AllureFormatter -o AllureReports
`

*Note: Select desired environment by replacing env=dev,prod or  stg*



