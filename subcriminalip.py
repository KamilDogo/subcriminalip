import requests
import argparse
import json
import re
from config import *

api_key = cip_api_key 

def banner():
    print("""
                                               
         _           _       _         _ _     
 ___ _ _| |_ ___ ___|_|_____|_|___ ___| |_|___ 
|_ -| | | . |  _|  _| |     | |   | .'| | | . |
|___|___|___|___|_| |_|_|_|_|_|_|_|__,|_|_|  _|
                                          |_|  
              
     Powered By CriminalIP
     https://www.criminalip.io/
    """)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Tool to search for domains , subdomains , IPs and orgname from CriminalIP API")
    parser.add_argument("-g", "--get", help="target", type=str)
    parser.add_argument("-s", "--subdomains", help="extract subdomains", action='store_true')
    parser.add_argument("-t", "--offset", help="Starting position in the dataset", type=str)
    parser.add_argument("-i", "--ips", help="extract ips adresses", action='store_true')
    parser.add_argument("-o", "--orgnames", help="extract organization names", action='store_true')
    parser.add_argument("-d", "--domains", help="extract domain names", action='store_true')
    return parser.parse_args()


def search_ssl_subject_common_names(query,offset=0):
    url = "https://api.criminalip.io/v1/banner/search"
    headers = {
        "x-api-key": api_key
    }

    params = {
        "query": f"ssl_subject_common_name:{query}",
        "offset": offset
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()["data"]["result"]
    ssl_subject_common_names = [item["ssl_subject_common_name"] for item in data]
    unique_ssl_subject_common_names = sorted(set(ssl_subject_common_names))

    for name in unique_ssl_subject_common_names:
        print(name)


def extract_ip_addresses(query,offset=0):
    url = "https://api.criminalip.io/v1/banner/search"
    headers = {
        "x-api-key": api_key
    }

    params = {
        "query": f"ssl_subject_common_name:{query}",
        "offset": offset
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()["data"]["result"]
    ip_addresses = sorted(set(item["ip_address"] for item in data))

    for ip_address in ip_addresses:
        print(ip_address)


def extract_orgnames(query,offset=0):
    url = "https://api.criminalip.io/v1/banner/search"
    headers = {
        "x-api-key": api_key
    }

    params = {
        "query": f"ssl_subject_common_name:{query}",
        "offset": offset,
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()["data"]["result"]
    orgnames = set(item["ssl_subject_organization"] for item in data)

    for orgname in orgnames:
        print(orgname)



def extract_domains(query,offset=0):
    url = "https://api.criminalip.io/v1/banner/search"
    query_params = {
        "query": f"ssl_subject_common_name:{query}",
        "offset": offset
    }
    headers = {
        "x-api-key": api_key
    }

    response = requests.get(url, params=query_params, headers=headers)
    data = response.json()

    ssl_info_list = [banner.get("ssl_info", "") for banner in data.get("data", {}).get("result", [])]
    pattern = r'\b((?:[a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9]\.)+(?:[a-zA-Z]{2,}))\b'

    ssl_domains = []

    for info in ssl_info_list:
        matches = re.findall(pattern, info)
        ssl_domains.extend(matches)
        
        for domain in ssl_domains:
            print(domain)


def main():

    args = parse_arguments()
    if args.get:
        if args.subdomains:
            if args.offset:
                search_ssl_subject_common_names(args.get,args.offset)
            search_ssl_subject_common_names(args.get)

        if args.ips:
            if args.offset:
                extract_ip_addresses(args.get,args.offset)
            extract_ip_addresses(args.get)

        if args.orgnames:
            if args.offset:
                search_ssl_subject_common_names(args.get,args.offset)
            else:
                search_ssl_subject_common_names(args.get)

        if parse_arguments().domains:
            if args.offset:
                extract_domains(args.get,args.offset)
            extract_domains(args.get)

if __name__ == "__main__":
    banner()
    main()
