# Open Data

## Licensing

Bradford 2025 City of Culture data is released under a 
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).


## Datasets

The Bradford 2025 City of Culture datasets are detailed below.

## Programme

There are two metrics contained in the Programme dataset.

| Metric   | Description                           |
| -------- | ------------------------------------- |
| Event    | Count of individual events            |
| Audience | Count of auddience recorded at events |

Data is available by the following dimensions

| Dimension           | Code | Description                                 |
| ------------------- | :--: | ------------------------------------------- |
| Event type          |  T   | Whether the event was open or closed        |
| Evaluation category |  C   | The category in which the event was counted |
| Project name        |  P   | Name of the project organising the event    |
| Month               |  M   | Month in which the event took place         |

The following aggregations are published.

| Aggregation                    | Code                     |                    File                     |    T    |  C  |    P    |    M    |
| ------------------------------ | ------------------------ | :-----------------------------------------: | :-----: | :-: | :-----: | :-----: |
| Total                          | TOTAL                    |   {{ dataset_link('programme/total.csv') }}    |         |     |         |         |
| By event type                  | BY_EVENT_TYPE            |   {{ dataset_link('programme/total.csv') }}    | &check; |     |         |         |
| By evaluation category         | BY_EVAL_CAT              |   {{ dataset_link('programme/total.csv') }}    |         |  &check;  |         |         |
| Monthly total                  | BY_MONTH                 |  {{ dataset_link('programme/by_month.csv') }}  |         |     |         | &check; |
| Monthly by event type          | BY_MONTH_BY_EVENT_TYPE   |  {{ dataset_link('programme/by_month.csv') }}  | &check; |     |         | &check; |
| Monthly by evaluation category | BY_MONTH_BY_EVAL_CAT     |  {{ dataset_link('programme/by_month.csv') }}  |         |  &check;  |         | &check; |
| By project                     | BY_PROJECT               | {{ dataset_link('programme/by_project.csv') }} |         |     | &check; |         |
| By project by event type       | BY_PROJECT_BY_EVENT_TYPE | {{ dataset_link('programme/by_project.csv') }} | &check; |     | &check; |         |

## Participants

There are two metrics contained in the Programme dataset.

| Metric                | Description                                                      |
| --------------------- | ---------------------------------------------------------------- |
| Participants          | Count of unique participants                                     |
| Participant instances | Count of participants participating during a to two hours period |

Particpant instances are a way of standardising the amount of participation
undertaken. It acknowledges that short and long events are substantively
different.

| Dimension      | Code | Description                                 |
| -------------- | :--: | ------------------------------------------- |
| Variable group |  G   | The category in which the event was counted |
| Project name   |  P   | Name of the project organising the event    |
| Month          |  M   | Month in which the event took place         |

The variable group is used in this case to refine the variable.

- Community programme
- Cultural learning
- Volunteers (individual)
- Corporate Volunteers
- Training and Skills

The following aggregations are published.

| Aggregation                 | Code                         |                   File                   |    G    |    P    |    M    |
| --------------------------- | ---------------------------- | :--------------------------------------: | :-----: | :-----: | :-----: |
| Total                       | TOTAL                        |   {{ dataset_link('participant/total.csv') }}    |         |         |         |
| By participant type         | BY_PARTICIPANT_TYPE          |   {{ dataset_link('participant/total.csv') }}    | &check; |         |         |
| Monthly total               | BY_MONTH                     |  {{ dataset_link('participant/by_month.csv') }}  |         |         | &check; |
| Monthly by participant type | BY_MONTH_BY_PARTICIPANT_TYPE |  {{ dataset_link('participant/by_month.csv') }}  | &check; |         | &check; |
| By project                  | BY_PROJECT                   | {{ dataset_link('participant/by_project.csv') }} |         | &check; |         |

## Audience survey

Audiences had had the opportunity to submit surveys following their attendance
at Bradford 2025 events. There are two key groups of metrics contained in this
dataset: classifying the respondents to the survey and their responess.

| Metric               | Description                                                                     |
| -------------------- | ------------------------------------------------------------------------------- |
| Survey respondents   | Count of survey respondents                                                     |
| Overall satisfaction | Overall satifaction of survey respondents                                       |
| Net promoter score   | Likelihood of recommending a Bradford 2025 City of Culture event o someone else |

The two survey responses were prompted by the following questions:

- **Overall rating**: How would you rate your overall experience of your most
  recent Bradford 2025 UK City of Culture activity/event that you attended?
- **Net promoter score**: On a scale of 0 - 10 how likely or unlikely are you to
  recommend a Bradford 2025 UK City of Culture activity/event to a friend,
  family member or colleague with 10 being extremely likely and 0 being not
  likely at all?

The data is collected by the following dimensions

| Dimension              | Code | Description                                                                |
| ---------------------- | :--: | -------------------------------------------------------------------------- |
| Month                  |  M   | Month the event being covered was held in                                  |
| Bradford ward          |  W   | Bradford Ward of residence the survey respondent                           |

The following aggregations are provided in the data

| Aggregation               | Code        |              File               |    M    |    W    |
| ------------------------- | ----------- | :-----------------------------: | :-----: | :-----: |
| Total                     | TOTAL       | {{ dataset_link('survey/total.csv') }}  |         |         |
| By month                  | BY_MONTH    | {{ dataset_link('survey/total.csv') }}  | &check; |         |
| By Bradford Ward          | BY_WARD     | {{ dataset_link('survey/by_geo.csv') }} |         | &check; |

## Ticketing

Many of the Bradford 2025 City of Culture events were ticketed. While the
audience figures are being tracked elsewhere, there is useful analysis of the
geographic reach, that can be gleaned from the data.

Order data is extracted from the ticketing platform, this includes the lead
booker postcode, from which can be determined the Bradford ward, postcode area
and local authority.

There is only one metric of significant interest: count of tickets sold.

| Metric       | Description           |
| ------------ | --------------------- |
| Tickets sold | Count of tickets sold |

The data is collected by the following dimensions

| Dimension              | Code | Description                                                                |
| ---------------------- | :--: | -------------------------------------------------------------------------- |
| Month                  |  M   | Month the event being covered was held in                                  |
| Ticket type            |  K   | Type of ticket                                                             |
| Bradford ward          |  W   | Bradford Ward of residence the survey respondent                           |
| Bradford postcode area |  A   | Bradford postcode area (i.e. first part of postcode) the survey respondent |
| Local authority        |  L   | UK local authority of residence of the survey respondent                   |

The following aggregations are provided in the data

| Aggregation              | Code     |                File                |    M    |    K    |    W    |    A    |    L    |
| ------------------------ | -------- | :--------------------------------: | :-----: | :-----: | :-----: | :-----: | :-----: |
| Total                    | TOTAL    |  {{ dataset_link('tickets/total.csv') }}   |         |         |         |         |         |
| By ticket type           | BY_TYPE  |  {{ dataset_link('tickets/total.csv') }}   |         | &check; |         |         |         |
| By month                 | BY_MONTH | {{ dataset_link('tickets/by_month.csv') }} | &check; |         |         |         |         |
| By Braford Ward          | BY_WARD  |  {{ dataset_link('tickets/by_geo.csv') }}  |         |         | &check; |         |         |
| By Braford postcode area | BY_AREA  |  {{ dataset_link('tickets/by_geo.csv') }}  |         |         |         | &check; |         |
| By Local Authority       | BY_LA    |  {{ dataset_link('tickets/by_geo.csv') }}  |         |         |         |         | &check; |

## Digital engagement

Statistics have been collected about the digital engagement with Bradford 2025
content (outside the digitally-mediated events).

The metrics include

| Metric        | Description                                                               |
| ------------- | ------------------------------------------------------------------------- |
| Website users | Total users accessing the website                                         |
| Followers     | Followers across various media including mailing lists, and social media. |
