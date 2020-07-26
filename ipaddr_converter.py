ipAddrList = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4"]

def convert_ip_addr(listOfIpAddrs):
    
    for i in range(len(listOfIpAddrs)):
        newIp = "10."
        subIp = listOfIpAddrs[i][4:]
        listOfIpAddrs[i] = newIp + subIp

    return listOfIpAddrs


print(convert_ip_addr(ipAddrList))
        
