FROM python:3.8.3
ARG ENV DEBIAN_FRONTEND noninteractive
# FROM ubuntu:22.04 as base
# # Set environment variables
# ARG PYTHON_VERSION=3.8

WORKDIR /app
COPY . /app

ENV ACCEPT_EULA=Y
RUN apt-get update -y && apt-get update \
  && apt-get install -y --no-install-recommends curl gcc g++ gnupg unixodbc-dev

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
  && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
  && apt-get update \
  && apt-get install -y --no-install-recommends --allow-unauthenticated msodbcsql17 mssql-tools \
  && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile \
  && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

RUN apt-get -y clean

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3-pip \
        build-essential \
        wget \
        git \
        unzip \
        gnupg2 \
        apt-utils \
        && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt
RUN apt update
RUN apt -y upgrade

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

RUN wget https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.72/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    rm chromedriver-linux64.zip

RUN cd ./chromedriver-linux64 && \
    chmod +x chromedriver && \
    mv -f chromedriver /usr/local/share/chromedriver && \
    ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver && \
    ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

# RUN chmod +x /app/*
# RUN chmod +x /app/*.py
# RUN chmod +x /app/*.json
# RUN apt update

# # CMD /bin/bash -c "/app/odbcInstaller.sh && python3 app.py"
# # CMD [ "/odbcInstaller.sh" ]
CMD [ "python3 app.py" ]
