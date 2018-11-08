# eBay Searcher

A flask-based web utility for interfacing with the eBay API.

## Setup

In order to successfully run the application, you must set the `EBAY_APP_NAME` and `EBAY_AUTH_TOKEN` environment variables prior to running the flask application.

The values can be created/configured/accessed via the [eBay developer portal](https://developer.ebay.com/my/auth). Setting the environment variables can be accomplished several ways:

* On a *nix type system, you can run `./run.sh --ebay-app-name=SAMPLE_APP --ebay-auth-token=SAMPLE_AUTH_TOKEN` with your app and auth_token values in place of the sample ones here
* On a *nix type system, you can also use `export EBAY_APP_NAME=SAMPLE_APP` and `export EBAY_AUTH_TOKEN=SAMPLE_AUTH_TOKEN` with your app and auth_token values in place of the sample ones here, then run the flask application contained in app.py manually (e.g. `FLASK_APP=app.py flask run --host=0.0.0.0`)
* On a windows system, you can use `set EBAY_APP_NAME SAMPLE_APP` and `set EBAY_AUTH_TOKEN SAMPLE_AUTH_TOKEN` with your app and auth_token values in place of the sample ones here, then run the flask application contained in app.py manually

Once running, you can access the application at localhost:5000 (depending on your flask configuration)

## Heads Up

This thing is meant as a hobby project and is not intended for third party use. Use at your own risk.
