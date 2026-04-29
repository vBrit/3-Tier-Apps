FROM httpd:2.4

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 \
    && rm -rf /var/lib/apt/lists/*

RUN sed -i 's/^Listen 80$/Listen 8080/' /usr/local/apache2/conf/httpd.conf

COPY containers/db/data.py /usr/local/apache2/cgi-bin/data.py
COPY playbooks/roles/db/files/clients.db /opt/db/seed/clients.db
COPY containers/db/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

RUN chmod 755 /usr/local/apache2/cgi-bin/data.py /usr/local/bin/docker-entrypoint.sh

VOLUME ["/var/lib/three-tier-db"]
EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
