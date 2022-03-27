''' These are the potentially unused lines from the previous module.
importing * : to enable writing sin(13) instead of math.sin(13)
from math import *
import getpass
'''

#importing wx files
import wx
import sys
import gui
from netmiko import ConnectHandler
from napalm import get_network_driver

#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class CalcFrame(gui.MainFrame):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        gui.MainFrame.__init__(self,parent)
 
    # Functions
    # Closes python program
    def closeFunc(self,event):
        sys.exit()
    # Clears hostname field
    def clearFunc(self,event):
        self.txtHostname.SetValue(str(''))
        self.txtOutput.SetValue("The hostname field was cleared.")
    # Checks Internet stats and writes results to a file
    def inetFunc(self,event):
        username = self.txtUsername.GetValue()
        password = self.txtPassword.GetValue()
        SATDCR7 = {
            'device_type': 'cisco_ios',
            'host':   '10.250.2.41',
            'username': username,
            'password': password,
        }

        NDHDCR7 = {
            'device_type': 'cisco_ios',
            'host':   '10.252.25.156',
            'username': username,
            'password': password,
        }
        net_connect = ConnectHandler(**SATDCR7)
        output = net_connect.send_command('show int ten 1/0/4 hum | inc Description|reliability|rate|errors')
        print('SATDC - ATT', file=open('inet_stats/internet_stats.txt', 'w'))
        print(output, file=open('inet_stats/internet_stats.txt', 'a'))
        print(' ', file=open('inet_stats/internet_stats.txt', 'a'))
        output = net_connect.send_command('show int ten 1/0/4 history 60min both')
        print(output, file=open('inet_stats/internet_stats.txt', 'a'))
        print(' ', file=open('inet_stats/internet_stats.txt', 'a'))
        #
        net_connect = ConnectHandler(**SATDCR7)
        output = net_connect.send_command('show int ten 1/0/5 hum | inc Description|reliability|rate|errors')
        print('SATDC - Zayo', file=open('inet_stats/internet_stats.txt', 'a'))
        print(output, file=open('inet_stats/internet_stats.txt', 'a'))
        print(' ', file=open('inet_stats/internet_stats.txt', 'a'))
        output = net_connect.send_command('show int ten 1/0/5 history 60min both')
        print(output, file=open('inet_stats/internet_stats.txt', 'a'))
        print(' ', file=open('inet_stats/internet_stats.txt', 'a'))
        #
        net_connect = ConnectHandler(**NDHDCR7)
        output = net_connect.send_command('show int ten 0/1/7 hum | inc Description|reliability|rate|errors')
        print('NDHDC - Zayo', file=open('inet_stats/internet_stats.txt', 'a'))
        print(output, file=open('inet_stats/internet_stats.txt', 'a'))
        print(' ', file=open('inet_stats/internet_stats.txt', 'a'))
        output = net_connect.send_command('show int ten 0/1/7 history 60min both')
        print(output, file=open('inet_stats/internet_stats.txt', 'a'))
        print(' ', file=open('inet_stats/internet_stats.txt', 'a'))
        #
        self.txtOutput.SetValue("Internet stats are available in the inet_stats directory.")
    # Writes running config of txtHostname to file in backups directory
    def backupFunc(self,event):
        hostname = self.txtHostname.GetValue()
        username = self.txtUsername.GetValue()
        password = self.txtPassword.GetValue()
        device = {
            'device_type': 'cisco_ios',
            'host':   hostname,
            'username': username,
            'password': password,
        }
        net_connect = ConnectHandler(**device)
        output = net_connect.send_command('terminal length 0')
        output = net_connect.send_command('show run')
        print(output, file=open("backups/" + hostname + "_running_config.txt", 'w'))
        self.txtOutput.SetValue(hostname + " was backed up successfully!")
    # Runs the Radius Fixit Script on txtHostname
    def radiusfixitFunc(self,event):
        cfg_file = "/radius_fix_it/radius_fix_it.txt"
        hostname = self.txtHostname.GetValue()
        username = self.txtUsername.GetValue()
        password = self.txtPassword.GetValue()
        device = {
            'device_type': 'cisco_ios',
            'host':   hostname,
            'username': username,
            'password': password,
        }
        net_connect = ConnectHandler(**device)
        with ConnectHandler(**device) as net_connect:
            output = net_connect.send_config_from_file(cfg_file)
            output = net_connect.save_config()
        self.txtOutput.SetValue("The radius fixit script was run on " + hostname + " successfully.")
    # Check for prod acl and merge config if missing
    def aclFunc(self,event):
        driver = get_network_driver('ios')
        hostname = self.txtHostname.GetValue()
        username = self.txtUsername.GetValue()
        password = self.txtPassword.GetValue()
        device = driver(hostname, username, password)
        device.open()
        device.load_merge_candidate(filename='acl_verification/prod_acl_universal.cfg')
        diffs = device.compare_config()
        if len(diffs) > 0:
            self.txtOutput.SetValue(diffs)
            device.discard_config()
        else:
            self.txtOutput.SetValue("No changes are necessary.")
            device.discard_config()
        device.close()



#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)
 
#create an object of CalcFrame
frame = CalcFrame(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()