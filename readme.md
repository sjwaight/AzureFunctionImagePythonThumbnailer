# Python Azure Function - JPEG Thumbnail creation

Sample Python Function that reads a message from an [Azure Storage Queue](https://docs.microsoft.com/azure/storage/queues/storage-queues-introduction) and receives a Blob (JPEG) from [Azure Blob Storage](https://docs.microsoft.com/azure/storage/blobs/storage-blobs-introduction) using an [Azure Function](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview) Input Binding which is then thumbnailed using [Pillow](https://python-pillow.org/) before the thumbnail image is uploaded back to Blob Storage using an Azure Function Output Binding.

If you're new to Azure Functions and want to understand how you can use Python with them, you should check out the official guide on [Azure Functions for Python developers](https://docs.microsoft.com/azure/azure-functions/functions-reference-python).

This repository is using a GitHub Action to bundle the Azure Function into a Docker Container so it can be run on Kubernetes with [KEDA](https://keda.sh/), but if you'd like to just bundle a Function and deploy to Azure without using a Container then you can follow the [published guide on Microsoft Docs](https://docs.microsoft.com/azure/azure-functions/functions-how-to-github-actions?tabs=python).

If you'd like to try this out you will need:

1. An Azure Subscription (you can get a free trial at https://azure.com/free)
2. An Azure Storage Account that has:
    1. Two Storage Containers
    2. One Storage Queue
3. An Azure Function App (Service Plan or Consumption is fine).
4. Make sure to include configuration settings value for the 'customserverless01_STORAGE' connection string.

There is an associated post that has some background on this Function sample that you can [find on my blog](https://blog.siliconvalve.com/2020/10/29/reading-and-writing-binary-files-with-python-with-azure-functions-input-and-output-bindings/).
