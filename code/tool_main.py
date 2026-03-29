0# student_name: Dharanesh A
# roll_number: 727823TUCY007
# project_name: Network Vulnerability Scanner
# date: 29-03-2026

import nmap
import datetime

print("Roll Number:", "727823TUCY007")
print("Scan Time:", datetime.datetime.now())

target = input("Enter Target IP: ")

scanner = nmap.PortScanner()

print("\n[+] Scanning target...\n")

scanner.scan(target, '21,22,80')

for host in scanner.all_hosts():
    print("Host:", host)
    print("State:", scanner[host].state())

    for proto in scanner[host].all_protocols():
        print("Protocol:", proto)

        ports = scanner[host][proto].keys()

        for port in sorted(ports):
            state = scanner[host][proto][port]['state']
            service = scanner[host][proto][port]['name']

            print(f"Port: {port} | State: {state} | Service: {service}")

print("\n[+] Scan Completed")
