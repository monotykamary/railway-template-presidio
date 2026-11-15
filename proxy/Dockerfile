FROM docker.io/caddy:2.11.9-alpine@sha256:003a97808e781aa9f7e75cc2f43d34d461099031faf5e20faefb9f61126836f0
COPY Caddyfile /etc/caddy/Caddyfile
COPY entrypoint.sh /usr/local/bin/presidio-proxy-entrypoint
RUN chmod +x /usr/local/bin/presidio-proxy-entrypoint \
    && ANALYZER_URL=http://analyzer:3000 ANONYMIZER_URL=http://anonymizer:3000 BASIC_AUTH_USER=test BASIC_AUTH_HASH='$2a$14$JqVwlbq99ETFkVZllxeXVOZH8kgm4YFxeRxB3bFu5AMkUxLG/yA/W' caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/presidio-proxy-entrypoint"]
