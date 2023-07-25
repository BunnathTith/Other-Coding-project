import random

def denary_to_bin(decimal):

    conversion_table = ['0', '1']
    binary = ''

    while decimal>0:
        remainder = decimal%2
        binary = conversion_table[remainder]+ binary
        decimal = decimal//2
    return binary

def denary_to_hex(decimal):
    conversion_table = ['0', '1', '2', '3' ,'4', '5', '6', '7' ,'8', '9', 'A', 'B', 'C', 'D' ,'E', 'F']
    hexa = ''

    while decimal > 0:
        remainder = decimal%16
        hexa = conversion_table[remainder] + hexa
        decimal = decimal // 16
    return hexa

def randomnumber(start, end):
    return random.randint(start, end)

def createIPv4():
    ipv4 = str(randomnumber(0, 225)) + '.' + str(randomnumber(0, 225)) + '.' +str(randomnumber(0, 225)) + '.' + str(randomnumber(0, 225))
    return ipv4

def storeIPv4(n):
    ipv4List = []
    for i in range(n):
        ipv4List.append(createIPv4())
    print ("New IPv4 addresses have been created: ", end = '')
    return ipv4List

def createIPv6():
    ipv6 = ''
    for i in range(7):
        ipv6 += denary_to_hex(randomnumber(0, 65535)) + ':'
    ipv6 += denary_to_hex(randomnumber(0, 65535))
    return ipv6

def createMAC():
    mac = ''
    for i in range(5):
        mac += denary_to_hex(randomnumber(0, 255)) + ':'
    mac += denary_to_hex(randomnumber(0, 255))
    return mac

def requestNetwork():
    print ("\tOption 1: Create an IPv4 address\n\tOption 2: Create an IPv6 address\n\tOption 3: Create a MAC address")
    num = int(input("Please select options 1/2/3: "))
    while num not in [1, 2, 3]:
        num = int(input("Re-enter options 1/2/3: "))
    if num == 1:
        print (createIPv4())
    elif num == 2:
        print (createIPv6())
    else:
        print (createMAC())
