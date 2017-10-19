FROM 3blades/core-server:build-112 AS core
FROM rocker/rstudio:3.4.1

EXPOSE 8080
RUN echo "www-port=8888" > /etc/rstudio/rserver.conf
RUN echo "session-default-working-dir=/resources" > /etc/rstudio/rsession.conf
WORKDIR /resources

# move copy to end to avoid cache busting
COPY --from=core runner /runner
