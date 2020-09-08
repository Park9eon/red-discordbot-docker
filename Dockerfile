FROM python:3.8.5-buster

RUN apt-get update \
    && apt-get install -y \
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncurses5-dev \
    xz-utils \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libffi-dev \
    liblzma-dev \
    libgdbm-dev \
    uuid-dev \
    python3-openssl \
    git \
    openjdk-11-jre-headless \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install -U pip setuptools wheel \
    && python -m pip install -U Red-DiscordBot[postgres]

ENV XDG_DATA_HOME /data

ENV XDG_CONFIG_HOME /etc/redbot

RUN mkdir -p ${XDG_DATA_HOME} \
    && mkdir -p ${XDG_CONFIG_HOME}

VOLUME ["${XDG_DATA_HOME}"]

COPY docker-entrypoint.* /usr/local/bin/

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["redbot"]
