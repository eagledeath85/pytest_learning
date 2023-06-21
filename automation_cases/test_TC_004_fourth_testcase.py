import pytest



@pytest.mark.Smoke
def test_tc_001_login_logout():
    print("This is Smoke test...")
    print("This is end of test case 1")


@pytest.mark.Sanity
def test_tc_003_login_logout_invalid_credentials():
    print(" This is Sanity test")
    print("This is end of test case 3")