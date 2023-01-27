
import json
import os
from whoisapi import *
client = Client(api_key='at_NkK9aUmd4ZU1QJ8xwqtlVqAXRf0ra')

from openpyxl import load_workbook
wb = load_workbook("IPs.xlsx")  # Work Book
ws = wb['Servers']  # Work Sheet
column = ws['A']  # Column
column_list = [column[x].value for x in range(len(column))]
print(column_list)
print(len(column_list))

ip_address = column_list

try:

   for ipval in range(len(ip_address)):
        # Get parsed whois record as a model instance.
       whois = client.data(ip_address[ipval])
        # Get particular field of the whois record
        #print(whois.created_date_raw)


        # Get raw API response
       resp_str = client.raw_data(ip_address[ipval])

       params = RequestParameters(ip=1, ip_whois=1)

       whois = client.data(ip_address[ipval], params)

        #print(whois.domain_availability_raw)

        # Also you can modify default values of parameters:
       client.parameters.output_format = 'json'
       jsonFile =  client.raw_data((ip_address[ipval]))


       filename=(ip_address[ipval]) + ".json"
       save_dir = r"C:\Users\c.velarde.moreno\PycharmProjects\pythonclasses\jsonips"
       full_path = os.path.join(save_dir, filename)
       with open(full_path, 'w') as f:
           json_string=json.dumps(jsonFile)
           f.write(json_string)
           f.close()

       # print(client.raw_data(ip_address[ipval]))

        filename = "51.46.189.11.json"
        path = r"C:\Users\c.velarde.moreno\PycharmProjects\pythonclasses\jsonips\51.46.189.11.json"

        with open(path) as filename:
           json_data = json.loads(filename.read())
           print(json_data)
           print(type(json_data))
           rows_json = []
           import  json
           for data in json_data:
               domain_name_json = data['domainName']
               print(domain_name_json)
               registrar_Name = data['registrarName']
               contact_Email = data['contactEmail']
               created_Date = data['registryData.createdDate']
               registrant_country = data['registrant.country']
               #print(domain_name)

except ValueError as err:
    print("This one has an error!")
    #with open('failedips.txt', 'w') as f:
       # f.write(str(ip_address[ipval]))
       # f.write('\n')
