FROM docker.io/caddy:2.11.4-alpine@sha256:5f5c8640aae01df9654968d946d8f1a56c497f1dd5c5cda4cf95ab7c14d58648
COPY Caddyfile /etc/caddy/Caddyfile
COPY entrypoint.sh /usr/local/bin/presidio-proxy-entrypoint
RUN chmod +x /usr/local/bin/presidio-proxy-entrypoint \
    && ANALYZER_URL=http://analyzer:3000 ANONYMIZER_URL=http://anonymizer:3000 BASIC_AUTH_USER=test BASIC_AUTH_HASH='$2a$14$JqVwlbq99ETFkVZllxeXVOZH8kgm4YFxeRxB3bFu5AMkUxLG/yA/W' caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/presidio-proxy-entrypoint"]
