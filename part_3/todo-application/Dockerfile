ARG PYTHON_VERSION=3.11.6


FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#ENV FLASK_RUN_PORT=5000
#ENV FLASK_RUN_HOST="0.0.0.0"
#ENV APP_SETTINGS="config.DevelopmentConfig"

WORKDIR /app

# Create non-root user
# ARG UID=10001

# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#    --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser
# RUN chown -R appuser:appuser .
# Install the dependencies
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

#USER appuser

COPY . .

EXPOSE ${FLASK_RUN_PORT}

CMD ["flask", "run"]
# Run the application using Gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "hello:app"]