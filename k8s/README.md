# Three-Tier App on Tanzu

This directory contains Kubernetes manifests for running the existing 3-tier app on Tanzu.

## Components

- `three-tier-db`: Apache + CGI endpoint (`/cgi-bin/data.py`) backed by SQLite on a PVC.
- `three-tier-app`: Apache + CGI endpoint (`/cgi-bin/app.py`) that calls DB service.
- `three-tier-web`: NGINX edge service that proxies `/` to app CGI endpoint.
- `Ingress`: External entrypoint to `three-tier-web`.

## 1. Build and push images

Run from repository root:

```bash
docker build -f containers/db/Dockerfile -t <registry>/three-tier-db:<tag> .
docker build -f containers/app/Dockerfile -t <registry>/three-tier-app:<tag> .
docker build -f containers/web/Dockerfile -t <registry>/three-tier-web:<tag> .

docker push <registry>/three-tier-db:<tag>
docker push <registry>/three-tier-app:<tag>
docker push <registry>/three-tier-web:<tag>
```

## 2. Update manifest image references

Edit these files and replace image placeholders:

- `k8s/base/db.yaml`
- `k8s/base/app.yaml`
- `k8s/base/web.yaml`

## 3. Set ingress hostname

Update host in `k8s/base/ingress.yaml`:

- `three-tier.wei-lab.com` -> your DNS name in Tanzu.

Also adjust ingress class annotation if your cluster does not use Contour.

## 4. Deploy

```bash
kubectl apply -k k8s/base
kubectl get pods,svc,ing -n three-tier-app
```

## Notes

- The DB pod copies `clients.db` seed data into the PVC at startup only if the DB file is missing.
- Existing VM-based Ansible deployment remains unchanged; this is an additive container path.
