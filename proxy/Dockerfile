FROM docker.io/caddy:2.11.7-alpine@sha256:d8542f48d34a9cf4e4c11a478865229840e87e4c96ea3f439101f31a5d35f75f
COPY Caddyfile /etc/caddy/Caddyfile
COPY entrypoint.sh /usr/local/bin/presidio-proxy-entrypoint
RUN chmod +x /usr/local/bin/presidio-proxy-entrypoint \
    && ANALYZER_URL=http://analyzer:3000 ANONYMIZER_URL=http://anonymizer:3000 BASIC_AUTH_USER=test BASIC_AUTH_HASH='$2a$14$JqVwlbq99ETFkVZllxeXVOZH8kgm4YFxeRxB3bFu5AMkUxLG/yA/W' caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/presidio-proxy-entrypoint"]
