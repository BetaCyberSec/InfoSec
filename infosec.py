#!/usr/bin/env python3

import requests, os, time, sys, socket, json

R = '\033[1;31;40m'
G = '\033[1;32;40m' 
C = '\033[1;36;40m' 
W = '\033[1;37;40m'
M = '\033[1;35;40m'

def TOS():
    info = input("TOS: We do not take any responsibility for your actions use this script on your own stuff or make sure u have permissionm by the owner type (agree) to continue type (disagree) to exit. = ")
    if info == 'agree':
        os.system("clear")
    else:
        sys.exit()
TOS()

VERSION = '4.0'

def banner():
    banner = r'''
==========================================
||  ___ _   _ _____ ___  ____            ||
|| |_ _| \ | |  ___/ _ \/ ___|  ___  ___ ||
||  | ||  \| | |_ | | | \___ \ / _ \/ __|||
||  | || |\  |  _|| |_| |___) |  __/ (__ ||
|| |___|_| \_|_|   \___/|____/ \___|\___|||
========================================== 
 ----------------------------------------------------------------------------                                        
 - S E C U R I T Y  I S  J U S T  A  W O R D , D O  N O T  T R U S T  I T ! -
 ----------------------------------------------------------------------------
'''
    request = requests.get("https://api.ipify.org/")
    print(C +"YOUR IPV4 IS :" + request.text)
    hostname = socket.gethostname()
    print(W +"YOUR COMPUTER NAME IS :" + hostname) 
    print(W + banner + W)
    print(M + "Coded By" + W + " = " + C + "Beta" +W)
    print(M + "Version" + W + " = " + C + "4.0" + W + '\n')
    print(C + "[" + W + "1" + C + "]" + W + "People Information Gathering")
    print(C + "[" + W + "2" + C + "]" + W + "WebSite Information Gathering")
    print(C + "[" + W + "3" + C + "]" + W + "Network Information Gathering")
    print(C + "[" + W + "4" + C + "]" + W + "Database Search (comming soon)")

def infosec():
    infosec = input("root@infosec:~# ")

    if infosec == '1':
        print(C + "[" + W + "1" + C + "]" + W + "Phone Number Lookup")
        print(C + "[" + W + "2" + C + "]" + W + "Email Lookup")
        print(C + "[" + W + "3" + C + "]" + W + "Skype resolver")
        print(C + "[" + W + "4" + C + "]" + W + "IP to Skype")
        print(C + "[" + W + "5" + C + "]" + W + "PSN Resolver")


        people = input("root@people:~# ")

        if people == '1':
            phoneNum = input("Enter Phone number : ")
            key = '31a224990c2974ac753e76a68d6a1ca6'
            json = requests.get('http://apilayer.net/api/validate?access_key=%s&format=1&number=%s' % (key, phoneNum))
            test = json.json()
            print(C + "---___PHONE NUMBER___---" + W)
            print("________________")
            print(C + "VALID: " + W)
            print(test['valid'])
            print("________________")
            print(C + "COUNTRY: " + W)
            print(test['country_name'])
            print("________________")
            print(C + "LOCATION: " + W)
            print(test['location'])
            print("________________")
            print(C + "CARRIER: " + W)
            print(test['carrier'])
            print("________________")
            print(C + "LINE TYPE: " + W)
            print(test['line_type'])
            print("________________")

        elif people == '2':
            email = input("Enter Email : ")
            key = 'ba2bea5ece9848389cd0a6e45400960b'
            json = requests.get('https://api.zerobounce.net/v1/validate?apikey=%s&email=%s' % (key, email))
            test = json.json()
            print(C + "---___EMAIL INFO___---" + W)
            print("________________") 
            print(C + "EMAIL: " + W)
            print(test['address'])
            print("________________")
            print(C + "VALID: " + W)
            print(test['status'])
            print("________________")
            print(C + "ACCOUNT: " + W)
            print(test['account'])
            print("________________")
            print(C + "DOMAIN: " + W)
            print(test['domain'])
            print("________________")
            print(C + "FIRSTNAME: " + W)
            print(test['firstname'])
            print("________________")
            print(C + "LASTNAME: " + W)
            print(test['lastname'])
            print("________________")
            print(C + "GENDER: " + W)
            print(test['gender'])
            print("________________")
            print(C + "LOCATION: " + W)
            print(test['location'])
            print("________________")
            print(C + "CREATIONDATE: " + W)
            print(test['creationdate'])
            print("________________")
            print(C + "PROCESSWDAT: " + W)
            print(test['processedat'])
            print("________________")

        elif network == '3':
            skype = input("Enter Skype : ")
            json = requests.get("https://webresolver.nl/api.php?key=M8GAR-4LBHP-I3WD8-S1Y0T&html=0&action=resolve&string=%s" % (skype))
            print(json.text)
        
        elif people == '4':
            ip = input("Enter IP : ")
            json = requests.get("https://webresolver.nl/api.php?key=M8GAR-4LBHP-I3WD8-S1Y0T&html=0&action=ip2skype&string=%s" % (ip))
            print(json.text)

        elif people == '5':
            psn = input("Enter PSN : ")
            json = requests.get("https://sprx.pr0jectn1ne.com/APIV3/Api.php?get=ResolverPsn&Token=bmZNb1ViZTV6SFcwWTRQY3p4TEo5RXFvbDFkekNtSDVYY0JRdGFSSUdiaz06OuZdbDz2WpjWfeVBqIAQDWQ=&Psn=%s" % (psn))
            print(json.text)

    elif infosec == '2':
        print(C + "[" + W + "1" + C + "]" + W + "CloudFlare Resolver")
        print(C + "[" + W + "2" + C + "]" + W + "Website Headers")      
        print(C + "[" + W + "3" + C + "]" + W + "Subnetcalc")         
        print(C + "[" + W + "4" + C + "]" + W + "Page Links")       
        print(C + "[" + W + "5" + C + "]" + W + "Zonetransfer")        
        print(C + "[" + W + "6" + C + "]" + W + "Host Search")          
        print(C + "[" + W + "7" + C + "]" + W + "Whois")       
        print(C + "[" + W + "8" + C + "]" + W + "DNS Resolver")       
        print(C + "[" + W + "9" + C + "]" + W + "Scan For All")
        website = input("root@website:~# ")

        if website == '1':
            url = input("Enter URL : ")
            json = requests.get('https://webresolver.nl/api.php?key=M8GAR-4LBHP-I3WD8-S1Y0T&html=0&action=cloudflare&string=%s' % (url))
            print(json.text)
        
        elif website == '2':
            url = input("Enter URL : ")
            json = requests.get('https://api.hackertarget.com/httpheaders/?q=%s' % (url))
            print(json.text)

        elif website == '3':
            url = input("Enter URL : ")
            json = requests.get('https://api.hackertarget.com/subnetcalc/?q=%s' % (url))
            print(json.text)
        
        elif website == '4':
            url = input("Enter URL : ")
            json = requests.get('https://api.hackertarget.com/pagelinks/?q=%s' % (url))
            print(json.text)

        elif website == '5':
            url = input("Enter URL : ")
            json = requests.get('https://api.hackertarget.com/zonetransfer/?q=%s' % (url))
            print(json.text)

        elif website == '6':
            url = input("Enter URL : ")
            json = requests.get('https://api.hackertarget.com/hostsearch/?q=%s' % (url))
            print(json.text)
        
        elif website == '7':
            url = input("Enter URL : ")
            json = requests.get('https://api.hackertarget.com/whois/?q=%s' % (url))
            print(json.text)
        
        elif website == '8':
            url = input("Enter URL : ")
            json = requests.get('https://webresolver.nl/api.php?key=M8GAR-4LBHP-I3WD8-S1Y0T&html=0&action=dns&string=%s' % (url))
            print(json.text)
        
        elif website == '9':
            url = input("Enter URL : ")
            print(C + "---___CloudFlare Info___---" + W)
            json = requests.get('https://webresolver.nl/api.php?key=M8GAR-4LBHP-I3WD8-S1Y0T&html=0&action=cloudflare&string=%s' % (url))
            print(json.text)


            print(C + "---___HTTP Headers___---" + W)
            json = requests.get('https://api.hackertarget.com/httpheaders/?q=%s' % (url))
            print(json.text)


            print(C + "---___Subnet___---" + W)
            json = requests.get('https://api.hackertarget.com/subnetcalc/?q=%s' % (url))
            print(json.text)


            print(C + "---___Page Links___---" + W)
            json = requests.get('https://api.hackertarget.com/pagelinks/?q=%s' % (url))
            print(json.text)


            print(C + "---___Zone Transfer___---" + W)
            json = requests.get('https://api.hackertarget.com/zonetransfer/?q=%s' % (url))
            print(json.text)


            print(C + "---___Host Search___---" + W)
            json = requests.get('https://api.hackertarget.com/hostsearch/?q=%s' % (url))
            print(json.text)


            print(C + "---___Whois___---" + W)
            json = requests.get('https://api.hackertarget.com/whois/?q=%s' % (url))
            print(json.text)


            print(C + "---___DNS Info___---" + W)
            json = requests.get('https://webresolver.nl/api.php?key=M8GAR-4LBHP-I3WD8-S1Y0T&html=0&action=dns&string=%s' % (url))
            print(json.text)

    elif infosec == '3':
        print(C + "[" + W + "1" + C + "]" + W + "GEO IP")
        print(C + "[" + W + "2" + C + "]" + W + "Nmap")
        print(C + "[" + W + "3" + C + "]" + W + "Mtr")
        print(C + "[" + W + "4" + C + "]" + W + "Reverse ip lookup")
        print(C + "[" + W + "5" + C + "]" + W + "IP Valid Check")
        print(C + "[" + W + "6" + C + "]" + W + "TOR Check")
        print(C + "[" + W + "7" + C + "]" + W + "PROXY Check")

        network = input("root@network:~# ")
        if network == '1':
            ip = input("Enter IP : ")
            json = requests.get("http://ipinfo.io/%s" % (ip))
            test = json.json()
            print(C + "---___IP INFO___---" + W)
            print(C + "IP:" + W)
            print(test['ip'])
            print("________________")
            print(C + "HOSTNAME:  " + W)
            print(test['hostname'])
            print("________________")
            print(C + "ORG: " + W)
            print(test['org'])
            print("________________")
            print(C + "COUNTRY: " + W)
            print(test['country'])
            print("________________")
            print(C + "CITY: " + W)
            print(test['city'])
            print("________________")
            print(C + "REGION:" + W)
            print(test['region'])
            print("________________")
            print(C + "POSTAL:" + W)
            print(test['postal'])
            print("________________")
            print(C + "LOC:" + W)
            print(test['loc'])
            print("________________")

        elif network == '2':
            ip = input("Enter IP : ")
            json = requests.get("https://api.hackertarget.com/nmap/?q=%s" % (ip))
            print(json.text)

        elif network == '3':
            ip = input("Enter IP : ")
            json = requests.get("https://api.hackertarget.com/mtr/?q=%s" % (ip))
            print(json.text)

        elif network == '4':
            ip = input("Enter IP : ")
            json = requests.get("https://api.hackertarget.com/reverseiplookup/?q=%s" % (ip))
            print(json.text)
        
        elif network == '5':
            ip = input("Enter IP : ")
            json = requests.get("https://api.c99.nl/ipvalidator?key=yolo.swagayden@gmail.0252om&ip=%s" % (ip))
            print(json.text)        

        elif network == '6':
            ip = input("Enter IP : ")
            json = requests.get("https://api.c99.nl/torchecker?key=yolo.swagayden@gmail.0252om&ip=%s" % (ip))
            print(json.text)        

        elif network == '7':
            ip = input("Enter IP : ")
            json = requests.get("https://api.c99.nl/proxydetector?key=yolo.swagayden@gmail.0252om>&ip=%s" % (ip))
            print(json.text)    

try:
    banner()
    infosec()
except KeyboardInterrupt:
    print('\n' + R + '[!]' + R + ' Keyboard Interrupt.' + W)
    exit()
