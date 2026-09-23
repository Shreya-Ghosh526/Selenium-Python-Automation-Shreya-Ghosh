*** Settings ***
Library    BuiltIn
Library    custom_library.py

*** Test Cases ***
Custom Python Keyword Test
    ${result}=    Calculate Sum    10    20
    Should Be Equal As Numbers    ${result}    30

BuiltIn Mathematical Operation Test
    ${result}=    Evaluate    15 * 4
    Should Be Equal As Numbers    ${result}    60