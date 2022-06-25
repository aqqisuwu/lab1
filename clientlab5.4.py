from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.56.104',  #Your Server IP
    'username': 'aqqisuwu', #your Server Username
    'password': '123456', #your server password
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('uname -a')
command = 'Sakit perut'
print(output)
