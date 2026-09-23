*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=login_data.csv

Test Template    Login With Different Users
Test Teardown    Close All Browsers

*** Variables ***
${URL}    https://www.saucedemo.com/

*** Test Cases ***
Login Test    Default User    Default Password

*** Keywords ***
Login With Different Users
    [Arguments]    ${username}    ${password}
    Open Browser    ${URL}    Chrome
    Maximize Browser Window
    Input Text    id=user-name    ${username}
    Input Text    id=password    ${password}
    Click Button    id=login-button
    Page Should Contain Element    class=title
    Sleep    2s