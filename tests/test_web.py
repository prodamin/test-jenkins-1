import allure

@allure.story('epic_1')
@allure.title("Parameterized test title")
def test_true():
    """true"""

    assert True

@allure.story('epic_2')
@allure.feature('feature_2')
def test_false():
    assert True

@allure.feature('feature_3')
def test_failed():
    assert False
