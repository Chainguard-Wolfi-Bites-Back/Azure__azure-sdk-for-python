# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.streamanalytics import StreamAnalyticsManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-streamanalytics
# USAGE
    python streaming_job_create_user_assigned_identity.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = StreamAnalyticsManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="56b5e0a9-b645-407d-99b0-c64f86013e3d",
    )

    response = client.streaming_jobs.begin_create_or_replace(
        resource_group_name="sjrg",
        job_name="sjName",
        streaming_job={
            "identity": {
                "type": "UserAssigned",
                "userAssignedIdentities": {
                    "/subscriptions/fa68082f-8ff7-4a25-95c7-ce9da541242f/resourceGroups/akvenkat/providers/Microsoft.ManagedIdentity/userAssignedIdentities/sdkIdentity": {}
                },
            },
            "location": "West US",
            "properties": {
                "compatibilityLevel": "1.0",
                "dataLocale": "en-US",
                "eventsLateArrivalMaxDelayInSeconds": 16,
                "eventsOutOfOrderMaxDelayInSeconds": 5,
                "eventsOutOfOrderPolicy": "Drop",
                "functions": [],
                "inputs": [],
                "outputErrorPolicy": "Drop",
                "outputs": [],
                "sku": {"name": "Standard"},
            },
            "tags": {"key1": "value1", "key3": "value3", "randomKey": "randomValue"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/streamanalytics/resource-manager/Microsoft.StreamAnalytics/preview/2021-10-01-preview/examples/StreamingJob_Create_UserAssignedIdentity.json
if __name__ == "__main__":
    main()
