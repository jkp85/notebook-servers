FROM 3blades/core-server AS core
FROM rocker/rstudio

EXPOSE 8080
COPY --from=core runner /runner
RUN echo "www-port=8888" > /etc/rstudio/rserver.conf
RUN echo "session-default-working-dir=/resources" > /etc/rstudio/rsession.conf
