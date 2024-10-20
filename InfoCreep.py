# returns status code for web url
import requests
import sys
import ipaddress
from NetworkTools import NetworkTools
from urllib.parse import urlparse

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def extract_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc or parsed_url.path

def run_info_creep():
    is_windows = input("Are you using Windows? (y/n): ").strip().lower() == 'y'
    network_tools = NetworkTools(is_windows)

    run = True
    while run:
        command = input("> ").strip().lower()
        
        if command == "-h":
            print_help()
        elif command.startswith("creep "):
            target = command.split("creep ")[1]
            result = network_tools.dnsRec(target)
            print(result)
        elif command == "exit":
            run = False
        else:
            print("Invalid command. Use -h for help.")

def print_help():
    print("I hope these help:")
    print("            -h                     --> help menu")
    print("            creep <target>         --> perform DNS lookup and network scan on target")
    print("            exit                   --> exit the program")

if __name__ == "__main__":
    run_info_creep()
