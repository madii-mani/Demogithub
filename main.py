from config import *
from lib import *
from myLogging import *
import threading
myObj = router_info()
result = myObj.get_router_details()
print(result['routers'])
loggingObj = nap_logging('log1.txt')
print(dir(loggingObj))
print("Hi")
loggingObj.logger.warning("Hi")
threads = []
def rtr_login(each_router):
    myObj1 = login(each_router)
    myObj1.router_connect()
    myObj1.router_enable()
    myObj1.router_show_ip()
    myObj1.router_parse_show_ip()
for each_router in result['routers']:
    t = threading.Thread(target=rtr_login,args=(each_router,))
    threads.append(t)
    t.start() 
for t in threads:
    t.join()    

# def router_login_1():
    # for each_router in result['routers']:
        # myObj1 = login(each_router)
        # myObj1.router_connect()