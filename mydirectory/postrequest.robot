*** Settings ***
Library     RequestsLibrary
Library    JSONLibrary


*** Variables ***
${baseurl}=     https://reqres.in
${endpoint}=    /api/users
${Json_Path}=   C:/Users/dell/PycharmProjects/pythonProject/mydirectory/testdata.json

*** Test Cases ***
testcasePostreq:
        Create Session    post    ${baseurl}
        ${input_json}      Load JSON From File     ${Json_Path}
        ${response}        POST On Session     post   ${endpoint}     ${input_json}
        Log To Console    ${response.json()}
        Log To Console    ${response.status_code}
        Log To Console    ${response.content}
        ${response_body}    Set Variable    ${response.json()}
        Should Be Equal As Strings    ${response.status_code}    201
        Should Be Equal As Strings    ${response_body['name']}    Swati
        ${name}=    Get Value From Json    ${response_body}    $.name
        Log To Console    ${name}
        Log To Console    ${input_json}
        
         