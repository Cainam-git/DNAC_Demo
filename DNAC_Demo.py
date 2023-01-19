import requests
import urllib3.exceptions

# Disable certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Declare API BASE URL
base_url = "https://sandboxdnac.cisco.com/"

########################
# RETRIEVE LOGIN TOKEN #
########################


def get_token():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
    }

    response = requests.request(method="POST",
                                url=base_url + "dna/system/api/v1/auth/token",
                                headers=headers,
                                verify=False).json()

    # Parse out the token and return it
    token = response['Token']
    return token


###########################
# GET ALL NETWORK DEVICES #
###########################


def get_network_devices(token):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Auth-Token': token
    }

    response = requests.request(method="GET",
                                url=base_url + "dna/intent/api/v1/network-device/",
                                headers=headers,
                                verify=False).json()
    return response

######################
# START MAIN SCRIPT #
#####################


if __name__ == '__main__':
    # Fetch the login token
    login_token = get_token()

    # Obtain a list of all network devices
    list_of_net_devices = get_network_devices(login_token)

    #############################################################
    # Print out some basic information about all network devices#
    #############################################################
    print("*************************************************")

    for device in list_of_net_devices['response']:
        print(f"Type:          {device['series']}")
        print(f"IP:            {device['managementIpAddress']}")
        print(f"Hostname:      {device['hostname']}")
        print(f"Serial Number: {device['serialNumber']}")
        print(f"UpTime:        {device['upTime']}")
        print(f"id:            {device['id']}")
        print("*************************************************")
    #############################################################
