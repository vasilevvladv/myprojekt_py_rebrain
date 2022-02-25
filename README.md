### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:vasilevvladv/myprojekt_py_rebrain.git
```

```
cd myprojekt_py_rebrain
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv .venv
```

```
source .venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd config
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
