from selenium import webdriver
import time

def login():
    signin_url = 'https://www.zhihu.com/signin'
    url='https://www.zhihu.com/'
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(options=option)
    driver.get(signin_url)
    #切换登录模式
    driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[1]/div[2]').click()
    #输入id
    driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[2]/div/label/input').send_keys(
        '15927468966')
    time.sleep(1)
    #输入password
    driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[3]/div/label/input').send_keys(
        'mm147258369')
    time.sleep(1)
    #登录
    driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/button').click()
    #sleep之后才会切换url
    time.sleep(1)
#    current_url = driver.current_url 还没用到
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/header/div[1]/ul/li[3]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div[1]/div/div/a[3]/div').click()

def main():
    login()


main()
