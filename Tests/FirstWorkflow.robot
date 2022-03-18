*** Settings ***
Documentation       First Demo Script with Robot Framework
Library             SeleniumLibrary
Library             ../Resource/HRM_Login.py
Library             ../Resource/HRM_Admin.py

*** Variables ***
${User}             Aravind

*** Keywords ***
myNote
    [Documentation]  All Keywords are available in their respective resource files

*** Test Cases ***
Orange HRM Login
    Open Browser to Login Page
    Enter Login Details
    Submit Credentials
    HRM page should be open

Administration
    Go to Admin Tab
    Search for Username
    Select search results
    Cancel Edit
