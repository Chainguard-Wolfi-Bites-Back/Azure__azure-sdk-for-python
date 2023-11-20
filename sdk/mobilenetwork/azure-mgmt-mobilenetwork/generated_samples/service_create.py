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
    python service_create.py

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

    response = client.services.begin_create_or_update(
        resource_group_name="rg1",
        mobile_network_name="testMobileNetwork",
        service_name="TestService",
        parameters={
            "location": "eastus",
            "properties": {
                "pccRules": [
                    {
                        "ruleName": "default-rule",
                        "rulePrecedence": 255,
                        "ruleQosPolicy": {
                            "5qi": 9,
                            "allocationAndRetentionPriorityLevel": 9,
                            "maximumBitRate": {"downlink": "1 Gbps", "uplink": "500 Mbps"},
                            "preemptionCapability": "NotPreempt",
                            "preemptionVulnerability": "Preemptable",
                        },
                        "serviceDataFlowTemplates": [
                            {
                                "direction": "Uplink",
                                "ports": [],
                                "protocol": ["ip"],
                                "remoteIpList": ["10.3.4.0/24"],
                                "templateName": "IP-to-server",
                            }
                        ],
                        "trafficControl": "Enabled",
                    }
                ],
                "servicePrecedence": 255,
                "serviceQosPolicy": {
                    "5qi": 9,
                    "allocationAndRetentionPriorityLevel": 9,
                    "maximumBitRate": {"downlink": "1 Gbps", "uplink": "500 Mbps"},
                    "preemptionCapability": "NotPreempt",
                    "preemptionVulnerability": "Preemptable",
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/mobilenetwork/resource-manager/Microsoft.MobileNetwork/stable/2023-09-01/examples/ServiceCreate.json
if __name__ == "__main__":
    main()
