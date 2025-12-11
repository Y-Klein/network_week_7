from  core.utils import *
from  core.output_string import *

flag = True
while flag:
    ip_dec = input("● IP address in format: x.x.x.x: ")
    mask_dec = input("● Mask network in format: x.x.x.x: ")
    if octet_validate(ip_dec) and octet_validate(mask_dec) and mask_validate(mask_dec):
        flag = False
    else:
        print("One or more of the data entered is incorrect. Please try again.")
ip = ip_format_to_binary(ip_dec)
mask = ip_format_to_binary(mask_dec)
network_address = binary_to_ip_format(finding_the_network_address(mask,ip))
broadcast_address = binary_to_ip_format(finding_the_broadcast_address(mask,ip))
hosts_number = finding_the_hosts_number(mask)
class_type = finding_the_cidr(mask,ip)
CIDR = len(mask[:finding_the_index(mask)])

with open(f"subnet_info_{ip_dec}_321424855.txt","w") as file:
    file.write(f"{format_input_ip(ip_dec)}{format_subnet_mask(mask_dec)}"
               f"{format_classful_status(class_type)}{format_network_address(network_address)}"
               f"{format_broadcast_address(broadcast_address)}{format_num_hosts(hosts_number)}"
               f"{format_cidr_mask(CIDR)}")