# Datasets

The Bradford 2025 City of Culture datasets are grouped as follows:

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

| Aggregation                    | Code                     | Published? |    T    |    C    |    P    |    M    |
| ------------------------------ | ------------------------ | :--------: | :-----: | :-----: | :-----: | :-----: |
| Total                          | TOTAL                    |            |         |         |         |         |
| By event type                  | BY_EVENT_TYPE            |            | &check; |         |         |         |
| By evaluation category         | BY_EVAL_CAT              |            |         | &check; |         |         |
| Monthly total                  | BY_MONTH                 |            |         |         |         | &check; |
| Monthly by event type          | BY_MONTH_BY_EVENT_TYPE   |            | &check; |         |         | &check; |
| Monthly by evaluation category | BY_MONTH_BY_EVAL_CAT     |            |         | &check; |         | &check; |
| By project                     | BY_PROJECT               |            |         |         | &check; |         |
| By project by event type       | BY_PROJECT_BY_EVENT_TYPE |            | &check; |         | &check; |         |

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

| Aggregation                 | Code                   | Published? |    G    |    P    |    M    |
| --------------------------- | ---------------------- | :--------: | :-----: | :-----: | :-----: |
| Total                       | TOTAL                  |            |         |         |         |
| By participant type         | BY_PARTICIPANT_TYPE    |            | &check; |         |         |
| Monthly total               | BY_MONTH               |            |         |         | &check; |
| Monthly by participant type | BY_MONTH_BY_PARTICIPANT_TYPE |            | &check; |         | &check; |
| By project                  | BY_PROJECT             |            |         | &check; |         |

<!--
## Ticketing

- Sales

## Audience survey

- Results
- Respondents
-->
