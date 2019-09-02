#!/bin/bash

if [ ! $(~/.nix-profile/bin/nix-env -q ${1}) ]; then
    ~/.nix-profile/bin/nix-env -i ${1}
fi
