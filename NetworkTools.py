import socket
import subprocess
from urllib.parse import urlparse
import shutil

class NetworkTools:
    def __init__(self, is_windows):
        self.is_windows = is_windows
        self.nmap_available = self.check_nmap_availability()

    def check_nmap_availability(self):
        return shutil.which('nmap') is not None

    def run_command(self, command, timeout=30):
        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            output, error = process.communicate(timeout=timeout)
            if error:
                return f"Error: {error.strip()}"
            return output.strip()
        except subprocess.TimeoutExpired:
            return f"Command timed out after {timeout} seconds"
        except Exception as e:
            return f"Error executing command: {str(e)}"

    def resolve_to_ip(self, target):
        try:
            parsed = urlparse(target)
            domain = parsed.netloc or parsed.path
            return socket.gethostbyname(domain)
        except socket.gaierror:
            return target  # Return the original target if resolution fails

    def simple_port_scan(self, ip, ports):
        open_ports = []
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        return open_ports

    def dnsRec(self, target):
        ip = self.resolve_to_ip(target)
        print(f"Performing DNS lookup and scan for {ip}...")
        
        # DNS lookup
        if self.is_windows:
            dns_result = self.run_command(f"nslookup {ip}")
        else:
            dns_result = self.run_command(f"dig {ip}")
        
        # WHOIS lookup
        if self.is_windows:
            whois_result = "WHOIS lookup not available on Windows"
        else:
            whois_result = self.run_command(f"whois {ip}")
        
        # Port scan
        if self.nmap_available:
            nmap_result = self.run_command(f"nmap -sV {ip}")
            if "open" not in nmap_result:
                port_scan_result = self.format_no_open_ports()
            else:
                port_scan_result = "See NMAP results"
        else:
            nmap_result = "NMAP not available"
            common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995, 3306, 3389, 5900, 8080]
            open_ports = self.simple_port_scan(ip, common_ports)
            if open_ports:
                port_scan_result = "\n".join([f"Port {port} is open" for port in open_ports])
            else:
                port_scan_result = self.format_no_open_ports()
        
        formatted_output = f"DNS Information for {ip}:\n"
        formatted_output += "=" * 40 + "\n"
        formatted_output += dns_result + "\n\n"
        formatted_output += f"WHOIS Information for {ip}:\n"
        formatted_output += "=" * 40 + "\n"
        formatted_output += whois_result + "\n\n"
        formatted_output += f"Port Scan Results for {ip}:\n"
        formatted_output += "=" * 40 + "\n"
        if self.nmap_available:
            formatted_output += nmap_result
        else:
            formatted_output += port_scan_result
        
        return formatted_output

    def format_no_open_ports(self):
        return (
            "┌───────────────────────┐\n"
            "│   No open ports found │\n"
            "└───────────────────────┘"
        )
