#!/usr/bin/env sh
set -eu

mkdir -p /var/lib/three-tier-db
if [ ! -f /var/lib/three-tier-db/clients.db ]; then
  cp /opt/db/seed/clients.db /var/lib/three-tier-db/clients.db
fi

exec httpd-foreground
