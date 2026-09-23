*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.saucedemo.com/

*** Test Cases ***
Open Browser And Navigate To Website
    Open Browser    ${URL}    Chrome
    Maximize Browser Window
    Sleep    2s
    [Teardown]    Close All Browsers

Fill Login Form
    Open Browser    ${URL}    Chrome
    Maximize Browser Window
    Input Text    id=user-name    standard_user
    Input Text    id=password    secret_sauce
    Sleep    2s
    [Teardown]    Close All Browsers

Verify Element On Webpage
    Open Browser    ${URL}    Chrome
    Maximize Browser Window
    Page Should Contain Element    id=login-button
    Sleep    2s
    [Teardown]    Close All Browsers