#!/usr/bin/python           # This is dns_resolver.py file
from dns_query import *
import struct

listRootServers = ['198.41.0.4', '192.228.79.201', '192.33.4.12', '199.7.91.13', '192.203.230.10', '192.5.5.241', '192.112.36.4', '128.63.2.53', '192.36.148.17', '192.58.128.30', '193.0.14.129', '199.7.83.42', '202.12.27.3']

"""
findIP return the IP adress of a domain name.

Raise an exception if the domain name is not correct.
Raise an exception if no server was able to answer.
"""
def findIP(website, show):
    # we initialize the object query
    query = DnsQuery()
    query.op = DQFlags.QUERY
    query.rd = DQFlags.RECURSION_NOT_DESIRED
    query.addQuestion(website, DRType.A, DQClass.IN)
    query.convertInStr()
    listAdress = listRootServers # listAdress possesses the IP adresses of the DNS we have to ask.
    result = []
    while True:
        for i in listAdress:
            # test if IP address is IPv4 or IPv6.
            if i.find('.') != -1:
                IPv4 = True
            else:
                IPv4 = False
            finish, tc, ra, err, nbAn, nbAu, nbAd, listAns, listAus, listAds = query.sendQuery(i, IPv4)
            if err != DRCode.SERVFAIL:
                # the variable show is use because sometime we have DNS we have to ask but we don't know the ip adress, just the domain name.
                if show:
                    print i
                break
        if err != DRCode.NOERROR:
            raise Exception('error', err)
        # print err, finish, tc, ra, listAns, listAus, listAds
        # finish mean that we have found the ip adress of the domain name requested or that there is a redirection.
        if finish:
            if nbAn != 0:
                if listAns[0][1] == DRType.A or listAns[0][1] == DRType.AAAA:
                    # we have found the ip adress of the domain name requested.
                    for i in listAns:
                        if i[1] == DRType.A or i[1] == DRType.AAAA:
                            result.append(i[5])
                    break
                elif listAns[0][1] == DRType.CNAME:
                    #we have to do a redirection
                    # we have this case for this website: www.google.fr.
                    website = listAns[0][5]
                    query.clearQuestion()
                    query.addQuestion(website, DRType.A, DQClass.IN)
                    query.convertInStr()
                    listAdress = listRootServers
            else:
                raise Exception('error: we should have one result')
        else:
            # we have to ask a DNS below
            if nbAd == 0:
                # we don't know the IP adress of the DNS below
                # we have this case for this website: docs.python.org
                temp = [x[5] for x in listAus]
                for i in temp:
                    try:
                        # print "{"
                        listAdress = findIP(i, False)
                        # print "}"
                        break
                    except:
                        pass
            else:
                listAdress = [ x[5] for x in listAds ]
    return result

print findIP('stackoverflow.com', True)
