# hiway

Heavy vehicle route planning

## Installation

Install Python 3, and GDAL with brew:

```
brew install python@3.9
brew install gdal
```

Create a virtual environment, activate it and install the Python dependencies:

```
python3 -m venv venv
. venv/bin/activate
python3 -m pip install -r requirements.txt
```

Sign up for a [Mapbox](https://mapbox.com) developer account and copy your public access token.

## Usage

Make sure you've activated the virtual environment, then run `streamlit run app.py` with the Mapbox token exported into you environment.

```
. venv/bin/activate
MAPBOX_TOKEN=<YOUR-MAPBOX-TOKEN> streamlit run app.py
```
