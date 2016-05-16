# -*- coding: utf-8 -*-

from pprint import pprint
from hpOneView.oneview_client import OneViewClient

config = {
    "ip": "172.16.102.59",
    "credentials": {
        "authLoginDomain": "",
        "userName": "administrator",
        "password": ""
    }
}

options = {
    "name": "OneViewSDK Test FC Network",
    "connectionTemplateUri": None,
    "autoLoginRedistribution": True,
    "fabricType": "FabricAttach",
}
oneview_client = OneViewClient(config)

# Creates a FC Network
fc_network = oneview_client.fc_networks.create(options)
print("Created fc-network '%s' sucessfully.\n  uri = '%s'" % (fc_network['name'], fc_network['uri']))

# Updates the created network
fc_network['autoLoginRedistribution'] = False
fc_network = oneview_client.fc_networks.update(fc_network)
print("Updated fc-network '%s' sucessfully.\n  uri = '%s' \n  with attribute {'autoLoginRedistribution': %s}" \
      % (fc_network['name'], fc_network['uri'], fc_network['autoLoginRedistribution']))

# Get all, with defaults
fc_nets = oneview_client.fc_networks.get_all()
pprint(fc_nets)

# Filter by name
fc_nets_filtered = oneview_client.fc_networks.get_all(filter='name="MyFibreNetwork"')
pprint(fc_nets_filtered)

# Sort by name descending
fc_nets_sorted = oneview_client.fc_networks.get_all(sort='name:descending')
pprint(fc_nets_sorted)

# Gets the second record
fc_nets_limited = oneview_client.fc_networks.get_all(1, 1)
pprint(fc_nets_limited)

# Gets by example
fc_nets_gotby = oneview_client.fc_networks.get_by('name', 'MyFibreNetwork')
pprint(fc_nets_gotby)

# Deletes the created network
oneview_client.fc_networks.delete(fc_network)