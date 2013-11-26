#!/usr/bin/python           # This is dns_resolver.py file
from dns_query import *
import struct

listRootServers = ['198.41.0.4', '192.228.79.201', '192.33.4.12', '199.7.91.13', '192.203.230.10', '192.5.5.241', '192.112.36.4', '128.63.2.53', '192.36.148.17', '192.58.128.30', '193.0.14.129', '199.7.83.42', '202.12.27.3']

def findIP(website):
    query = DnsQuery()
    query.op = DQFlags.QUERY
    query.rd = DQFlags.RECURSION_NOT_DESIRED
    query.addQuestion(website, DRType.A, DQClass.IN)
    query.convertInStr()
    listAdress = listRootServers
    result = []
    while True:
        for i in listAdress:
            if i.find('.') != -1:
                IPv4 = True
            else:
                IPv4 = False
            finish, tc, ra, err, nbAn, nbAu, nbAd, listAns, listAus, listAds = query.sendQuery(i, IPv4)
            if err != DRCode.SERVFAIL:
                print i
                break
        if err != DRCode.NOERROR:
            raise Exception('error', err)
        # print err, finish, tc, ra, listAns, listAus, listAds
        if finish:
            if nbAn != 0:
                if listAns[0][1] == DRType.A or listAns[0][1] == DRType.AAAA:
                    for i in listAns:
                        if i[1] == DRType.A or i[1] == DRType.AAAA:
                            result.append(i[5])
                    break
                elif listAns[0][1] == DRType.CNAME:
                    # we have this case for this website: www.google.fr 
                    website = listAns[0][5]
                    query.clearQuestion()
                    query.addQuestion(website, DRType.A, DQClass.IN)
                    query.convertInStr()
                    listAdress = listRootServers
            else:
                raise Exception('error: we should have one result')
        else:
            if nbAd == 0:
                # we have this case for this website: docs.python.org
                temp = [x[5] for x in listAus]
                for i in temp:
                    try:
                        # print "{"
                        listAdress = findIP(i)
                        # print "}"
                        break
                    except:
                        pass
            else:
                listAdress = [ x[5] for x in listAds ]
    return result
    
print findIP('docs.python.org')
