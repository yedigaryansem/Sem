from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException


def autogoing_to_cars_page(driver):
    first_window = driver.find_element_by_xpath('//*[@id="menu"]/div/div[1]')
    action1.move_to_element(first_window).perform()
    second_window = driver.find_element_by_xpath('//*[@id="menu"]/div/div[1]/div/div/span[2]/a')
    action1.move_to_element(second_window).perform()
    third_window = driver.find_element_by_xpath('//*[@id="menu"]/div/div[1]/div/div/span[2]/div/div[1]/div[1]/a[1]')
    third_window.click()
    action1.reset_actions()


def go_last_page(driver):
    a = driver.find_elements_by_xpath('/html/body/div[3]/div[4]/div[2]/div[*]/div[2]/a')
    count = 0
    while len(a) > 0:
        # find_all_auto_names(driver)
        count += 1
        time.sleep(1)
        a[0].click()
        a = driver.find_elements_by_xpath('/html/body/div[3]/div[4]/div[2]/div[*]/div[2]/a[2]')
    return count


def count_cars_in_page(driver):
    page_auto_list = driver.find_elements_by_xpath('//*[@id="contentr"]/div[*]/div[1]/a[*]')
    return len(page_auto_list)


def find_all_car_names(driver):
    a = driver.find_elements_by_xpath('//*[@id="contentr"]/div[3]/div[1]/a[*]')
    for i in range(len(a)):
        b = a[i].find_element_by_xpath(f'/html/body/div[3]/div[4]/div[2]/div[3]/div[1]/a[{i + 1}]/div[3]') \
            if a[i].find_element_by_xpath(
            f'/html/body/div[3]/div[4]/div[2]/div[3]/div[1]/a[{i + 1}]/div[1]').text == "Դիլեր" \
               or a[i].find_element_by_xpath(
            f'/html/body/div[3]/div[4]/div[2]/div[3]/div[1]/a[{i + 1}]/div[1]').text == "Շտապ!" \
            else a[i].find_element_by_xpath(f'/html/body/div[3]/div[4]/div[2]/div[3]/div[1]/a[{i + 1}]/div[2]')
        print(b.text)


def car_count(driver):
    first_page_car_count = count_cars_in_page(driver)
    pages_count = go_last_page(driver)
    last_page_car_count = count_cars_in_page(driver)

    total_cars_count = first_page_car_count * pages_count + last_page_car_count
    return total_cars_count
    # print(first_page_car_count, pages_count, last_page_car_count)


def car_mark(driver, mark):
    mark_type = driver.find_element_by_xpath('//*[@id="bList"]')
    mark_type.click()
    mark_type.send_keys(mark)
    mark_type.click()


def liking(driver):
    time.sleep(1)
    random_car = driver.find_element_by_xpath(
        '/html/body/div[3]/div[*]/div[2]/div[@class="dl"]/div[@class="gl"]/a[1]/img')
    action2 = ActionChains(driver)
    action2.move_to_element(random_car).perform()
    action2.reset_actions()
    # time.sleep(2)
    liker = driver.find_element_by_xpath('//*[@id="star"]/div')
    liker.click()
    time.sleep(1)
    try:
        checker = driver.find_element_by_xpath('//*[@id="dialog"]/div[2]')
        # print(checker.text)
        if checker.text == 'Խնդրում ենք մուտք գործեք կամ գրանցվեք, որպեսզի կարողանաք ավելացնել ընտրածների մեջ:':
            enter = driver.find_element_by_xpath('//*[@id="dialog"]/div[3]/a')
            enter.click()
            login(driver, True)
    except NoSuchElementException:
        # print("U alredy logined")
        print("")

def login(driver, check):
    login = driver.find_element_by_xpath('//*[@id="_idyour_email"]')
    login.click()
    login.send_keys("loginpa@mail.ru")
    password = driver.find_element_by_xpath('//*[@id="_idpassword"]')
    password.click()
    password.send_keys('123456qweasd')
    # time.sleep(2)
    enter = driver.find_element_by_xpath('//*[@id="loginaction__form_action0"]')
    enter.click()
    if check:
        car_mark(driver, mark)
        liking(driver)


def checker(driver):
    login_icon = driver.find_element_by_xpath('//*[@id="ma"]/img')
    action2 = ActionChains(driver)
    action2.move_to_element(login_icon).perform()
    favourite_publications = driver.find_element_by_xpath('//*[@id="ma"]/div/a[5]/div[2]')
    favourite_publications.click()
    # favourite_autos = driver.find_element_by_xpath('//*[@id="contentr"]/div')
    # for i in range(len(favourite_autos)):
    #     favourite_autos[i].find_element_by_xpath('//*[@id="contentr"]/div/a[3]/div[1]/div[1]')
    #     if favourite_autos[i].text == item_name_for_checking:
    #         return "YOur avto avelation"
    # return "item is not avelation"


# mark = str(input("PLease Enter auto mark: "))
driver = webdriver.Chrome()
# driver.maximize_window()
# action1 = ActionChains(driver)
# driver.get("https://www.list.am/")
# autogoing_to_cars_page(driver)
# car_mark(driver, mark)
# print(mark, car_count(driver), 'Штук')
# liking(driver)
# checker(driver)
# # print(checker(driver, check_value))
# # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")




driver.get("https://www.list.am/category/23/9?bid=5&crc=-1&n=0")
a = driver.find_element_by_xpath('/html/head/link[3]')
print(type(a.get_attribute("href")))






















