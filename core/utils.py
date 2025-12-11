from operator import index



def binary_to_decimal(binary_str):
    decimal_num = int(binary_str, 2)
    return decimal_num

def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num)[2:].zfill(8)
    return binary_num

def ip_format_to_binary(ip_or_mask):
    full = ""
    for octet in ip_or_mask.split("."):
        full += decimal_to_binary(int(octet))
    return full
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
    full_mask = ip_format_to_binary(mask_bin)
    fleg = True

    if len(full_mask) != 32:
        fleg = False

    if full_mask[0] != "1" or full_mask[-1] != "0":
        fleg = False

    if int(full_mask[finding_the_index(full_mask):],2) > 0:
        fleg = False

    return fleg

def mask_by_split(mask,binary_str):
    my_index = finding_the_index(mask)
    network = binary_str[:my_index]
    host = binary_str[my_index:]
    return


def finding_the_network_address(mask,ip):
    my_index = finding_the_index(mask)
    ip = ip[:my_index] + "0" * len(ip[my_index:])
    return ip

def finding_the_broadcast_address(mask,ip):
    my_index = finding_the_index(mask)
    ip = ip[:my_index] + "1" * len(ip[my_index:])
    return ip

def finding_the_hosts_number(mask):
    my_index = finding_the_index(mask)
    result = (2 ** len(mask[my_index:])) - 2
    return result

def finding_the_cidr(mask,ip):
    my_index = finding_the_index(mask)

    if 0< binary_to_decimal(ip[:8]) <=127 and len(mask[:my_index]) == 8:
        return "Class A"
    elif 128<= binary_to_decimal(ip[:8]) <=191 and len(mask[:my_index]) == 16:
        return "Class B"
    elif 192<= binary_to_decimal(ip[:8]) <=223 and len(mask[:my_index]) == 24:
        return "Class C"
    else:
        return "Classless"

def binary_to_ip_format(bin_num):
    result = (f"{binary_to_decimal(bin_num[:8])}.{binary_to_decimal(bin_num[8:16])}"
              f".{binary_to_decimal(bin_num[16:24])}.{binary_to_decimal(bin_num[24:])}")
    return result


