#!/usr/bin/python           # This is dns_query.py file
import struct
import socket
import time
import string
from bitstring import BitArray

class DQFlags: #DNS Query Flags
    QUERY = 0 # qr
    RESPONSE = 1 # qr
    STANDARD = 0 # op
    STATUS = 2 # op
    RECURSION_DESIRED = 1 # rd
    RECURSION_NOT_DESIRED = 0 # rd

class DRType: # DNS Record Type
    A = 1 # IPv4
    NS = 2 # an authoritative name server
    CNAME = 5 # the canonical name for an alias; not implemented
    SOA = 6 # marks the start of a zone of authority; not implemented
    WKS = 11 # a well known service description; not implemented
    PTR = 12 # a domain name pointer; not implemented
    HINFO = 13 # host information; not implemented
    MINFO = 14 #mailbox or mail list information; not implemented
    MX = 15 # mail exchange; not implemented
    TXT = 16 # text strings; not implemented
    RP = 17 # for responsible person; not implemented
    AFSDB = 18 # for AFS Data Base location; not implemented
    X25 = 19 # for X.25 PSDN address; not implemented
    AAAA = 28 # IPv6

class DQClass: # DNS Query Class
    IN = 1 # Internet
    CH = 3 # Chaos; not implemented
    HS = 4 # Hesiod not implemented
    NONE = 254 # not implemented
    ANY = 255 # not implmented 

class DnsQuery:
    _id = 1
    TIME_OUT = 20 # secondes
    def __init__(self):
        # qr: query/response, op: operation code, aa: authoritative answer flag, tc: truncation, rd: recursion desired, ra: recursion available, rc: response code
        self.op = self.rd = self.flags = None
        self.listQsr = self.aa = self.tc = self.ra = self.rc = 0
        try:
            self.id = struct.pack('>H', DnsQuery._id)
            DnsQuery._id += 1
        except:
            DnsQuery._id = 1
            self.id = struct.pack('>H', DnsQuery._id)
        # nbQ: number of questions, nbAn: number of answer resource records, nbAu: number of authority resource records, nbAd: number of additional resource records
        self.nbQ = self.nbAn = self.nbAu = self.nbAd = 0
        # q: question, an: answer resource records, au: authority resource records, ad: additional resource records
        self.request = self.listQs = self.listAns = self.listAus = self.listAds = ''
    def DnsNotInStr(self, data, index):
        result = ''
        length = struct.unpack('>B', data[index])[0]
        debut = True
        # print 'index', index
        while length != 0:
            if debut:
                debut = False
            else:
                result += '.'
            if length == 192:
                # print 'index', index
                # print 'length', length
                result += self.DnsNotInStr(data, struct.unpack('>B', data[index + 1])[0])[1]
                index += 2
                return index, result
            # print 'index', index
            # print 'length', length
            for i in range(index + 1, index + 1 + length):
                result += data[i]
            index = index + length + 1
            length = struct.unpack('>B', data[index])[0]
        index += 1
        return index, result
    def strInDnsNot(self,website):
        website = website.split('.')
        result = ''
        for i in website:
            result += struct.pack('>B', len(i))
            result += i
        # for i in range((len(result) % 32) / 8):
        result += struct.pack('>B', 0)
        return result
    def addQuestion(self, website, typ, cla):
        question = self.strInDnsNot(website) + struct.pack('>H',typ) + struct.pack('>H', cla)
        self.listQs += question
        self.nbQ += 1
    def convertInStr(self):
        self.flags = self.rc + (self.ra << 7) + (self.rd << 8) + (self.tc << 9) + (self.aa << 10) + (self.op << 11) + (self.listQsr << 15)
        self.request = self.id + struct.pack('>H', self.flags) + struct.pack('>H', self.nbQ) + struct.pack('>H', self.nbAn) + struct.pack('>H', self.nbAu) + struct.pack('>H', self.nbAd) + self.listQs + self.listAns + self.listAus + self.listAds
    def processRData(self, typ, data, index, length):
        result = ''
        # print typ
        if typ == DRType.A:
            for i in range(index, index + length - 1):
                result = result + str(ord(data[i])) + '.'
            result += str(ord(data[index + length - 1]))
        elif typ == DRType.NS:
            result += self.DnsNotInStr(data, index)[1]
        elif typ == DRType.AAAA:
            for i in range(index, index + length - 2, 2):
                result = result + '{:02x}'.format(ord(data[i])) + '{:02x}'.format(ord(data[i + 1])) + '.'
            result += '{:02x}'.format(ord(data[index + length - 2])) + '{:02x}'.format(ord(data[index + length - 1]))
        else:
            pass
        return result
    def process(self, data):
        aa = (ord(data[2]) >> 2) & 1 == 1
        tc = (ord(data[2]) >> 1) & 1 == 1
        ra = ord(data[3]) >> 7 == 1
        rc = ord(data[3]) & 0xF
        nbAn = struct.unpack('>H', data[6] + data[7])[0]
        nbAu = struct.unpack('>H', data[8] + data[9])[0]
        nbAd = struct.unpack('>H', data[10] + data[11])[0]
        if rc != 0:
            return aa, tc, ra, rc, nbAn, nbAu, nbAd, None, None, None
        else:
            index = len(self.request)
            listAns = []
            listAus = [] 
            listAds = []
            listTemp = [[listAns, nbAn], [listAus, nbAu], [listAds,nbAd]]
            # print listTemp
            for i in listTemp:
                # print 'oui', i[1]
                for j in range(i[1]):
                    # print index
                    temp = []
                    index, name = self.DnsNotInStr(data, index)
                    temp.append(name)
                    # print name
                    typ = struct.unpack('>H', data[index] + data[index + 1])[0]
                    temp.append(typ)
                    temp.append(struct.unpack('>H', data[index + 2] + data[index + 3])[0])
                    temp.append(struct.unpack('>I', data[index + 4] + data[index + 5] + data[index + 6] + data[index + 7])[0])
                    length = struct.unpack('>H', data[index + 8] + data[index + 9])[0]
                    temp.append(length)
                    # print 'length', length
                    index = index + 10
                    temp.append(self.processRData(typ, data, index, length))
                    index += length
                    i[0].append(temp)
            return aa, tc, ra, rc, nbAn, nbAu, nbAd, listAns, listAus, listAds
    def sendQuery(self, ip):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        host = ip
        port = 53
        bytes = BitArray(bytes=self.request)
        print bytes.bin
        s.sendto(self.request, (host, port))
        timeStart = time.time()
        s.settimeout(DnsQuery.TIME_OUT)
        while(time.time() - timeStart < DnsQuery.TIME_OUT):
            result, addr = s.recvfrom(1024)
            if addr == (host,port) and string.find(result,self.id) == 0:
                print BitArray(bytes=result).bin
                return self.process(result)
            else:
                print 'oups'
