#!/bin/bash
# Needs the package jq
AUTH=`cat ~/.homeassistant/.spotify-token-cache | jq -r '.access_token'`
echo "Using access_token:"
echo $AUTH
A='curl -X PUT "https://api.spotify.com/v1/me/player/shuffle?state=true" -H "Accept: application/json" -H "Authorization: Bearer '
C=${A}${AUTH}\"

eval $C