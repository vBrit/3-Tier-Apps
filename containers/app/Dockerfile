FROM httpd:2.4

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 python3-pip \
    && pip3 install --no-cache-dir requests \
    && rm -rf /var/lib/apt/lists/*

RUN sed -i 's/^Listen 80$/Listen 8080/' /usr/local/apache2/conf/httpd.conf

COPY containers/app/app.py /usr/local/apache2/cgi-bin/app.py
COPY playbooks/roles/app/files/icons/ /usr/local/apache2/htdocs/icons/

RUN chmod 755 /usr/local/apache2/cgi-bin/app.py \
    && find /usr/local/apache2/htdocs/icons -type f -exec chmod 644 {} \;

EXPOSE 8080

CMD ["httpd-foreground"]
