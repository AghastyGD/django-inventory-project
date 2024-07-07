echo "Starting build script"

pip install -r requirements.txt

# make migrations
python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py collectstatic

echo "Build script completed"
