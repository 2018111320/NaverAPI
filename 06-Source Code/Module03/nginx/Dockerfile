FROM nginx:latest

WORKDIR /etc/nginx

COPY default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]

EXPOSE 80
EXPOSE 443
