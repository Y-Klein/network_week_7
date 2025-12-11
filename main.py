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


print(mask_dec,"\n",ip_dec,"\n",network_address,"\n",broadcast_address,"\n",hosts_number,"\n",
      class_type,"\n",CIDR)
