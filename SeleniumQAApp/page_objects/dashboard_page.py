from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from tabulate import tabulate


class DashboardPage:
    __dashboard_url = (By.XPATH, "//div[@id='navbarSupportedContent']//a[@href='/dashboard']")
    __header_texts = (By.CSS_SELECTOR, ".mb-3.text-center.text-primary")
    __table_row_data = (By.XPATH, "/html//div[@id='root']/div[@class='App']//table[@class='table']//th")
    __table_col_data = (By.XPATH, "//table[@class='table']//tbody/tr/td[1]")
    __table_data = (By.CLASS_NAME, "table")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self):
        return self._driver.current_url

    def get_contact_title(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(e.presence_of_element_located(self.__header_texts))
        return self._driver.find_element(*self.__header_texts).text

    def get_table_data(self):
        wait = WebDriverWait(self._driver, 10)
        table = wait.until(e.presence_of_element_located((By.XPATH, "//table")))

        headers = [header.text for header in table.find_elements(By.XPATH, ".//th")]

        rows = table.find_elements(By.XPATH, ".//tr")
        data = []
        for row in rows[1:]:
            row_data = [cell.text for cell in row.find_elements(By.XPATH, ".//td")]
            data.append(row_data)

        print("The following data is shown from the table:")
        print(tabulate(data, headers=headers, tablefmt="grid"))