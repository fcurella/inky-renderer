An API service to show images on an [InkyPHAT](https://www.adafruit.com/product/3934).

## Installation

```
sudo raspi-config
```

Under "interfaces", enable SPI.

```
mkdir Envs
python3 -m venv ~/Envs/inky-renderer
source ~/Envs/inky-renderer/bin/activate

mkdir Code
cd Code
git clone ...
cd inky-renderer
pip install -r requirements.txt
export DJANGO_SECRET_KEY=supersecret
./manage.py migrate
./manage.py runserver 0.0.0.0:8000
```

