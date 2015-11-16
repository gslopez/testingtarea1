*** Settings ***
Documentation     Example test cases using the keyword-driven testing approach.
...
...               All tests contain a workflow constructed from keywords in
...               ``CACCLibrary.py``. Creating new tests or editing
...               existing is easy even for people without programming skills.
...
...               The _keyword-driven_ appoach works well for normal test
...               automation, but the _gherkin_ style might be even better
...               if also business people need to understand tests. If the
...               same workflow needs to repeated multiple times, it is best
...               to use to the _data-driven_ approach.
Library           CACCLibrary.py

*** Test Cases ***

# Caso 1: 
All True
    ${log1} =  Get Module 1
    ${spider_1} =  Get Spider 1
    ${expected} =  Create List  ${spider_1}
    
    All True Case    ${log1}

    Result Should Be    ${expected}

# Caso 2:
B False Others True
    ${log2} =  Get Module 2
    ${expected} =  Create List

    B False Others True Case    ${log2}

    Result Should Be    ${expected}

# Caso 3:
C False Others True
    ${log3} =  Get Module 3
    ${expected} =  Create List

    C False Others True Case    ${log3}

    Result Should Be    ${expected}

# Caso 3:
D False Others True
    ${log4} =  Get Module 4
    ${expected} =  Create List

    D False Others True Case    ${log4}

    Result Should Be    ${expected}
