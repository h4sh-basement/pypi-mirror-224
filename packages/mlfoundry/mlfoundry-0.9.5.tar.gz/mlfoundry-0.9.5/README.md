# MlFoundry

![](https://github.com/MyName/my-project/workflows/Project%20Tests/badge.svg)

This guide is to give an idea of how you can log metrics, paramaters, predictions, models, dataset using MlFoundry. MlFoundry supports logging above mentioned logs to S3 asynchronously.

## API Workflow:

Using mlfoundry you ca create multiple projects and each projects can have multiple run.

**Example**

1. Project 1
   - run 1
   - run 2
2. Project 2
   - run 1
   - run 2
   - run 3
   - run 4

Each run under each project will have a unique run_id.

## Quickstart

### 1. Install mlfoundry

```
# Install via pip
pip install mlfoundry --extra-index-url https://api.packagr.app/public
```

### 2. Setup AWS credentials

To setup AWS credentials MlLogs_foundry's CLI can be used. AWS credentials are required to store the artifacts like model, dataset, whylogs_metrics etc in S3 Bucket.

The CLI requires AWS credentials(SECRET_ACCESS_KEY, ACCESS_KEY_ID)

All the credentials can be set by running:

`mlfoundry init`

### 3. Initialise mlfoundry

Create an project and use the project_name to create a run:

```python
 import mlfoundry as mlf

 # create a run
 mlf_run = mlf.create_run(project_name=<project-name>)
```

If you want to use a previously created run:

```python
# printing all the runs available and get the run_id
show_all_runs()

run = get_run(run_id=<run_id>)
```

### 4. Start logging

**To log a model:**

```python
run.log_model(sklearn_model, framework=mlf.ModelFramework.SKLEARN)
```

**To log parameters:**

```python
run.log_params({'learning_rate':0.01,
                  'n_epochs:10'
                  })
```

**To log metrics:**

```python
run.log_metrics({'accuracy':87,
                  'f1_score':0.84,
                  })
```

**Log predictions synchronously:**

feature_df: a pd.DataFrame, the input given to the model to make predictions

predictions: must be a list or pd.Series

To log predictions synchronously:

```python
run.log_predictions(self, feature_df, predictions)
```

To log predictions asynchronously:

```python
responses = run.log_predictions_async(self, feature_df, predictions)

#### To confirm that the log request completed successfully, await for futures to resolve: This is a blocking call
import concurrent.futures as cf
for response in cf.as_completed(responses):
  res = response.result()
```

Users can additionaly pass in feature_names argument which is a list of feture names for feature_df.

# To release as Python package

Use Github Releases to create a tag on main and release it. This will trigger the workflow and publish the pip package

Tags must be of format `vx.x.x`, example `v0.1.0`

# Development instructions

```
git clone https://github.com/truefoundry/mlfoundry.git
cd mlfoundry
virtualenv venv
source venv/bin/activate
pip install poetry==1.4.2
poetry install
pre-commit install
```

# Run Manual QA
```
git clone https://github.com/truefoundry/mlf-test
cd mlf-test
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cd mlf_examples
python main.py  In-this-step-check-for-error-logs
mlfoundry ui  In-this-step-go-to-the-listed-url-and-play-around-with-the-ui
```
