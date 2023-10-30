poetry update

if [[ ! -f .env ]]; then
    cp {local,}.env
fi

source .env

cd src
alembic upgrade head
cd ..