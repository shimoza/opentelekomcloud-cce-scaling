import urllib.request 
import time 
import http.client
import json

interval = 30*60 #30 minutes 
conn = dict()

def do_post(req_number): 

    conn = http.client.HTTPSConnection("cce.eu-de.otc.t-systems.com")
payload = json.dumps({
  "kind": "Node",
  "apiVersion": "v3",
  "metadata": {
    "name": "node"
  },
  "spec": {
    "flavor": "s3.large.2",
    "az": "eu-de-02",
    "faultDomain": "",
    "os": "CentOS 7.7",
    "login": {
      "sshKey": "SSHKEY"
    },
    "rootVolume": {
      "size": 40,
      "volumetype": "SATA"
    },
    "dataVolumes": [
      {
        "size": 100,
        "volumetype": "SATA"
      }
    ],
    "billingMode": 0,
    "count": 2,
    "extendParam": {
      "isAutoRenew": "false",
      "isAutoPay": "false",
      "alpha.cce/postInstall": "",
      "DockerLVMConfigOverride": "dockerThinpool=vgpaas/90%VG;kubernetesLV=vgpaas/10%VG;diskType=evs;lvType=linear"
    },
    "nodeNicSpec": {
      "primaryNic": {
        "subnetId": "a5dd5a3d-1f17-4362-b25a-9be2d81bae1c"
      }
    }
  }
})
headers = {
  'Content-Type': 'application/json',
  'X-Auth-Token': 'XXXXXx',
  'Authorization': 'Bearer XXXXX'
}
conn.request("POST", "/api/v3/projects/a5dd5a3d-1f17-4362-b25a-9be2d81bae1c/clusters/8d4e599a-ca8f-11eb-93ba-0255ac1016af/nodes", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
 
# Treshold check
while True: 
    req = urllib.request.Request('URI' + str(interval)) 
    with urllib.request.urlopen(req) as response: 
        the_page = response.read() 
 
    r = int(the_page) 
 
    if ( r > 40) :
        do_post(r) 
 
    time.sleep(interval)