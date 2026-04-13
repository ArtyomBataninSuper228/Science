from protocol_2_0 import *

con = Connection('192.168.1.8', 55432)
#con.send_inner(b'Hello there!')
time.sleep(2)
con.close()
print('Closed')
