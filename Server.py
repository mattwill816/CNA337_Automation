# This is the template code for the CNA337 Final Project
# Matthew Williams
# CNA 337 Fall 2020
#Worked with Dylan McCormack,  Eric Yevenko
#Received help from Hassan

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        EC2Matt = os.system("ping -n 4 " + self.server_ip)
        return self.server_ip
