#!/usr/bin/env bash

if [[ -z "$@" ]]; then
    echo "ERROR: No users specified"
fi

## Set vars
script_path="$(pwd)"
now="$(date +%Y%m%d-%H%M%S)"

## Get list of repositories
for line in $(python listRepos.py "$@"); do

    ## Set some variables
    user=$(echo ${line} | awk -F ';' '{ print $1 }')
    name=$(echo ${line} | awk -F ';' '{ print $2 }')
    repo=$(echo ${line} | awk -F ';' '{ print $3 }')

    ## Set the bundle path
    bundle_path="${script_path}/bundles/${user}/${now}"

    ## Create bundle path if not present
    if [[ ! -d "${bundle_path}" ]]; then
        mkdir -pv ${bundle_path}
    fi

    ## Set the temp path
    repo_path="/tmp/repos/${user}/${name}"

    ## Remove repo if it already exists
    if [[ -d "${repo_path}" ]]; then
        rm -rfv ${repo_path}
    fi

    ## Clone the repo and cd into it
    git clone --mirror ${repo} ${repo_path} && cd ${repo_path}

    ## Create git bundle
    git bundle create ${bundle_path}/${name}.bundle --all

done
