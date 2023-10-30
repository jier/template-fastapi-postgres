poetry update

if [[ ! -f .env ]]; then
    cp {local,}.env
fi