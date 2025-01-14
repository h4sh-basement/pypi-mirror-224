import re
import time
import logging
from hapanapi.driver_tools import driver_init, CHROME_PATH, CHROME_BIN
from hapanapi.parsers import schedule_date_parser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger("HapanaINIT")


class Hapana:
    def __init__(self, username, password, driver=None):
        self.username = username
        self.password = password
        if not driver:
            self.driver = driver_init(CHROME_PATH=CHROME_PATH, CHROME_BIN=CHROME_BIN)
        else:
            self.driver = driver

        # First Timer Report
        self.trial_present_sessions = {}

    def login(self, platform='core'):
        self.driver.get(f"https://{platform}.hapana.com/")
        if platform == 'grow':
            logger.info("Unable to login, please re-code this again")
        else:
            signin_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'signin')))
            self.driver.find_element(By.NAME, 'email').send_keys(self.username)
            self.driver.find_element(By.NAME, 'password').send_keys(self.password)
            signin_button.click()
        time.sleep(2)

    def add_client(self, first_name, last_name, email, phone, platform='core'):
        if platform == 'core':
            self.driver.get("https://core.hapana.com/index.php?route=dashboard/clients/addclientnewpayment&pageurl=clients&from=home")
            time.sleep(2)
            self.driver.find_element(By.ID, 'first_name').send_keys(first_name)
            self.driver.find_element(By.ID, 'last_name').send_keys(last_name)
            self.driver.find_element(By.ID, 'email').send_keys(email)
            self.driver.find_element(By.ID, 'phone').send_keys(phone)
            self.driver.find_element(By.ID, "btn-add-client").click()
            time.sleep(2)
        elif platform =='grow':
            self.driver.get("https://grow-api.hapana.com/widget/form/vIYNBYCfx0mIl8DJr1fL")
            time.sleep(1)
            self.driver.find_element(By.NAME, 'first_name').send_keys(first_name)
            self.driver.find_element(By.NAME, 'last_name').send_keys(last_name)
            self.driver.find_element(By.NAME, 'email').send_keys(email)
            self.driver.find_element(By.NAME, 'phone').send_keys(phone)
            self.driver.find_element(By.CLASS_NAME, "btn").click()
            time.sleep(2)
        else:
            logger.info("Wrong platform specified, client not added")

    def find_client(self, email=None, phone=None, platform='core'):
        if platform == 'core':
            self.driver.get("https://core.hapana.com/index.php?route=dashboard/clients")
            time.sleep(2)
            if email:
                search_term = email
            elif phone:
                search_term = phone
            else:
                logger.error("Did not specify email or phone, unable to search")
                return None
            searchbar = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'clientsearch')))
            searchbar.send_keys(search_term)
            time.sleep(4)
            client_table = self.driver.find_elements(By.XPATH, f"//tbody[@id='clientresults']/tr")
            if len(client_table) < 1:
                logger.error(f"{search_term} is not found in {platform}!")
                return None
            else:
                first_client = client_table[0]  # TODO verify with phone number as well
                cols = first_client.find_elements(By.TAG_NAME, "td")
                client_link = cols[1].get_attribute('onclick')
                client_link = client_link.replace("window.location.href=", "").strip("'")
                return client_link
        else:
            logger.error(f"The current platform {platform} is not supported")
            return None

    def find_membership(self, client_page):
        self.driver.get(client_page)
        time.sleep(2)
        all_memberships = self.driver.find_elements(By.XPATH, f"//form[@id='recpayform']/table/tbody[@id='resultsrec']/tr")
        if len(all_memberships) < 1:
            logger.error("Can't find membership for this user!")
            return None
        else:
            for item in all_memberships:
                package_type = item.find_element(By.XPATH, "//td[@class='pkgType']/span").get_attribute('innerText')
                if package_type != "Active" and package_type != "Suspended":
                    package_link = None
                    continue
                else:
                    package_link = item.find_element(By.XPATH, "//td[@class='transaction-action']/a").get_attribute('href')
                    return package_link
            if not package_link:
                logger.error("No package found!")
                return package_link

    def pause_membership(self, package_page, start_date=None, end_date=None):
        self.driver.get(package_page)
        self.driver.find_element(By.XPATH, "//i[@data-target='#editStatus']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, 'set_payment_status').click()
        status_update_options = self.driver.find_elements(By.XPATH, "//select[@id='set_payment_status']/option")
        for option in status_update_options:
            if option.get_attribute("innerText") == "Suspended":
                option.click()
                break
        if start_date:
            self.driver.find_element(By.ID, "suspension_start_type").click()
            time.sleep(1)
            start_type_options = self.driver.find_elements(By.XPATH, "//select[@id='suspension_start_type']/option")
            for option in start_type_options:
                if option.get_attribute("innerText") == "On Date":
                    option.click()
                    break
            self.driver.find_element(By.ID, "suspension_date").click()
            day, month, year = start_date.split("/")
            self.datepicker(day=day, month=month, year=year)
        if end_date:
            self.driver.find_element(By.ID, "reactive_duration_type").click()
            time.sleep(1)
            end_type_options = self.driver.find_elements(By.XPATH, "//select[@id='reactive_duration_type']/option")
            for option in end_type_options:
                if option.get_attribute("innerText") == "On Date":
                    option.click()
                    break
            self.driver.find_element(By.ID, "reactivation_date").click()
            day, month, year = end_date.split("/")
            self.datepicker(day=day, month=month, year=year)
        time.sleep(1)
        self.driver.find_element(By.ID, "updateStatus").click()

    def datepicker(self, year, month, day,
                   year_tag="ui-datepicker-year", month_tag="ui-datepicker-month", day_tag="ui-datepicker-calendar"):
        # Year Picker
        self.driver.find_element(By.CLASS_NAME, year_tag).click()
        time.sleep(1)
        year_options = self.driver.find_elements(By.XPATH, f"//select[@class='{year_tag}']/option")
        for option in year_options:
            if option.get_attribute("innerText") == str(year):
                option.click()
                break
        # Month Picker
        self.driver.find_element(By.CLASS_NAME, month_tag).click()
        time.sleep(1)
        month_options = self.driver.find_elements(By.XPATH, f"//select[@class='{month_tag}']/option")
        for option in month_options:
            if option.get_attribute("value") == str(int(month)-1):
                option.click()
                break
        # Day Picker
        day_options = self.driver.find_elements(By.XPATH, f"//table[@class='{day_tag}']/tbody/tr/td")
        for option in day_options:
            if option.get_attribute("innerText") == str(day):
                option.click()
                break

    def schedule(self, date):
        today, day, day_of_week = schedule_date_parser(date)
        self.driver.get("https://core.hapana.com/index.php?route=dashboard/schedule")
        time.sleep(2)
        elems = self.driver.find_elements(By.XPATH,
                                          f"//div[@class='fc-content-skeleton']/table/tbody/tr[1]/td[{day_of_week}]/div[@class='fc-content-col']/div[@class='fc-event-container']/a")
        time.sleep(1)
        session_ids = [elem.get_attribute('href').split("=")[-1] for elem in elems]
        for session_id in session_ids:
            link = f"https://core.hapana.com/index.php?route=dashboard/schedule&seid={session_id}&dt={day}&eid={session_id}&curr={today}"
            self.driver.get(link)
            time.sleep(2)
            class_name = self.driver.find_element(By.XPATH, f"//div[@id='eventLoad']/div[1]/h4").text
            class_name = re.sub('[^A-Za-z0-9 ]+', '', class_name)
            user_table = self.driver.find_elements(By.XPATH,
                                              f"//ul[@id='attendeesList']/li[contains(@class,'d-lg-block')]")
            if len(user_table) < 1:
                logger.info(f"{class_name} is empty!")
            else:
                for item in user_table[1:]:
                    cols = item.find_elements(By.TAG_NAME, "div")
                    visits = cols[1].find_element(By.CLASS_NAME, "milestone").get_attribute('innerText')
                    try:
                        if int(visits) > 1:
                            continue
                    except Exception as e:
                        print(f"Error: {e} detected in {class_name}")
                        continue
                    name = cols[1].find_element(By.TAG_NAME, "a").get_attribute('innerText')
                    name = re.sub('[^A-Za-z0-9 ]+', '', name)
                    package_name = cols[5].find_element(By.TAG_NAME, "span").get_attribute('innerText')
                    if "ClassPass" in package_name:
                        package_name = "ClassPass"
                    else:
                        booked_sessions = re.findall("\(\d{1,}\/\d{1,}\)", package_name)
                        if len(booked_sessions) > 0:
                            booked_pattern = "\\" + booked_sessions[0][:-1] + "\\" + booked_sessions[0][-1]
                            package_name = re.sub(booked_pattern, '', package_name)
                            # num, denom = booked_sessions[0].strip("()").split("/")

                    # home_location = cols[1].find_element(By.XPATH, f"//span[@aria-label='Home Location Alert']")
                    # print(home_location.get_attribute('style'))
                    if class_name not in self.trial_present_sessions:
                        self.trial_present_sessions[class_name] = [
                            {"name": name, "package": package_name, "visits": int(visits)}]
                    else:
                        self.trial_present_sessions[class_name].append(
                            {"name": name, "package": package_name, "visits": int(visits)})
                    print({
                        "name": name,
                        "visits": visits,
                        "package": package_name
                    })
