#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

ansible-playbook -i localhost, "$ROOT_DIR/playbooks/render_inventory.yml"
ansible-playbook -i "$ROOT_DIR/inventories/production/inventory.yml" "$ROOT_DIR/deploy.yml" "$@"
