import pytest


# Test case must be written inside a method.
# Method name must start with test_

# To display details about tests and their statuses, we can use the command 'pytest -v':
# pytest -v .\automation_cases\

# To display print() statements from our tests, we can use the command 'pytest -s':
# pytest -s -v .\automation_cases\

# To skip any specific test case, we need to add a specific decorator to it: @pytest.mark.skip
# To skip a test on a condition, whe use @pytest.mark.skipif(condition, reason="reason")

# To execute a specific test case within a folder, we use the syntax "-k test_name folder_name":
# pytest -s -v -k test_tc_001_login_logout .\automation_cases\

a = 100
expected_result = "Hello"

@pytest.mark.skip("Skipping as this functionality is not working")
@pytest.mark.skipif(a > 100, reason="Skipping as this functionality is not working")
def test_tc_001_login_logout():
    print("This is our test case code 1...")
    print("This is end of test case 1")
    assert expected_result == "Hello"


def test_tc_003_login_logout_invalid_credentials():
    print(" This is our test case 3")
    print("This is end of test case 3")
    actual_result = "Hello"
    assert expected_result != actual_result, f"actual result: {actual_result} and expected result: {expected_result}" \
                                             f" must be different"