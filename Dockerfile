# Use Python 3.8 as base image
FROM python:3.8

# Set working directory inside the container
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . /app

# Install curl and gnupg for package management
RUN apt-get update && \
    apt-get install -y \
    curl \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Check Ubuntu version and exit if not supported
RUN if ! [[ "18.04 20.04 22.04 23.04" == *"$(lsb_release -rs)"* ]]; then \
        echo "Ubuntu $(lsb_release -rs) is not currently supported."; \
        exit 1; \
    fi

# Install Microsoft GPG key
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Install Microsoft SQL Server repository configuration
RUN curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | \
    tee /etc/apt/sources.list.d/mssql-release.list

# Update apt-get and install MS SQL Server tools and dependencies
RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y \
    msodbcsql18 \
    mssql-tools18 \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Add mssql-tools to PATH
RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc

# Source .bashrc to apply PATH changes
RUN /bin/bash -c "source ~/.bashrc"

# Set the entry point for the container to run your Python application
CMD ["python3", "app.py"]
