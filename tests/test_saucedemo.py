def test_saucedemo_homepage(driver):
    driver.get("https://www.saucedemo.com/")

    assert "Swag Labs" in driver.title