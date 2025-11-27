# Open data publishing

This document outlines the process that will be followed for each new open
data release.
The purpose of having such a process is to ensure that data is released
safely, and that risks to the Bradford 2025 organisation are contained.

## Process overview

1.  Identify key contacts for data that are to be released.
    This should include at least:
    *   Owners &mdash; people who are responsible for the data - probably
        'director of' or 'head of' role
    *   Managers &mdash; people working closely with the data and most able
        to answer questions about the structure and meaning of the data
2.  Document the data release pipeline.
    This should describe:
    *   The dataset or datasets which are to be released as part of this process.
    *   A description of the data processing which will be performed.
    *   For each dataset identified above, be sure to document:
        *   The key dimensions and facts contained in the dataset as extracted
            from the source system.
            Dimensions are typically discrete / countable categories by which
            the dataset might be reasonably summarised.
            Facts are typically numerical data which it makes sense to sum,
            average, or perform other categorical calculations on.
            It could be that the dataset as extracted is entirely dimensional,
            in which case the facts are simply derived through summarisation.
        *   Note which, if any, of the dimensions or facts are potentially
            sensitive from a personal or commercial nature.
            This data may be covered by a data sharing agreement or by data
            privacy regulation.
        *   Any special processing to handle data, particularly if this data
            is sensitive in nature.
    *   The files created, including any handling of data masking such as removing
        values below a given level or other statistical fuzzing.
    *   A set of technical risks and mitigations specific to this dataset.
3.  Review the risks for all datasets against the corporate risk register.
    This has two purposes:
    *   To identify any new corporate risks based on the current publication.
    *   To align the new release with existing risks and controls in place.
4.  (TO BE COMPLETED) Gain approvals from the following people:
    *   Data owner
    *   Head of evaluation
    *   Directors?
    *   Board? Delegated to???
    *   ...
5.  (TO BE COMPLETED) Lodge the complete approvals somewhere...???

## Licensing

Data released by Bradford 2025 will be released under an appropriate
license. This article covering
[guidance on licensing, published by the Open Data Institute](https://theodi.org/insights/guides/publishers-guide-to-open-data-licensing/)
is an excellent starting point in selecting a license.

Broadly, their recommendation is to use a
[Creative Commons license](https://creativecommons.org/) when publishing
data. The UK Open Government License (OGL) is a broadly used alternative
for the UK Public Sector.

For the moment, it's assumed that we'll use a
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
to cover the data releases.
