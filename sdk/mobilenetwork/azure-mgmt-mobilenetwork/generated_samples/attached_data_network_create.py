# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.mobilenetwork import MobileNetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-mobilenetwork
# USAGE
    python attached_data_network_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MobileNetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.attached_data_networks.begin_create_or_update(
        resource_group_name="rg1",
        packet_core_control_plane_name="TestPacketCoreCP",
        packet_core_data_plane_name="TestPacketCoreDP",
        attached_data_network_name="TestAttachedDataNetwork",
        parameters={
            "location": "eastus",
            "properties": {
                "dnsAddresses": ["1.1.1.1"],
                "naptConfiguration": {
                    "enabled": "Enabled",
                    "pinholeLimits": 65536,
                    "pinholeTimeouts": {"icmp": 30, "tcp": 180, "udp": 30},
                    "portRange": {"maxPort": 49999, "minPort": 1024},
                    "portReuseHoldTime": {"tcp": 120, "udp": 60},
                },
                "userEquipmentAddressPoolPrefix": ["2.2.0.0/16"],
                "userEquipmentStaticAddressPoolPrefix": ["2.4.0.0/16"],
                "userPlaneDataInterface": {"name": "N6"},
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/mobilenetwork/resource-manager/Microsoft.MobileNetwork/stable/2023-09-01/examples/AttachedDataNetworkCreate.json
if __name__ == "__main__":
    main()
