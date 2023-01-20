#!/bin/bash

ORG=
BUCKET=
TOKEN=

data='temperature,location=kitchen value=24.8'

curl -i -XPOST "https://us-east-1-1.aws.cloud2.influxdata.com/api/v2/write?org=$ORG&bucket=$BUCKET" \
    -H "Authorization: Token $TOKEN" \
    -H 'Content-Type: application/octet-stream' \
    --data-binary "$data"
