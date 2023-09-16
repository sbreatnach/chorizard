#!/usr/bin/env sh

set -e

# auto-run any migrations
spicedb migrate head

exec spicedb "$@"
