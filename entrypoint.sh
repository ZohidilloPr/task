# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# fail exit if one of your pipe command fails
set -o pipefail
# exits if any of your variables is not set
set -o nounset
export DJANGO_SETTINGS_MODULE=config.settings.product

echo "Running migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running tests..."
pytest

echo "Starting Gunicorn..."
gunicorn config.wsgi:application --bind 0.0.0.0:8000
