#!/usr/bin/env bash
# Runs on the server: starts one image as a container and replaces the older container with the same name.
# Usage: scripts/deploy.sh <image> <container-name> <port>
# Example: scripts/deploy.sh ghcr.io/samkian0007/portfolio-cicd:<commit> portfolio-staging 8002
set -euo pipefail

IMAGE="${1:?give the image}"
NAME="${2:?give the container name}"
PORT="${3:?give the port}"

docker pull "$IMAGE"

# Replace the running container. The settings (secret key, domain) come from a file
# that only exists on the server, so they never appear in the code or the pipeline.
docker rm -f "$NAME" >/dev/null 2>&1 || true
docker run -d --name "$NAME" --restart unless-stopped \
  --env-file /etc/portfolio/production.env \
  -p "127.0.0.1:$PORT:8000" \
  "$IMAGE"

# Remove images that no container uses and that are older than a week, so the disk does not fill up.
# Every version stays in the registry and can be pulled again.
docker image prune -a -f --filter "until=168h" >/dev/null
echo "Started $NAME from $IMAGE on port $PORT"
