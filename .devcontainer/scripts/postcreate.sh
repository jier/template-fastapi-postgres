poetry update

if [[ ! -f .env ]]; then
    cp {local,}.env
fi

source .env

cd src
poetry run alembic upgrade head
cd ..