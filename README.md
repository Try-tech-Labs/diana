# Diana Project

### About this software

This is a information aggregator system, created to facilitate the way how people read about interesting things on internet.

Diana is basically and acronym to "Daily Information Aggregator Notably Affordable"

Diana's main goal is not to compete with the main news aggregators or RSS (for example), the goal is to be the place where people find more informaion about what people is more searching on internet.

For example, if for some reason a lot of people (100k+) are searching on google for chocolate cake recipies, Diana is where you will get everything about it, videos, news, tweets, books, images, articles, images, podcasts and so.

#

You can access the online project on [DianaWeb](https://diana.trytechlab.com)

#

# Start coding on Diana

This project was bootstrapped with [Django Startproject](https://docs.djangoproject.com/pt-br/3.1/intro/tutorial01/#creating-a-project).

#

## Available Scripts

In the project directory, you have a Makefile with some usefull commands:


### `Build`
This command will create the docker images and containers of the project with all necessarie dependencies to run and test it.
Usage:

```bash
    #On project root
    make build
```

### `Run`
This command will start the app docker container on port 8000.
Usage:

```bash
    #On project root
    make run
```

### `Test`
This command will run pytest for the project, testing all suites on all django apps inside the project root. (The tests will run randomly)
Usage:

```bash
    #On project root
    make test
    
    #To test a specific app or file just add the path after test, like showed bellow
    make test app/news/tests
```

### `Lint`
This command will verify if the project files are following PEP8 formating rules.
Usage:

```bash
    #On project root
    make lint

    #To verify a specific app or file just add the path after lint, like showed bellow
    make lint app/news/tests
```

### `Format`
This command will format the project files, following PEP8 rules.
Usage:

```bash
    #On project root
    make format

    #To format files from a specific app or a specific file just add the path after format, like showed bellow
    make format app/news/tests/test_example.py
```

### `Create database (Comming soon)`
This command will create the tables and columns (blank) of the project on the database container.
Usage:

```bash
    #On project root
    make create_database
```


### `Create database from sample (Future)`
This command will create the tables and columns of the project, with sample data populated on the database container.
Usage:

```bash
    #On project root
    make create_database_from_sample
```