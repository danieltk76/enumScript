# Selenium is a pain, Im switching to PlayWright
from playwright.sync_api import sync_playwright
import re
import time
import subprocess
import shlex

def perform_dns_lookup(domain):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto("https://viewdns.info/", timeout=60000)  # Increased timeout to 60 seconds
            page.wait_for_selector('input[name="domain"]', timeout=30000)  # Increased to 30 seconds
            page.fill('input[name="domain"]', domain)
            page.click('input[type="submit"]')
            page.wait_for_selector('.table-responsive', timeout=30000)
            dns_info = page.inner_text('.table-responsive')
            browser.close()
            return dns_info
        except Exception as e:
            browser.close()
            return f"Error performing DNS lookup: {str(e)}"

def format_dns_info(dns_info):
    # Remove ASCII art and extra whitespace
    cleaned_info = re.sub(r'═+\s*ViewDNS.info.*?═+', '', dns_info, flags=re.DOTALL)
    cleaned_info = re.sub(r'\s{2,}', '\n', cleaned_info.strip())
    
    # Split the information into lines
    lines = cleaned_info.split('\n')
    
    # Format the output
    formatted_output = "DNS Lookup Results:\n"
    formatted_output += "=" * 20 + "\n"
    for line in lines:
        if line.strip():
            key, value = line.split(':', 1)
            formatted_output += f"{key.strip():<20}: {value.strip()}\n"
    
    return formatted_output

def run_command(command):
    try:
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        if error:
            return f"Error: {error}"
        return output
    except Exception as e:
        return f"Error executing command: {str(e)}"

def dnsRec(target):
    print(f"Performing DNS lookup and scan for {target}...")
    
    # WHOIS lookup
    whois_result = run_command(f"whois {target}")
    
    # Nmap scan with version detection
    nmap_result = run_command(f"nmap -sV {target}")
    
    return f"WHOIS Information:\n{whois_result}\n\nNMAP Scan Results:\n{nmap_result}"

# Example usage
if __name__ == "__main__":
    domain = input("Enter a domain for DNS lookup: ")
    result = dnsRec(domain)
    print(result)
