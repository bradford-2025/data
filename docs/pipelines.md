# Pipelines

Pipeline stages are defined in Jupyter notebooks, allowing code and documentation to be mixed.

## Operational systems

### Airtable

* [Programme](pipelines/programme.ipynb)
* [Cultural Learning](pipelines/cultural-learning.ipynb)
* [Digital followers](pipelines/digital-followers.ipynb)
* [Sustainability](pipelines/sustainability.ipynb)

### Spektrix

* [Ticketing](pipelines/ticketing.ipynb)

### Spreadsheets / manual

* [Audience Survey](pipelines/audience-survey.ipynb)
* [Manual data](pipelines/manual_data_feeds.ipynb)

### Rosterfy

* [Volunteering - people](pipelines/volunteer-people.ipynb)
* [Volunteering - shifts](pipelines/volunteer-shift.ipynb)

### Google Analytics

* [Digital audience](pipelines/digital-audience.ipynb)
* [Digital events](pipelines/digital-events.ipynb)

## Preparation and Publishing

* [Combine programme data](pipelines/combine.ipynb)
* [Open Data Publishing pipelines](pipelines/combine.ipynb)  
    Create publishable version of the data.
    The planned [open data schema](datasets/index.md) will be published with the evaluation report.

## Utilities

* [Status](pipelines/status.ipynb)  
    Check status of remote files
* [Catalogue](pipelines/catalogue.ipynb)  
    Download and store schema of source systems &mdash; useful for troubleshooting

## Orchestration

Stages are orchestrated by [**DVC**](https://dvc.org/), which determines the correct order
to execute the stages. The following is a view of the dependencies between stages, showing the
stage definitions.

```mermaid
{%
    include "../upstream/dag-stages.mermaid"
%}

        classDef yellow fill:#e0b942;
        classDef green fill:#45d108;
        classDef pink,default fill:#f4accd;
```

DVC works by defining the dependencies and outputs for each stage, and ensuring that stages 
producing files are "upstream" of stages consuming these files.

This is a view of the flow of files across each stage.

```mermaid
{%
    include "../upstream/dag-outs.mermaid"
%}

        classDef yellow,default fill:#e0b942;
        classDef green fill:#45d108;
        classDef pink fill:#f4accd;
```

### Triggering the pipelines

The first stage in the dependency graph is responsible for storing today's date.
This is set to always run, and all systems pulling from operational systems are 
set to depend on that file. This means, that under normal circumstances, the whole
pipeline will only run once per day.
