from operator import index



def binary_to_decimal(binary_str):
    decimal_num = int(binary_str, 2)
    return decimal_num

def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num)[2:].zfill(8)
    return binary_num

def finding_the_index(mask):
    my_index = 0
    for num in range(len(mask)):
        if mask[num] == "0":
            my_index = index(num)
            break
    return my_index

def octet_validate(ip_or_masc:str):
    flag = True
    ip_or_masc = ip_or_masc.split(".")
    if len(ip_or_masc) != 4:
        flag = False
    for octet in ip_or_masc:
        if not (0<= int(octet) <= 255):
            flag = False
    return flag

def mask_validate(mask_bin):
    full_mask = ""
    for octet in mask_bin:
        full_mask += octet


    fleg = True

    if len(full_mask) != 32:
        fleg = False

    if full_mask[0] != "1" or full_mask[-1] != "0":
        fleg = False

    for num in full_mask:
        if num != "1" and num != "0" :
            fleg = False

    if int(full_mask[finding_the_index(full_mask):],2) > 0:
        fleg = False

    return fleg

def finding_the_network_address():
    pass
def finding_the_broadcast_address():
    pass
def finding_the_hosts_number():
    pass
def finding_the_cidr():
    pass