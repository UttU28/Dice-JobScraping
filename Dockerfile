FROM ubuntu:22.04 as base
# Set environment variables
ARG PYTHON_VERSION=3.8
# Set the working directory
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Update and install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3-pip \
        build-essential \
        curl \
        wget \
        git \
        unzip \
        gnupg2 \
        openjdk-8-jdk \
        unixodbc-dev \
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

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated msodbcsql17
RUN ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

RUN chmod +x /app/*
RUN chmod +x /app/*.py
RUN chmod +x /app/*.json
RUN apt update

# CMD /bin/bash -c "/app/odbcInstaller.sh && python3 app.py"
# CMD [ "/odbcInstaller.sh" ]
CMD [ "ls -l", "python3 app.py" ]
