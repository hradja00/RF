import re

LOG_FILE = "setupapi.dev.log"
DEVICE_START_STR = "[Device Install"
is_device_found = False

with open(LOG_FILE) as f:
    for line in f:
        m = re.search(r'\[Device Install .*#(.*?&.*?)&(.*?)&(.*?)#(.*)#', line)
        if is_device_found:
            print(f"\t{line}")
            is_device_found = False

        if m:
            vendor_ID = m.group(1)
            product_ID = m.group(2)
            revision = m.group(3)
            serial_num = m.group(4)
            #print(m.group())
            #print(serial_num)
            #(f"Vendor ID: {vendor_ID}")
            print(f"\nVendor ID: {vendor_ID}\n\t~Product ID: {product_ID}\n\t~Revision: {revision}\n\t~Serial number: {serial_num}")
            is_device_found = True