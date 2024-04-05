import re
from scapy.all import Raw


def regex_search(packet, data):
    try:
        # packet.show()
        regex = data["regex"]
        text = packet[Raw].load.decode("utf-8")
        pattern = re.compile(regex)
        match = pattern.search(text)
        if match:
            return True
        else:
            return False
    except:
        return False


def keyword_search(packet, data):
    try:
        keyword = data["keyword"]
        s = packet[Raw].load.decode("utf-8")
        si = s.find(keyword)
        if si == -1:
            return False
        else:
            return True        
    except :
        return False