import urllib.request, json

def json_response(cve_ID):
    url = 'https://cve.circl.lu/api/cve/' + cve_ID
    response = urllib.request.urlopen(url)
    return json.loads(response.read().decode())

def capec_print(cve):
    json_data = json_response(cve)
    capec = json_data.get('capec')
    print("CAPEC - ", capec)
    print(type(capec))
    return capec
    
def cve_info_print(cve):
    json_data = json_response(cve)
    cve_info = json_data.get('summary')
    print("CVE Info - ", cve_info)
    return cve_info

def vulnerable_product_print(cve):
    json_data = json_response(cve)
    vulnerable_product = json_data.get('vulnerable_product')
    print("Vulnerable Product - ", vulnerable_product)
    return vulnerable_product
        # return vulnerable_each_product

# json_response(CVE_Number)
# capec_print()
# cve_info_print()
# vulnerable_product_print()

'''
    capec = data.get('capec')
    cve_info = data.get('summary')
    vulnerable_product = data.get('vulnerable_product')
    print("CVE Info - ", cve_info)
    print()
    print("CAPEC -")
    for capec_item in capec:
        for key,value in capec_item.items():
            print(key,": ", value)
        print()
    print("Vulnerable Products: ")
    for vulnerable_each_product in vulnerable_product:
        print(vulnerable_each_product)
    
'''