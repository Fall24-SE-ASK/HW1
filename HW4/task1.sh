#!/usr/bin/env bash

ps -ef | grep infinite.sh | grep -v grep | gawk '{ print $2 }' | xargs kill -9
