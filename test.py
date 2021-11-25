from guacamole1 import Guac
from pprintpp import pprint

guac1 = Guac(url='http://10.3.47.21:32773/guacamole/')
#authenticate to Guacamole and get a token.
guac1.auth('guacadmin','guacadmin')


cons = guac1.listConnections()
congrups = guac1.listConnectionGroups()



