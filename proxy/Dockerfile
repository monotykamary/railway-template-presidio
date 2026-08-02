FROM docker.io/caddy:2.10.2-alpine@sha256:d8c17a862962def15cde69863a3a463f25a2664942eafd7bdbf050e9c3116b83
COPY Caddyfile /etc/caddy/Caddyfile
COPY entrypoint.sh /usr/local/bin/presidio-proxy-entrypoint
RUN chmod +x /usr/local/bin/presidio-proxy-entrypoint \
    && ANALYZER_URL=http://analyzer:3000 ANONYMIZER_URL=http://anonymizer:3000 BASIC_AUTH_USER=test BASIC_AUTH_HASH='$2a$14$JqVwlbq99ETFkVZllxeXVOZH8kgm4YFxeRxB3bFu5AMkUxLG/yA/W' caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/presidio-proxy-entrypoint"]
