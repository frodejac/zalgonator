#!/usr/bin/env bash

set -e

run_webserver() {
    exec gunicorn -c /opt/zalgonator/zalgonator/gunicorn.cfg.py zalgonator.wsgi:app
}

echo Starting Zalgonator with command "$@"

if [[ $# -eq 0 ]]; then
    run_webserver
else
    case "$1" in
        webserver)
            run_webserver
            ;;
        *)
            exec "$@"
    esac
fi

