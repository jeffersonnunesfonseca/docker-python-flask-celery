#!/bin/sh
FILE=env_vars.sh
DIR=$CONDA_PREFIX/etc/conda/activate.d/
DIRFILE=$DIR$FILE

if [ -f "$DIRFILE" ]; then
    echo "Remove arquivo atual"
    rm -rf $CONDA_PREFIX/etc/conda
fi

mkdir -p $DIR
touch $DIRFILE

echo "#!/bin/sh" > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
echo export $(cat $(pwd)/.env) > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
echo run: $ conda activate docker-python-flask
