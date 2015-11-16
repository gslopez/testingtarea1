*** Settings ***
Documentation     Example test cases using the keyword-driven testing approach.
...
...               All tests contain a workflow constructed from keywords in
...               ``FuncLibrary.py``. Creating new tests or editing
...               existing is easy even for people without programming skills.
...
...               The _keyword-driven_ appoach works well for normal test
...               automation, but the _gherkin_ style might be even better
...               if also business people need to understand tests. If the
...               same workflow needs to repeated multiple times, it is best
...               to use to the _data-driven_ approach.
Library           FuncLibrary.py

*** Test Cases ***

#get_func_args(self,func, stripself=False):

# Caso 1
Get Arguments of None
    Should Cause Error    ${None}  ${False}

# Caso 2
Get Arguments of function with strip
    ${func} =  Get Function  2
    ${expected} =  Create List  b  c

    Get Arguments    ${func}  ${True}
    Result Should Be    ${expected}

# Caso 3
Get Arguments of function with default values
    ${func} =  Get Function  1
    ${expected} =  Create List  a  b  c

    Get Arguments    ${func}  ${False}
    Result Should Be    ${expected}

# Caso 4
Get Arguments of class with constructor
    ${func} =  Get Standard Class
    ${expected} =  Create List  a  b  c

    Get Arguments    ${func}  ${False}
    Result Should Be    ${expected}

# Caso 5
Get Arguments of class method
    ${func} =  Get Class Method
    ${expected} =  Create List  a  b  c

    Get Arguments    ${func}  ${False}
    Result Should Be    ${expected}

# Caso 6
Get Arguments of Enumerable Class
    ${func} =  Get Enumerable Class
    ${expected} =  Create List

    Get Arguments    ${func}  ${False}
    Result Should Be    ${expected}

# Caso 7
Get Arguments of Partial Method
    ${func} =  Get Partial  1
    ${expected} =  Create List  b  c

    Get Arguments    ${func}  ${False}
    Result Should Be    ${expected}

# Caso 8
Get Arguments of String method
    ${func} =  Get String Method
    ${expected} =  Create List

    Get Arguments    ${func}  ${False}
    Result Should Be    ${expected}

# Caso 9
Get Arguments of Method Descriptor
    ${func} =  Get Method Descriptor
    ${expected} =  Create List

    Get Arguments    ${func}  ${False}
    Result Should Be    ${expected}

# Caso 10
Get Arguments of Item Getter
    ${func} =  Get Item Getter
    ${expected} =  Create List

    Get Arguments    ${func}  ${False}
    Result Should Be    ${expected}
