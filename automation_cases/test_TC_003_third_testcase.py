import pytest


# Fixture that will run before test case
# To declare it as a fixture, we use the @pytest.fixture() decorator
# To execute it, we pass it as an argument to the test case we want to run
# To execute code after the test case is finished, we use yield keyword and put code after it
# yield can return anything we want
# Scope allow us to configure if we want the fixture to run:
#       - on each test case (scope="function")
#       - on each python module (scope="module")
#       - on .... (scope="session")


@pytest.fixture(scope="module")
def fixture_code():
    print("This is our fixture code that will run before the test case")
    print("-----------------------------------------------------------")
    yield  # The code after yield is the fixture to run after the test case execution ends
    print("Closing dB connection after test case execution")
    print("-----------------------------------------------------------")

@pytest.mark.Smoke
def test_tc_001_login_logout(fixture_code):
    print("This is our Smoke test case...")
    print("This is end of test case 1")



@pytest.mark.Sanity
def test_tc_003_login_logout_invalid_credentials(fixture_code):
    print(" This is Sanity test case")
    print("This is end of test case 3")