# based on: https://github.com/GoogleCloudPlatform/python-runtime#kubernetes-engine--other-docker-hosts
FROM python:3.11

WORKDIR /app

ENV GOOGLE_CLOUD_PROJECT=phonic-command-379501

# install python libraries with poetry
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-root --without dev-dependencies

# Add the application source code.
COPY chat-bot.py /app/

CMD ["streamlit", "run","chat-bot.py","--server.port","8080"]