#!/bin/bash

. ~/develop/config/script_config.txt

HOST=$(hostname)
curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"${1} \n from: ${HOST}\"}\"" https://hooks.slack.com/services/${SLACK_NOTIFICATION}
