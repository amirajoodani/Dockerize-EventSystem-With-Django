FROM nginx:1.15
LABEL MAINTAINER="AMIRAJOODANI | https://nextsysadmin.ir"

COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]