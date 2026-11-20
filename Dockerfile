# The website as a Docker image: the same image is tested, stored and deployed.

# Small official Python image, same version as in CI.
FROM python:3.11-slim

# No .pyc files, and logs go straight to the container output.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install the packages first, so this layer is reused when only the code changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collect the static files into the image. The key is a throwaway value,
# only needed so Django can start for this one command.
RUN DJANGO_SECRET_KEY=build-only python manage.py collectstatic --noinput

# Run as a normal user, not as root.
RUN useradd --create-home appuser
USER appuser

EXPOSE 8000

# Gunicorn is the production web server (the same one the live site uses today).
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--access-logfile", "-"]
