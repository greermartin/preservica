# About this repository

Contains a Python script (csv2opex.py) that creates one OPEX file (.opex) per row for a given CSV.
The created .opex files:

1. Include the <opex:sourceID> element required for for bulk ingest of files to Preservica.
2. Include any DC metadata that was in the CSV
3. Output a .opex file for each row using the value in the SourceID column as the filename
