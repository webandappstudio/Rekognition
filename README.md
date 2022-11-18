# Amazon Rekognition Image, Video, and Custom labels examples

## Purpose

Shows how to use the AWS SDK for Python (Boto3) with Amazon Rekognition to
recognize people, objects, and text in images and videos. 

* Detect faces, celebrities, objects, and text in an image.
* Create a collection of indexed faces and search for faces in your collection 
that match a reference image.
* Detect faces, celebrities, and objects in a video.
* Create a notification channel so your code can determine when a video
detection job has completed.

Also included are utilities that you can use with Amazon Rekognition Custom Labels.

*Amazon Rekognition makes it easy to add image and video analysis to your applications. 
You provide an image or video to the Amazon Rekognition API, and the service 
identifies objects, people, text, scenes, and activities.*
## ⚠ Important

- As an AWS best practice, grant this code least privilege, or only the 
  permissions required to perform a task. For more information, see 
  [Grant Least Privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) 
  in the *AWS Identity and Access Management 
  User Guide*.
- This code has not been tested in all AWS Regions. Some AWS services are 
  available only in specific Regions. For more information, see the 
  [AWS Region Table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)
  on the AWS website.
- Running this code might result in charges to your AWS account.

## Running the code

### Prerequisites

- You must have an AWS account, and have your default credentials and AWS Region
  configured as described in the [AWS Tools and SDKs Shared Configuration and
  Credentials Reference Guide](https://docs.aws.amazon.com/credref/latest/refdocs/creds-config-files.html).
- Python 3.7 or later
- Boto3 1.14.47 or later
- Requests 2.23.0 or later
- Pillow 7.2.0 or later 
- PyTest 5.3.5 or later (to run unit tests)

### Command

There are three demonstrations in this set of examples:

* Detecting items in a single image.
* Building a collection of indexed faces and searching for matches.
* Detecting items in a video.

**Image detection**

Run this example at a command prompt with the following command.

```commandline
python rekognition_image_detection.py
``` 

**Face collection**

Run this example at a command prompt with the following command.

### Example structure

The example contains the following files.

**rekognition_image_detection.py**

Shows how to use Amazon Rekognition image detection APIs. The `usage_demo` script 
detects faces, objects, text, and more by passing images to Amazon Rekognition. 

**rekognition_objects.py**

A set of classes that encapsulate data returned from Amazon Rekognition APIs,
such as faces, labels, and people. These classes are used to transform data from 
the service format to an object format.

---
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: Apache-2.0
