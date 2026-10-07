# Syslog with Elasticsearch

> This guide explains how to configure Syslog data collection and analysis using Elasticsearch, Kibana, and Fleet Server with MikroTik RouterOS devices. It covers prerequisites, setup steps for both Elastic and...

# Syslog with Elasticsearch

## Introduction

Elasticsearch is a popular NoSQL database that can be used to store a wide range of data, including Syslog data. Alongside Kibana you can create a powerful tool to analyze Syslog data from your RouterOS devices. This guide will rely on Elasticsearch integrations and for it to work you need to have a working Elasticsearch setup. This guide will not cover setup instructions for Elasticsearch and Kibana, but will cover the relevant steps to set up Syslog data collection and analysis.

There are many possible configurations that can be made with Elasticsearch, but for the sake of this guide we will use the following principle:

- A RouterOS (10.0.0.1) device sends out Syslog data to a server (10.0.0.2) running [Custom UDP logs](https://www.elastic.co/docs/current/integrations/udp).
- The server (10.0.0.2) running the Custom UDP logs integration ingests Syslog data, processes the data and sends it to a [Fleet Server](https://www.elastic.co/guide/en/fleet/current/fleet-server.html) (10.0.0.3).
- A Fleet Server (10.0.0.3) stores the data in [Elasticsearch](https://www.elastic.co/elasticsearch) (10.0.0.4).
- [Kibana](https://www.elastic.co/kibana) (10.0.0.5) retrieves data from Elasticsearch (10.0.0.4), analyzes it and allows you to search the data.

:::info
This guide will not use [Logstash](https://www.elastic.co/logstash) as a part of analyzing Syslog data; it has been replaced by a Fleet Server.

:::

:::info
It is possible to install Elasticsearch, Kibana, Fleet Server and Custom UDP logs integration on the same device.

:::

## Prerequisites

- [Set up Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html).  
  :::info
  Elasticsearch is widely supported on many platforms. It is recommended to set up a cluster of Elasticsearch nodes.
  :::
- [Set up Kibana](https://www.elastic.co/guide/en/kibana/current/setup.html).  
  :::info
  Kibana can be installed on the same device on which you installed Elasticsearch, but it can also be installed on a separate device for performance reasons. While it is possible to analyze Syslog data without Kibana, it requires writing your own API requests, but Kibana is very easy to use and has a wide range of features.
  :::
- [Setup Fleet Server](https://www.elastic.co/guide/en/fleet/current/add-fleet-server-on-prem.html).  
  :::info
  It is possible to set up Fleet Server on the same device on which you installed Elasticsearch and/or Kibana. It is recommended to install Fleet Server on a different device. Refer to Elasticsearch manual for recommendations on hardware and topology requirements.
  :::

## Setup

The setup instructions are divided into two parts: Elastic (configuration regarding Elasticsearch, Kibana and Fleet Server) and RouterOS (configuration that is relevant to your RouterOS device).

### Elastic

:::warning
Some steps might change over time. Refer to Elastic's manual to find the most up-to-date steps.

:::

1. [Log into your Kibana](https://www.elastic.co/guide/en/kibana/current/access.html).
2. Open the [Fleet](https://www.elastic.co/guide/en/kibana/current/fleet.html) section under the main menu.
3. Open the "[Agent policies](https://www.elastic.co/guide/en/fleet/current/agent-policy.html)" section.
4. Press the "Create agent policy" button to [create a new Agent Policy](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#create-a-policy).
5. Give the policy a name, for example, "Syslog policy", adjust advanced settings if required, create the policy. Or you can use the API request below:  

   ```text
   POST kbn:/api/fleet/agent_policies
   {
     "name": "Syslog policy",
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

6. Open your newly created policy by clicking on its name.
7. Press "[Add integration](https://www.elastic.co/guide/en/fleet/current/agent-policy.html#add-integration)".
8. Search for "[Custom UDP logs](https://www.elastic.co/docs/current/integrations/udp)" and press "Add Custom UDP logs".
9. Adjust the configuration, and make sure:  
   - Set "Listen Address" to the IP address of your server that is going to run the Custom UDP logs integration , in this example the address should be "10.0.0.2".  
   - Set "Listen Port" to "5514".  
   - Set "Dataset name" to "routeros".  
   - Set "Ingest Pipeline" to "logs-routeros@custom".  
   - Set "Syslog Parsing" to "Yes".
10. Save the integration.
11. Press the "[Add Elastic Agent to your host](https://www.elastic.co/guide/en/fleet/current/elastic-agent-installation.html)" button.
12. Follow the instructions on how to add Elastic Agent to your host.  
    :::info
    The official Elastic manual recommends installing the Elastic Agent as Fleet-managed. Consider following the recommendation since managing the agents is easier when they are Fleet-managed.
    :::
13. Go to "Stack Management" on the main menu, then open "[Ingest Pipelines](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html)".
14. Create a new Ingest Pipeline by pressing "[Create pipeline](https://www.elastic.co/guide/en/fleet/current/data-streams-pipeline-tutorial.html#data-streams-pipeline-one)" then "New pipeline".
15. Set "Name" to "logs-routeros@custom".
16. Press "Import processors" and paste the following processors:  

    ```json
    {
    	"processors": [
    		{
    			"grok": {
    			"field": "message",
    			"patterns": [
    				"^first L2TP UDP packet received from %{IP:source.ip}$",
    				"^login failure for user %{USERNAME:user.name} from %{IP:source.ip} via %{DATA:service.name}$",
    				"^%{USERNAME:user.name} logged in, %{IP:client.ip} from %{IP:source.ip}$",
    				"^dhcp alert on %{DATA}: discovered unknown dhcp server, mac %{MAC:source.mac}, ip %{IP:source.ip}$",
    				"in:%{DATA} out:%{DATA}, ?(connection-state:%{DATA},|)?(src-mac %{MAC:source.mac},|) proto %{DATA:network.transport} \\(%{DATA}\\), %{IP:source.ip}:?(%{INT:source.port}|)->%{IP:destination.ip}:?(%{INT:destination.port}|), len %{INT:network.bytes}$",
    				"in:%{DATA} out:%{DATA}, ?(connection-state:%{DATA},|)?(src-mac %{MAC:source.mac},|) proto %{DATA:network.transport}, %{IP:source.ip}:?(%{INT:source.port}|)->%{IP:destination.ip}:?(%{INT:destination.port}|), len %{INT:network.bytes}$",
    				"^%{DATA:network.name} (deassigned|assigned) %{IP:client.ip} for %{MAC:client.mac} %{DATA}$",
    				"^%{DATA:user.name} logged out, %{INT:event.duration} %{INT} %{INT} %{INT} %{INT} from %{IP:client.ip}$",
    				"^user %{DATA:user.name} logged out from %{IP:source.ip} via %{DATA:service.name}$",
    				"^user %{DATA:user.name} logged in from %{IP:source.ip} via %{DATA:service.name}$",
    				"^%{DATA:network.name} client %{MAC:client.mac} declines IP address %{IP:client.ip}$",
    				"^%{DATA:network.name} link up \\(speed %{DATA}\\)$",
    				"^%{DATA:network.name} link down$",
    				"^user %{DATA:user.name} authentication failed$",
    				"^%{DATA:network.name} fcs error on link$",
    				"^phase1 negotiation failed due to time up %{IP:source.ip}\\[%{INT:source.port}\\]<=>%{IP:destination.ip}\\[%{INT:destination.port}\\] %{DATA}:%{DATA}$",
    				"^%{DATA:network.name} (learning|forwarding)$",
    				"^user %{DATA:user.name} is already active$",
    				"^%{GREEDYDATA}$"
    			]
    			}
    		},
    		{
    			"lowercase": {
    			"field": "network.transport",
    			"ignore_missing": true
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.category",
    			"description": "Enrich logon events",
    			"allow_duplicates": false,
    			"value": [
    				"authentication"
    			],
    			"if": "ctx.message =~ /(login failure for user|logged in from|logged in,)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.outcome",
    			"description": "Enrich successful login events",
    			"allow_duplicates": false,
    			"value": [
    				"success"
    			],
    			"if": "ctx.message =~ /(logged in from|logged in,)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.outcome",
    			"description": "Enrich failed login events",
    			"allow_duplicates": false,
    			"value": [
    				"failure"
    			],
    			"if": "ctx.message =~ /(login failure for user)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.category",
    			"description": "Enrich network events",
    			"allow_duplicates": false,
    			"value": [
    				"network"
    			],
    			"if": "ctx.message =~ /( fcs error on link| link down| link up)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.outcome",
    			"description": "Enrich network failures",
    			"allow_duplicates": false,
    			"value": [
    				"failure"
    			],
    			"if": "ctx.message =~ /( fcs error on link)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.category",
    			"allow_duplicates": false,
    			"value": [
    				"session"
    			],
    			"if": "ctx.message =~ /(logged out)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "event.category",
    			"allow_duplicates": false,
    			"value": [
    				"threat"
    			],
    			"if": "ctx.message =~ /(from address that has not seen before)/"
    			}
    		},
    		{
    			"append": {
    			"ignore_failure": true,
    			"field": "service.name",
    			"value": [
    				"l2tp"
    			],
    			"if": "ctx.message =~ /(^L2TP\\/IPsec VPN)/"
    			}
    		},
    		{
    			"geoip": {
    			"ignore_failure": true,
    			"ignore_missing": true,
    			"field": "source.ip",
    			"target_field": "source.geo"
    			}
    		},
    		{
    			"geoip": {
    			"ignore_failure": true,
    			"ignore_missing": true,
    			"field": "destination.ip",
    			"target_field": "destination.geo"
    			}
    		},
    		{
    			"geoip": {
    			"ignore_failure": true,
    			"ignore_missing": true,
    			"field": "client.ip",
    			"target_field": "client.geo"
    			}
    		}
    	]
    }
    ```

17. Press "Save pipeline".
18. Go to "Stack Management" on the main menu, then select "Index Management" and then select "Component templates".
19. Create a new template by pressing "Create component template".
20. Set the "Name" to "logs-routeros@custom".
21. Under the "Index settings" section, paste the following:  

    ```json
    {
      "index": {
        "lifecycle": {
          "name": "logs"
        },
        "default_pipeline": "logs-routeros@custom"
      }
    }
    ```

    :::info
    Change the ILM policy to your required policy name. The "logs" policy is the default policy that might be in use for other logs.
    :::
22. Under the "Mappings" section, press "Load JSON" and paste the following:  

    ```json
    {
      "dynamic_templates": [],
      "properties": {
        "service": {
          "type": "object",
          "properties": {
            "name": {
              "type": "keyword"
            }
          }
        },
        "destination": {
          "type": "object",
          "properties": {
            "port": {
              "type": "long"
            },
            "ip": {
              "type": "ip"
            }
          }
        },
        "host": {
          "type": "object",
          "properties": {
            "ip": {
              "type": "ip"
            }
          }
        },
        "client": {
          "type": "object",
          "properties": {
            "ip": {
              "type": "ip"
            },
            "mac": {
              "type": "keyword"
            }
          }
        },
        "source": {
          "type": "object",
          "properties": {
            "geo": {
              "type": "object",
              "properties": {
                "continent_name": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "region_iso_code": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "city_name": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "country_iso_code": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "country_name": {
                  "ignore_above": 1024,
                  "type": "keyword"
                },
                "location": {
                  "type": "geo_point"
                },
                "region_name": {
                  "ignore_above": 1024,
                  "type": "keyword"
                }
              }
            },
            "as": {
              "type": "object",
              "properties": {
                "number": {
                  "type": "long"
                },
                "organization": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "ignore_above": 1024,
                      "type": "keyword",
                      "fields": {
                        "text": {
                          "type": "match_only_text"
                        }
                      }
                    }
                  }
                }
              }
            },
            "address": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "port": {
              "type": "long"
            },
            "domain": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "ip": {
              "type": "ip"
            },
            "mac": {
              "type": "keyword"
            }
          }
        },
        "event": {
          "type": "object",
          "properties": {
            "duration": {
              "type": "long"
            },
            "category": {
              "type": "keyword"
            },
            "outcome": {
              "type": "keyword"
            }
          }
        },
        "message": {
          "type": "match_only_text"
        },
        "user": {
          "type": "object",
          "properties": {
            "name": {
              "type": "keyword"
            }
          }
        },
        "network": {
          "type": "object",
          "properties": {
            "bytes": {
              "type": "long"
            },
            "name": {
              "type": "keyword"
            },
            "transport": {
              "type": "keyword"
            }
          }
        },
        "tags": {
          "ignore_above": 1024,
          "type": "keyword"
        }
      }
    }
    ```

23. Press "Next" and then press "Save component template".  
    :::warning
    If a component template exists with such a name, then edit the existing one instead.
    :::
24. Go to "Stack Management" on the main menu, then select "Index Management" and then select "Index templates".
25. Create a new template by pressing "Create template".
26. Set the "Name" to "logs-routeros".
27. Set "Index patterns" to "logs-routeros-\*".
28. Under "Component templates" section add the following templates to your new Index template:  

    ```text
    logs@settings
    logs-routeros@custom
    ecs@mappings
    ```

29. Press "Next" and then "Save template".
30. Make sure you have opened the 5514/UDP port on your host and elsewhere in the path from your RouterOS device (10.0.0.1).
31. Your Elastic Agent is now ready to receive Syslog data!

### RouterOS

1. Configure the [remote logging action](../log/#send-the-log-to-a-syslog-server) on your RouterOS device (10.0.0.1):

   ```ros
   /system/logging/action
   set [find where name="remote"] remote-log-format=syslog \
       remote=10.0.0.2 remote-port=5514 syslog-facility=syslog
   ```

2. Add a rule for each of the [topics](../log/#topics) you want to receive from your RouterOS device (10.0.0.1), for example:

   ```ros
   /system/logging
   add action=remote topics=info
   add action=remote topics=error
   add action=remote topics=critical
   add action=remote topics=warning
   add action=remote topics=bridge,stp
   ```

3. You should now start to see Syslog data being ingested.
4. Continue the guide to start using Kibana.

## Using Kibana

Kibana allows you to search the ingested Syslog data. To see ingested logs, do the following:

1. [Log into your Kibana](https://www.elastic.co/guide/en/kibana/current/access.html).
2. Open "Discover" from the main menu.
3. [Add a filter](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#explore-fields-in-your-data), and use the following parameters:  

   ```text
   Select a field: data_stream.dataset
   Select operator: IS
   Select a value: routeros
   ```

4. For simplicity we recommend [searching for fields](https://www.elastic.co/guide/en/kibana/current/discover-get-started.html#explore-fields-in-your-data) in the  Discover menu and searching for "message", then adding the field to the view.
5. We also recommend searching for the "log.syslog.hostname" field and adding it to the view as well.
6. Consider [saving the search](https://www.elastic.co/guide/en/kibana/current/save-open-search.html#_save_a_search) for easier access later.
7. Done.

:::tip
While searching for logs can be useful, you are more likely looking for a way to create [alerts](https://www.elastic.co/guide/en/kibana/current/alerting-getting-started.html) for certain activities and create [connectors](https://www.elastic.co/guide/en/kibana/current/action-types.html) to send alerts to e-mail, webhooks, chats and other options. Consider enabling the [Spike in failed logon events](https://www.elastic.co/guide/en/security/current/spike-in-failed-logon-events.html) rule to alert for excessive failed login attempts. You can also create a [threshold rule](https://www.elastic.co/guide/en/observability/current/metrics-threshold-alert.html) and set it to alert after a fixed amount of failed logins.

:::
