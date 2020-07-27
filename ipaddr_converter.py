

def convert_ip_addr(listOfIpAddrs):
    for i in range(len(listOfIpAddrs)):
        newIp = "10."
        subIp = listOfIpAddrs[i][4:]
        listOfIpAddrs[i] = newIp + subIp

    return listOfIpAddrs


filePath = input("Please enter the absolute file path of the list of IP addresses you would like to convert: ")
newFilePath = input("Please enter the absolute file path of where you would like to save the new IPs to: ")
ipAddrs = open(filePath)
newList = ipAddrs.readline().split(" ")
updatedList = convert_ip_addr(newList)

ipAddrs.close()

new_ips = open(newFilePath, 'w')

new_ips.write(" ".join(updatedList))

new_ips.close()

