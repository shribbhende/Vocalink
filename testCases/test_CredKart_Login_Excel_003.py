import pytest

from pageObjects.Login_Page import Login_Page_Class
from utilities.Logger import log_generator_class
from utilities.ReadConfig import ReadConfigClass
from utilities import Excel_Utils

@pytest.mark.usefixtures("driver_setup")
class Test_Login_Excel_003:

    log = log_generator_class.loggen_method()
    login_url = ReadConfigClass.get_data_for_login_url()
    driver = None
    excel_path = ".\\TestData\\Test_Data.xlsx"
    sheet_name = "login_data"

    def test_CredKart_Login_Excel_003(self):
        self.log.info("Testcase test_CredKart_Login_Excel_003 is started")
        self.lp = Login_Page_Class(self.driver)
        self.log.info("Reading the data from excel file")
        self.rows = Excel_Utils.get_row_count( self.excel_path, self.sheet_name)
        self.log.info("Number of rows in excel file is: " + str(self.rows))
        Result_list =[]
        for i in range(2, self.rows + 1):
            self.log.info("Opening browser and landing on login page--" + self.login_url)
            self.driver.get(self.login_url)
            self.email = Excel_Utils.read_data(self.excel_path, self.sheet_name, i, 2)
            self.password = Excel_Utils.read_data(self.excel_path, self.sheet_name, i, 3)
            self.expected_result = Excel_Utils.read_data(self.excel_path, self.sheet_name, i, 4)
            self.log.info("Entering email--" + str(self.email))
            self.lp.Enter_Email(self.email)
            self.log.info("Entering password--" + self.password)
            self.lp.Enter_Password(self.password)
            self.log.info("Clicking on login button")
            self.lp.Click_Submit_Button()
            self.log.info("Verifying user login")
            if self.lp.verify_menu() == "Pass":
                self.log.info("User logged in successfully")
                self.log.info("Writing result to excel file")
                Excel_Utils.write_data(self.excel_path, self.sheet_name, i, 5, "Pass")
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(f".\\Screenshots\\test_CredKart_Login_Excel_003_{i}_{self.email}_pass.png")
                self.log.info("Clicking on menu button")
                self.lp.Click_Menu_Button()
                self.log.info("Clicking on logout link")
                self.lp.Click_Logout_Link()
                actual_result = "Pass"
            else:
                self.log.info("User not logged in")
                self.log.info("Writing result to excel file")
                Excel_Utils.write_data(self.excel_path, self.sheet_name, i, 5, "Fail")
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(f".\\Screenshots\\test_CredKart_Login_Excel_003_{i}_{self.email}_fail.png")
                actual_result = "Fail"

            if self.expected_result == actual_result:
                test_case_status = "Pass"
            else:
                test_case_status = "Fail"

            Result_list.append(test_case_status)
            self.log.info("Writing result to excel file")
            Excel_Utils.write_data(self.excel_path, self.sheet_name, i, 6, test_case_status)
            # self.log.info("Opening browser and landing on login page--" + self.login_url)
            # self.driver.get(self.login_url)

        if "Fail" not in Result_list:
            self.log.info("All the test cases passed")
            assert True
        else:
            self.log.info("Some test cases failed")
            assert False

        self.log.info("Testcase test_CredKart_Login_Excel_003 is completed")
