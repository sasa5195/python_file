import os
import urllib.request
import io

# note - you would need to pip install this (or add it with GUI in pycharm
# (file->settings->project->project interperter->install (a green "+" sign)
from tld import get_tld


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name

# this is the linux version
# def get_ip_address(url):
#     command = "host" + url
#     process = os.popen(command)
#     results = str(process.read())
#     marker = results.find('has address') + 12
#     return results[marker].splitlines()[0]

# this is the windows version
def get_ip_address(url):
    command = "nslookup " + url
    process = os.popen(command)
    results = str(process.read())
    # there's a problem - on some websites the ip will be on the 5th line (index 4) and some it will be on different
    # so I just take everything
    # marker = results.splitlines()[4]
    return results

# this will work for linux automatically.
# Windows users need to download it from here: https://nmap.org/download.html
def get_nmap(domain):
    command = "nmap " + domain
    process = os.popen(command)
    results = str(process.read())
    return results

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request.urlopen(path + 'robots.txt', data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()


# notice that the command in this function will only work on linux, while in windows you have to download whois
# https://technet.microsoft.com/en-us/sysinternals/whois.aspx
# You might have to add the directory path of where you unpack whois to the system variables
# if so, check:
# http://superuser.com/questions/284342/what-are-path-and-other-environment-variables-and-how-can-i-set-or-use-them
def get_whois(url):
    command = "whois " + url
    process = os.popen(command)
    results = str(process.read())
    return results


def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(domain_name)
    nmap = get_nmap(domain_name)  # ('-F', ip_address) - this is the linux version
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, ip_address, nmap, robots_txt, whois)

def create_report(name, full_url, domain_name, ip_address, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/ipaddress.txt', ip_address)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots.txt', robots_txt)
    write_file(project_dir + '/whois.txt', whois)

ROOT_DIR = 'companies'
create_dir(ROOT_DIR)
gather_info('thenewboston', 'https://www.thenewboston.com/')