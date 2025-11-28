Data is extracted from _operational systems_ such as **Rosterfy**, **Airtable** and **Spektrix**.
The pipelines documented here are responsible for

* extracting the data from the source systems
* cleansing the data &mdash; filling in missing data and converting dates, etc
* summarising and anonymising to ensure no sensitive information (e.g. personal data) is made public
* combining multiple datasets into aggredate sets
* creating output files

This flow is shown schematically in the diagram below

```mermaid
graph LR
    airtable[Airtable]
    google_analytics[Google Analytics]
    rosterfy[Rosterfy]
    spektrix[Spektrix]
    manual_files[Manual files]

    pipeline[/Data processing
    pipelines/]

    class pipeline pink;

    processed_data@{ shape: docs, label: "Processed
    data files"}

    class processed_data green;

    airtable --> pipeline
    google_analytics --> pipeline
    rosterfy --> pipeline
    spektrix --> pipeline
    manual_files --> pipeline
    pipeline --> processed_data

    classDef yellow,default fill:#e0b942;
    classDef green fill:#45d108;
    classDef pink fill:#f4accd;
```

The pipelines extract data from the following operational systems

* **Airtable**
    * Programme data (_projects_, _schedule_ and _venues_)
    * Sustainability data (_carbon impact_ per project)
* **Google Analytics**
    * Website traffic
* **Rosterfy**
    * Volunteers
    * Shifts
* **Spektrix**
    * Ticket sales
* **Manual files**
    * Events / schedule

There are also pipelines which

* match data across systems (e.g. Airtable and Spektrix events)
* combine event data from multiple systems.

The pipelines run overnight at 03:25 UTC (3:25 AM GMT / 4:25 AM BST).

## Pipeline stages

Pipeline stages are defined in Jupyter notebooks, allowing code and documentation to be mixed.
[Pipeline documentation](pipelines.md) can be found elsewhere in this documentation site.

Stages are orchestrated by `dvc`, which determines the correct order
to execute the stages. The following is a view of the dependencies between stages.

```mermaid
{%
    include "../upstream/dag-stages.mermaid"
%}

        classDef yellow fill:#e0b942;
        classDef green fill:#45d108;
        classDef pink,default fill:#f4accd;
```
