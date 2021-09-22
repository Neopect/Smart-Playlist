FROM php:7.4-cli

RUN apt-get update && apt-get install -y \
        git \
        zip unzip \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) gd

COPY ./myapp/ /usr/src/myapp/web
WORKDIR /usr/src/myapp/

COPY ./composer.sh ./
RUN ./composer.sh
RUN mv composer.phar /usr/local/bin/composer

WORKDIR /usr/src/myapp/web

RUN composer require jwilsson/spotify-web-api-php

CMD [ "php", "./your-script.php" ]