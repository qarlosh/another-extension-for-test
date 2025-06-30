FROM cloudblueconnect/connect-extension-runner:31.0

COPY pyproject.toml poetry.* package*.json /extension/
WORKDIR /extension
RUN poetry update && poetry install --no-root
RUN if [ -f "/extension/package.json" ]; then npm install; fi
