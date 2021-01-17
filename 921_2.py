import datetime
import time
import os
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from msedge.selenium_tools import Edge, EdgeOptions
today = datetime.datetime.now().date()
def Restart_Modem():
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("-inprivate")
    #edge_browser=webdriver.Edge('./msedgedriver.exe')
    edge_browser=Edge(options = options)
    edge_browser.get('http://192.168.0.1')
    time.sleep(2)
    print('Welcome')
    login = edge_browser.find_element_by_name('username')
    password = edge_browser.find_element_by_name('password')
    sign = edge_browser.find_element_by_class_name('styled_button_s')
    login.clear()
    password.clear()
    login.send_keys('admin')
    password.send_keys('admin')
    sign.click()
    print('Sign in')
    alert = Alert(edge_browser)
    time.sleep(2) 
    edge_browser.get('http://192.168.0.1/saveconf.htm')
    time.sleep(2)
    system = edge_browser.find_element_by_id('three_level_menu1')
    system.click()
    time.sleep(2)
    reboot = edge_browser.find_element_by_name('reboot')
    reboot.click()
    alert.accept()
    time.sleep(90)
    print('Reboot')
    edge_browser.quit()
#Restart_Modem()
#time.sleep(30)
#Restart_Modem()
while (True):    
    now = datetime.datetime.now().time()
    my_time = now.replace(hour=1, minute=5, second=0, microsecond=0)
    tomorrow = datetime.datetime.now().date()
    if(tomorrow > today):
            if(now > my_time):
               Restart_Modem()
               break
            else:
                print (now)
                time.sleep(60)
    else:
        print (now)
        time.sleep(60)
while (True):
    time.sleep(60)
    ping = os.system("ping -n 1 8.8.8.8")
    if (ping == 1):
        print('offline')
        Restart_Modem()
    else:
        print('online')
        break
