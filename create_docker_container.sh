docker build . -t django-markdown-docs
# docker run -p 8098:8099 --name django-markdown-docs --network nginxproxymanager_default django-markdown-docs
docker run -p 8098:8099 --name django-markdown-docs django-markdown-docs