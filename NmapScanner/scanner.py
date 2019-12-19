#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()
print('                  NMAP AUTOMATION TOOL                 ')
print('             <--------------------------------->')
ip_addr = input('Enter IP address to Scan: ')
print('IP address is:',ip_addr)
type(ip_addr)

resp = input(""""\nPlease enter the type of Scan you want to perform
                    1.SYN ACK Scan
                    2.UDP Scan
                    3.Comprehensive Scan
                    
Enter your Option:\n""")

print('You have selected option: ',resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
else:
    print("Please enter a valid option")

     
