#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This application demonstrates how to perform basic operations on topics
with the Cloud Pub/Sub API.

For more information, see the README.md under /pubsub and the documentation
at https://cloud.google.com/pubsub/docs.
"""

# [START quickstart]
from gcloud import pubsub

pubsub_client = pubsub.Client.from_service_account_json(
    # Path to Service Account file. Defaults to the value of the
    # GOOGLE_APPLICATION_CREDENTIALS environment variable.
    '/path/to/keyfile.json',

    # Your Project ID. Defaults to the value of the
    # GCLOUD_PROJECT environment variable.
    project='your-project-id'
)

topic = pubsub_client.topic('my-new-topic')
topic.create()
# [END quickstart]