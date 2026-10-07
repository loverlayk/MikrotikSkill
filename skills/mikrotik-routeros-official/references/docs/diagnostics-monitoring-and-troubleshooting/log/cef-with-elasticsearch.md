# CEF with Elasticsearch

> This guide explains how to configure CEF log collection and analysis using Elasticsearch, Kibana, and Fleet Server with MikroTik RouterOS devices. It covers prerequisites, setup steps for both Elastic and RouterOS...

# CEF with Elasticsearch

## Introduction

Elasticsearch is a popular NoSQL database that can be used to store a wide range of data, including CEF logs. Along with Kibana you can create a powerful tool to analyze CEF logs from your RouterOS devices. This guide will rely on Elasticsearch integrations and for it to work you need to have a working Elasticsearch setup. This guide will not cover setup instructions for Elasticsearch and Kibana, but will cover the relevant steps to set up CEF log collection and analysis.

There are many possible configurations that can be made with Elasticsearch, but for the sake of this guide we will use the following principle:

- A RouterOS (10.0.0.1) device sends out CEF logs to a server (10.0.0.2) running [CEF integration](https://www.elastic.co/docs/reference/integrations/cef).
- The server (10.0.0.2) running CEF integration ingests CEF logs, processes the data and sends it to a [Fleet Server](https://www.elastic.co/guide/en/fleet/current/fleet-server.html) (10.0.0.3).
- The Fleet Server (10.0.0.3) stores the data in [Elasticsearch](https://www.elastic.co/elasticsearch) (10.0.0.4).
- [Kibana](https://www.elastic.co/kibana) (10.0.0.5) retrieves data from Elasticsearch (10.0.0.4), analyzes it and allows you to search the data.

:::info
This guide will not use [Logstash](https://www.elastic.co/logstash) as a part of analyzing CEF logs; it has been replaced by a Fleet Server.

:::

:::info
It is possible to install Elasticsearch, Kibana, Fleet Server and CEF logs integration on the same device.

:::

## Prerequisites

- [Setup Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html).  
  :::info
  Elasticsearch is widely supported on many platforms. It is recommended to set up a cluster of Elasticsearch nodes.
  :::
- [Setup Kibana](https://www.elastic.co/guide/en/kibana/current/setup.html).  
  :::info
  Kibana can be installed on the same device on which you installed Elasticsearch, but it can also be installed on a separate device for performance reasons. While it is possible to analyze CEF logs without Kibana, it requires writing your own API requests. Kibana is very easy to use and has a wide range of features.
  :::
- [Setup Fleet Server](https://www.elastic.co/guide/en/fleet/current/add-fleet-server-on-prem.html).  
  :::info
  It is possible to set up Fleet Server on the same device on which you installed Elasticsearch and/or Kibana. It is recommended to install Fleet Server on a different device. Refer to the Elasticsearch manual for recommendations on hardware and topology requirements.
  :::

## Setup

The setup instructions are divided into two parts: Elastic (configuration regarding Elasticsearch, Kibana and Fleet Server) and RouterOS (configuration that is relevant to your RouterOS device).

### Elastic

:::warning
Some steps might change over time, refer to Elastic's manual to find the most up-to-date steps.

:::

- [Log into your Kibana](https://www.elastic.co/guide/en/kibana/current/access.html).
- Open the [Fleet](https://www.elastic.co/guide/en/kibana/current/fleet.html) section under the main menu.
- Open the "[Agent policies](https://www.elastic.co/guide/en/fleet/current/agent-policy.html)" section.
- Press the "Create agent policy" button to [create a new Agent Policy](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#create-a-policy).
- Give the policy a name, for example, "CEF policy", adjust advanced settings if required, and create the policy. Or you can use the API request below:  

  ```text
  POST kbn:/api/fleet/agent_policies
  {
    "name": "CEF policy",
    "description": "",
    "namespace": "default",
    "monitoring_enabled": [
      "logs",
      "metrics"
    ],
    "inactivity_timeout": 1209600,
    "is_protected": false
  }
  ```

- Open your newly created policy by clicking on its name.
- Press the "[Add integration](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#add-integration)" button.
- Search for "[Common Event Format (CEF)](https://www.elastic.co/docs/reference/integrations/cef)" and press "Add Common Event Format (CEF)".
- Adjust configuration, make sure:  
  - Under the "Collect CEF application logs (input: udp)" section set "Syslog Host" to "0.0.0.0".  
  - Under the "Collect CEF application logs (input: tcp)" section set "Syslog Host" to "0.0.0.0".
- Save the integration.
- Press the "[Add Elastic Agent to your host](https://www.elastic.co/guide/en/fleet/current/elastic-agent-installation.html)" button.
- Follow the instructions on how to add Elastic Agent to your host.  
  :::info
  Elastic's official manual recommends installing the Elastic Agent as Fleet-managed. Consider following the recommendation since managing the agents is easier when they are Fleet-managed.
  :::
- Go to "Stack Management" on the main menu, then open "[Ingest Pipelines](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html)".
- Create a new Ingest Pipeline by pressing "[Create pipeline](https://www.elastic.co/guide/en/fleet/current/data-streams-pipeline-tutorial.html#data-streams-pipeline-one)" then "New pipeline".
- Set "Name" to "logs-cef.log@custom".
- Press "Import processors" and paste the following processors:  

  ```json
  {
  	"processors": [
  		{
  			"set": {
  			"ignore_empty_value": true,
  			"field": "host.name",
  			"copy_from": "cef.extensions.deviceHostName"
  			}
  		},
  		{
  			"set": {
  			"ignore_empty_value": true,
  			"field": "host.ip",
  			"copy_from": "cef.extensions.deviceAddress"
  			}
  		}
  	]
  }
  ```

  :::info
  The "logs-cef.log@custom" pipeline is not required, but it makes searching the logs easier when you are using Elasticsearch for other types of logs too.
  :::
- Press "Save pipeline".
- Make sure you have opened the 9003/UDP port on your host and elsewhere in the path from your RouterOS device (10.0.0.1).
- Your Elastic Agent is now ready to receive CEF logs.

### RouterOS

1. Configure a [remote logging action](../log/#send-the-log-to-a-syslog-server) on your RouterOS device (10.0.0.1):

   ```ros
   /system/logging/action
   add cef-event-delimiter="\n" name=syslog remote=10.0.0.2 \
       remote-log-format=cef remote-port=9003 \
       syslog-time-format=iso8601 target=remote
   ```

2. Add a rule for each of the [topics](../log/#topics) you want to receive from your RouterOS device (10.0.0.1), for example:

   ```ros
   /system/logging
   add action=syslog topics=info
   add action=syslog topics=error
   add action=syslog topics=critical
   add action=syslog topics=warning
   add action=syslog topics=bridge,stp
   ```

3. You should now start to see CEF logs being ingested.
4. Continue the guide to start using Kibana.

### Using Kibana

Kibana allows you to search the ingested CEF logs. To see ingested logs, do the following:

1. [Log into your Kibana](https://www.elastic.co/guide/en/kibana/current/access.html).
2. Open "Discover" from the main menu.
3. [Add a filter](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#explore-fields-in-your-data), and use the following parameters:  

   ```text
   Select a field: data_stream.dataset
   Select operator: IS
   Select a value: cef.log
   ```

4. For simplicity we recommend [searching for fields](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#explore-fields-in-your-data) in the  Discover menu and searching for "message", then adding the field to the view.
5. We also recommend searching for the "host.name" field and adding to the view as well.
6. Consider [saving the search](https://www.elastic.co/guide/en/kibana/current/save-open-search.html#_save_a_search) for easier access later.
7. Done!
