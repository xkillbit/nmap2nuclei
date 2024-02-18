import xml.etree.ElementTree as ET

def convert_nmap_xml_to_nuclei_target(nmap_xml_file, output_file):
    tree = ET.parse(nmap_xml_file)
    root = tree.getroot()
    with open(output_file, 'w') as f:
        for host in root.findall('host'):
            ip_address = host.find('address').get('addr')
            for port in host.findall(".//port"):
                portid = port.get('portid')
                protocol = port.find('.//service').get('name')
                # Customize this part for different protocols or port numbers
                if protocol in ['http', 'https']:
                    url = f"{protocol}://{ip_address}:{portid}"
                    f.write(url + '\n')
                elif portid in ['80', '443']:  # Assuming HTTP for port 80 and HTTPS for port 443 by default
                    protocol = 'https' if portid == '443' else 'http'
                    url = f"{protocol}://{ip_address}"
                    f.write(url + '\n')

# Example usage
nmap_xml_file = input('Enter Name of Nmap XML File:')
output_file = 'nuclei_targets.txt'
convert_nmap_xml_to_nuclei_target(nmap_xml_file, output_file)
print('File converted! See nuclei_targets.txt in your current working directory')
