#!/bin/bash

set -e
docker-entrypoint.py

if [[ "$@" = "redbot" ]]; then
  redbot "$REDBOT_NAME" --edit --no-prompt --token $REDBOT_TOKEN --prefix $REDBOT_PREFIX
  exec "$@" "$REDBOT_NAME"
else
  exec "$@"
fi
