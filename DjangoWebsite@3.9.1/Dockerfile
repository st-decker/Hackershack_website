FROM python:3.9-slim as production

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

# make sure postgres is installed on docker image, necessary dependencies
RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essential \
    gcc \
    libffi-dev \
    musl-dev \ 
    openssl \
    postgresql \
    libpq-dev

# Have image but not files from local machine. Below: left copies from local system into right
COPY requirements/prod.txt ./requirements/prod.txt

# Install dependencies into Docker image
RUN pip install -r ./requirements/prod.txt

COPY manage.py ./manage.py
COPY setup.cfg ./setup.cfg
COPY stevend_website ./stevend_website
# could copy everything in local directory with COPY . .    dont right now because it is bloat

#Expose port that this is running on
EXPOSE 8000

# Tag

# Development
FROM production as development

COPY requirements/dev.txt ./requirements/dev.txt
RUN pip install -r ./requirements/dev.txt

# Copy everything
COPY . . 