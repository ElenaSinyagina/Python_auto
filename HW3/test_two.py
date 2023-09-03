import time
from testpage import OperationHelper

username = "MaxMax2003"
password = "5cb3ca5359"

def test_step(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login(username)
    test_page1.enter_pswd(password)
    test_page1.click_button()

    time.sleep(3)

    test_page1.click_contact()

    time.sleep(3)

    test_page1.enter_cont_name("field_name")
    test_page1.enter_cont_email("email@gmail.ru")
    test_page1.enter_cont_text("field_text")

    time.sleep(1)

    test_page1.click_button()

    time.sleep(1)

    assert test_page1.get_alert_text() == "Form successfully submitted"