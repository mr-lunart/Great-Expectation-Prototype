# Great Expectation Prototype

Great Expectations (GX) operates through a Data Context, the central entry point for managing configurations and metadata. Most components must be registered within this context to function.

The standard workflow follows a structured hierarchy:
1. Data Source: Connects GX to your infrastructure (e.g., PostgreSQL, S3, or Spark).
2. Data Asset: Specifies the specific table or file within that source.
3. Batch Definition: Defines how data is sliced or sampled for testing.

Validation & Automation

Once the data is linked, you can define and automate quality checks:
- Expectation Suite: A collection of verifiable assertions (rules) about your data.
- Validation Definition: Links a specific Batch of data to an Expectation Suite.
- Checkpoint: Orchestrates the validation process and triggers Actions, such as sending Slack alerts or updating Data Docs.

To run this project :
1. Prepare venv with python3:11
2. Install requirements package
3. run prototype.py

## Install PIP Requirements
Install python package dependences
```bash
pip install -R requirements.txt
```

