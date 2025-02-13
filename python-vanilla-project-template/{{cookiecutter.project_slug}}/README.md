# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Requirements

* poetry
* docker
* python version {{cookiecutter.python_full_version}}

#### Docker

Setup requires that you already have docker installed on your machine.

Build the image with `docker build -t {{cookiecutter.project_slug}} .`

Run Unit tests with `docker run --name "{{cookiecutter.project_slug}}-container" --entrypoint /app/scripts/build.sh {{cookiecutter.project_slug}}`

## Execution

`poe run`

