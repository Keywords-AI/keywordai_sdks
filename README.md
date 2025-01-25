<p align="center">
<a href="https://www.keywordsai.co">
<img width="800" src="https://keywordsai-static.s3.us-east-1.amazonaws.com/social_media_images/logo-header.jpg">
</a>
</p>
<p align="center">
  <p align="center">Observability, prompt management, and evals for LLM engineering teams.</p>
</p>

# Keywords AI

Observability, prompt management, and evals for LLM engineering teams.

## Keywords AI Tracing

### What for?
Perform telemetry in LLM applications in [OpenLLMetry](https://github.com/traceloop/openllmetry) format.

### Installation
Using pip:
```
pip install keywordsai-tracing
```
Using poetry:
```
poetry add keywordsai-tracing
```
### Getting started
```python
import os
from keywordsai_tracing.main import KeywordsAITelemetry

os.environ["KEYWORDSAI_BASE_URL"] = "https://api.keywordsai.co/api" # This is also the default value if not explicitly set
os.environ["KEYWORDSAI_API_KEY"] = "YOUR_KEYWORDSAI_API_KEY"
k_tl = KeywordsAITelemetry()
```
That's it! You can now trace your LLM applications using the decorators.
With the instance:
```python
from keywordsai_tracing.decorators import workflow, task

@workflow(name="my_workflow")
def my_workflow():
    @task(name="my_task")
    def my_task():
        pass
    my_task()
```
For a comprehensive example, see the [trace example run](https://github.com/Keywords-AI/keywordsai_sdks/blob/main/python-sdks/keywordsai-tracing/tests/tracing_tests/basic_workflow_test.py).

Guide for recreating the example step by step can be found [here](https://github.com/Keywords-AI/keywordsai_sdks/blob/main/python-sdks/keywordsai-tracing/README.md).

## Keywords AI SDK
### What for?
This is a lightweight package used for defining the types used in Keywords AI and conversions between them.

It:
- Is a dependency of Keywords AI server and other Keywords AI python SDKs
- Defines pydantic models
- Defines conversion functions between different Input/Output formats (e.g. OpenAI->Anthropic)
- Accept external PRs that add new types

It does not:
- Provide APIs for interacting with Keywords AI server
- Accept external PRs that alters the `_internal_types.py` file.

### Installation

Using pip:
```
pip install keywordsai-sdk
```
Using poetry:
```
poetry add keywordsai-sdk
```

