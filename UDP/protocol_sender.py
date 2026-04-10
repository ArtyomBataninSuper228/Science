from protocol_base import *

con = Connection('192.168.1.8', 65432)
time.sleep(2)
con.close()
print('Closed')
