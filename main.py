# This is the template code for the CNA337 Final Project
# Matthew Williams
# CNA 337 Fall 2020
# Worked with Dylan McCormack,  Eric Yevenko
# Received help from Hassan
from Server import Server


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Matthew")


# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    LaunchWizard26 = Server('3.138.140.132')
    # TODO - Call Ping method and print the results
    print(LaunchWizard26.ping())
