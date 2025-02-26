# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Requirements

* uv
* docker
* python version {{cookiecutter.python_full_version}}

#### Docker

Setup requires that you already have docker installed on your machine.

Create .env file `cp .env.dist .env`

Build the image with `docker build -t {{cookiecutter.project_slug}} .`

Run Unit tests with `docker run --name "{{cookiecutter.project_slug}}-container" --entrypoint /app/scripts/build.sh {{cookiecutter.project_slug}}`

## Install Dependencies

`uv sync`

## FrontEnd app execution

Execution of Streamlit app:

`poe run`

In case you need auto-reload, change the following in `./.streamlit/config.toml`:

In section `[server]`
1. set `fileWatcherType = "auto"`
2. set `runOnSave = true`

Or run the streamlit app using `poe dev`

## Databricks Apps deployment

Create the `requirements.txt` using `uv pip compile pyproject.toml -o requirements.txt`   

The `app.yaml` contains the command Databricks executes.

More detail see: 
- https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-apps/app-development
- https://www.databricks.com/product/pricing/compute-for-apps
