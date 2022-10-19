import sys
import nmap3

url = '127.0.0.1' if len(sys.argv) < 2 else sys.argv[1]
nmap = nmap3.Nmap()
result = nmap.nmap_version_detection(url)

print("{: >20} \t {: >20} \t {: >20}".format("Service", "Version", "Port number"))
for prt in result[url]['ports']:
    if "service" in prt:
        serv = prt["service"]
        name = serv["name"] if "name" in serv else "None"
        ver = serv["version"] if "version" in serv else "None"
    num = prt["portid"] if "portid" in prt else "None"
    print("{: >20} \t {: >20} \t {: >20}".format(name, ver, num))
