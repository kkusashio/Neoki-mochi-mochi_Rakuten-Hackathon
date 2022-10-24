# ねおきもちもち
#楽天夏の陣ハッカソン(全体準優勝)

## Requirements
- docker-compose
- make

## Installation
```
make build
```

## Pipenv

```shell
make backend-shell
pipenv shell
pipenv install package-name
exit
```


## Appの作り方
```
make backend-shell
pipenv shell
python manage.py startapp {applicationname(-,_とか含めると後々めんどそう)}
```

## Frontendが動かなかった時の対処法

1. `docker-compose.development.yml`の38行目を一旦コメントアウト
1. `make up`
1. `make fromtend-shell`
1. `yarn install`
1. `yarn serve`
