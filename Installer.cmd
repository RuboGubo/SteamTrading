cd "..\SteamTrading"

pip --quiet install --user pipenv
pipenv sync

pipenv run jupyter notebook