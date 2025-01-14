from setuptools import setup, find_packages

setup(
    name="owntrack2gpx",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[
        "gpx==0.2.1",
        "gpxpy==1.5.0",
    ],
    entry_points={
        "console_scripts": [
            "owntrack2gpx=convert",
        ],
    },
    long_description="OwnTrack have its own tool ocat but with it you loose"
    "some data like battery and speed data. For this reason you should export data to"
    "json and then use this tool to convert to gpx.",
)
