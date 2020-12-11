# CNA 337 Fall 2020
# Matthew Williams 12/10/2020
# I got help from Hasan

from Server import Server
def print_program_info():

    print("Server Automator v0.1 by matthew")

if __name__ == '__main__':
    print_program_info()

    EC2server = Server('3.138.140.132')

    print(EC2server.ping())
