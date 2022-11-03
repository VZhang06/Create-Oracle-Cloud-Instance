from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def find_resource():
    driver_path = 'chromedriver.exe'
    driver = webdriver.Chrome(driver_path)
    driver.get('http://cloud.oracle.com/?region=us-sanjose-1')
    driver.maximize_window()
    user_name_path = '//*[@id="cloudAccountName"]'
    user_name = driver.find_element(By.XPATH, '//*[@id="cloudAccountName"]')
    user_name.send_keys()
    nxt_path = '/html/body/div[2]/section[2]/div/div/div/div[1]/div/div/div[3]/div[3]/div/a'
    nxt = driver.find_element(By.XPATH, '//*[@id="cloudAccountButton"]')
    nxt.click()
    sleep(5)
    email = driver.find_element(
        By.XPATH, '//*[@id="idcs-signin-basic-signin-form-username"]')
    email.send_keys()
    pwd = driver.find_element(
        By.XPATH, '//*[@id="idcs-signin-basic-signin-form-password|input"]')
    pwd.send_keys()
    sign_in = driver.find_element(By.XPATH, '//*[@id="ui-id-4"]')
    sign_in.click()
    sleep(6)
    enter_instance_path = '/html/body/section/div[1]/div[3]/main/div[1]/div[2]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[1]/a/span[1]'
    driver.find_element(By.XPATH, enter_instance_path).click()
    sleep(2)
    driver.refresh()
    sleep(3)
    WebDriverWait(
        driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.ID, "sandbox-compute-container")))
    driver.find_element(
        By.XPATH,
        ".//*[starts-with(@id,'active_compartment_select-')]//a").click()
    sleep(2)
    driver.find_element(
        By.XPATH,
        '/html/body/div[1]/div[1]/div/aside/div[3]/div/div[2]/div[1]/div/div/div/div/ul/div/div/li/label').click()
    sleep(2)
    driver.find_element(
        By.XPATH,
        '/html/body/div[1]/div[1]/div/div/div[2]/div/div[1]/button[1]').click()
    sleep(2)
    driver.find_element(
        By.XPATH,
        '//*[@id="oui-savant__viewstack__container"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/fieldset[2]/div[1]/div[2]/button').click()
    sleep(2)
    driver.find_element(
        By.XPATH,
        '//*[@id="oui-savant__viewstack__container"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/fieldset[2]/div[2]/div[1]/div[1]/div/div[2]/button').click()
    sleep(2)
    driver.find_element(
        By.XPATH,
        '//*[@id="oui-savant__viewstack__container"]/div[3]/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div/div[3]/div/div[2]/label').click()
    sleep(2)
    driver.find_element(
        By.XPATH,
        '//*[@id="oui-savant__viewstack__container"]/div[3]/div[2]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[1]/td[1]/input').click()
    driver.find_element(
        By.XPATH,
        '//*[starts-with(@id, "VM_Standard_A1_Flexcores")]').send_keys(
        Keys.CONTROL + 'a')
    driver.find_element(
        By.XPATH, '//*[starts-with(@id, "VM_Standard_A1_Flexcores")]').send_keys(Keys.DELETE)
    driver.find_element(
        By.XPATH,
        '//*[starts-with(@id, "VM_Standard_A1_Flexcores")]').send_keys('4')
    driver.find_element(
        By.XPATH,
        '//*[@id="oui-savant__viewstack__container"]/div[3]/div[2]/div/div[2]/div[3]/button[1]').click()
    sleep(1)
    driver.find_element(
        By.XPATH,
        '//*[@id="oui-savant__viewstack__container"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/fieldset[4]/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div/span[1]/button').click()
    driver.find_element(
        By.XPATH,
        '//*[@id="oui-savant__viewstack__container"]/div[2]/div[2]/div/div[2]/div[3]/button[1]').click()
    sleep(3)
    if driver.find_element(
            By.XPATH,
            './/*[starts-with(@id, "oui-savant__viewstack__container")]'):
        res = open('result.txt', 'a')
        res.write('No resources available %s.\n' %
                  (datetime.datetime.now()))
        res.close()
        driver.quit()
    else:
        sleep(50)
        res = open('result.txt', 'a')
        res.write('Yes! %s./n' %
                  (datetime.datetime.now()))
        res.close()
        driver.quit()


with open('result.txt') as f:
    if 'Yes' in f.read():
        f.close()
    else:
        find_resource()
