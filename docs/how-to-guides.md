## Daily checks

The pipeline run daily in GitHub. It's worth checking in periodically.

1. Visit the [Data Pipeline actions page](https://github.com/bradford-2025/open-data-pipelines/actions/workflows/data-pipeline.yml). This shows the individual runs of the pipeline jobs.
2. Check that the tick next to the latest run is a green tick. If the job has failed for any reason, it will show a red cross.
3. Open the most recent workflow run by clicking the text Data Pipeline (which is a link).
4. Check that the build summary has `0` in the **Status** column.

If you need to explore further because of some failures, you can click on the **build** job block in the pipeline overview. This will open the logs for that job. These should generally be all ticks, but in the event something has gone wrong, error messages will be shown describing the problem. - typically this will be in the **Run DVC pipelines** step.

## Local development

### One-time setup

1. [Setup credentials](#setup-credentials)
2. [Setup Python and uv](#setup-python-and-uv)

#### Setup credentials

TODO Complete this section

You will need to set up some environment variables to connect to the various source systems.
These should be stored in a file named `.env` in the respository root, and contain the following records.
Activating the `pipenv` shell should make these available (tested in macos and Linux).
The values for these environment variables are available on request.

```ini
# SFTP Server
SFTP_HOSTNAME=<SFTP hostname>
SFTP_USERNAME=<SFTP username>
SFTP_PASSWORD=<SFTP password>
SFTP_ROOTPATH=<Absolute path to directory on SFTP server>
```

#### Setup Python and uv

The pipelines are written using Python.

Make sure you have Python (ideally version 3.12, although uv will resolve the correct version if not available) installed on your system.
You can find [Python downloads and install instructions](https://www.python.org/downloads/) on the Python website.

We're using [uv](https://docs.astral.sh/uv/) to manage the dependencies and virtual environments.

 you can install **uv**
by running

```sh
pipx install uv
```

We have set up a series of environment variables in the `.env` file, which it would be useful to auto-load.
You can do this by setting the `UV_ENV_FILE` environment variable in the current shell.
Assuming you're running in `bash`, appending this to your `~/.bashrc` file will make this happen for future
shells.

```sh
export UV_ENV_FILE=.env
```

Once this is done, run `uv sync` to install the required packages.

<!-- 
#### Setup Pipenv

The pipelines are written using Python.
We're using [Pipenv](https://pipenv-searchable.readthedocs.io/) to manage the dependencies and virtual environments.
Follow the appropriate instructions to set this up for your system.

If you're running Windows, it's strongly recommended to run inside WSL (Windows System for Linux).

Once this is installed, run `pipenv sync` to install the required packages.
-->

### Running pipelines

To run the pipelines locally, you will need to ensure that uv knows to read the `.env` file.
You can do this by setting the `UV_ENV_FILE` environment variable in the current shell.
Assuming you're running in `bash` running this command will do the job

```sh
export UV_ENV_FILE=.env
```

You might want to put this in your `~/.bashrc` file, as suggested in the setup section.

follow the steps below:

1. Run the following commands to update the data.  
    ```sh
    git pull --rebase
    uv run dvc pull
    ```
2. Run the full pipeline (warning this might pull fresh data, and could take several minutes to run!)
    ```sh
    uv run dvc repro --pull pipelines/dvc.yaml
    ```
    This has also been bundled into a single tasks
    ```sh
    uv run task pipelies
    ```
3. To run a specific stage (e.g. `combine`)
    ```sh
    uv run dvc repro --single-item --pull pipelines/dvc.yaml:combine
    ```
    This won't execute if none of the dependencies have changes. You can include the `--force` flag alongside to force the pipeline to run.

Once you have completed your local run, assuming you want to keep the changes, make sure you commit the changes to git then run the following command to update the cache.

```sh
uv run dvc push
```

## Running github workflows locally

Install `act`

```
gh extension install act
```

```sh
gh act --platform ghcr.io/catthehacker/ubuntu:act-latest  --pull=false --workflows .github/workflows/update-docs.yml workflow_dispatch
```

https://hub.docker.com/r/nektos/act-environments-ubuntu/tags