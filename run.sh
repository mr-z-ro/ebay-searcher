#!/bin/sh

function usage()
{
    echo "Run the Ebay API Integration flask app"
    echo ""
    echo "./run.sh"
    echo "\t-h --help"
    echo "\t--ebay-app-name=SAMPLE_APP"
    echo "\t--ebay-auth-token=SAMPLE_AUTH_TOKEN"
    echo ""
}

while [ "$1" != "" ]; do
    PARAM=`echo $1 | awk -F= '{print $1}'`
    VALUE=`echo $1 | awk -F= '{print $2}'`
    case $PARAM in
        -h | --help)
            usage
            exit
            ;;
        --ebay-app-name)
            EBAY_APP_NAME=$VALUE
            ;;
        --ebay-auth-token)
            EBAY_AUTH_TOKEN=$VALUE
            ;;
        *)
            echo "ERROR: unknown parameter \"$PARAM\""
            usage
            exit 1
            ;;
    esac
    shift
done

if [ "$EBAY_APP_NAME" == "" ]; then
    echo "Please set EBAY_APP_NAME environment variable, e.g. using the --ebay-app-name flag. Register your app name via https://developer.ebay.com/my/keys"
    exit 1
fi
if [ "$EBAY_AUTH_TOKEN" == "" ]; then
    echo "Please set EBAY_AUTH_TOKEN environment variable, e.g. using the --ebay-auth-token flag. Refresh your auth token via https://developer.ebay.com/my/auth"
    exit 1
fi

export EBAY_APP_NAME=$EBAY_APP_NAME
export EBAY_AUTH_TOKEN=$EBAY_AUTH_TOKEN

FLASK_APP=app.py FLASK_DEBUG=1 python -m flask run --host=0.0.0.0
