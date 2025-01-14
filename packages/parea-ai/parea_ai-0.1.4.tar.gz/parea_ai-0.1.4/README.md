# parea-sdk

<div align="center">

[![Build status](https://github.com/parea-ai/parea-sdk/workflows/build/badge.svg?branch=master&event=push)](https://github.com/parea-ai/parea-sdk/actions?query=workflow%3Abuild)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/parea-ai/parea-sdk/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/parea-ai/parea-sdk/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/parea-ai/parea-sdk/releases)
[![License](https://img.shields.io/github/license/parea-ai/parea-sdk)](https://github.com/parea-ai/parea-sdk/blob/master/LICENSE)

Parea python sdk

</div>

## Installation

```bash
pip install -U parea-ai
```

or install with `Poetry`

```bash
poetry add parea-ai
```

## Getting Started

```python
import os

from dotenv import load_dotenv

from parea import Parea
from parea.schemas.models import Completion, UseDeployedPrompt, CompletionResponse, UseDeployedPromptResponse

load_dotenv()

p = Parea(api_key=os.getenv("API_KEY"))

# You will find this deployment_id in the Parea dashboard
deployment_id = '<DEPLOYMENT_ID>'

# Assuming your deployed prompt's message is:
# {"role": "user", "content": "Write a hello world program using {{x}} and the {{y}} framework."}
inputs = {"x": "Golang", "y": "Fiber"}

# You can easily unpack a dictionary into an attrs class
test_completion = Completion(
  **{
    "deployment_id": deployment_id,
    "llm_inputs": inputs,
    "metadata": {"purpose": "testing"}
  }
)

# By passing in my inputs, in addition to the raw message with unfilled variables {{x}} and {{y}}, 
# you we will also get the filled-in prompt:
# {"role": "user", "content": "Write a hello world program using Golang and the Fiber framework."}
test_get_prompt = UseDeployedPrompt(deployment_id=deployment_id, llm_inputs=inputs)


def main():
  completion_response: CompletionResponse = p.completion(data=test_completion)
  print(completion_response)
  deployed_prompt: UseDeployedPromptResponse = p.get_prompt(data=test_get_prompt)
  print("\n\n")
  print(deployed_prompt)


async def main_async():
  completion_response: CompletionResponse = await p.acompletion(data=test_completion)
  print(completion_response)
  deployed_prompt: UseDeployedPromptResponse = await p.aget_prompt(data=test_get_prompt)
  print("\n\n")
  print(deployed_prompt)
```    

### Open source community features

Ready-to-use [Pull Requests templates](https://github.com/parea-ai/parea-sdk/blob/master/.github/PULL_REQUEST_TEMPLATE.md)
and several [Issue templates](https://github.com/parea-ai/parea-sdk/tree/master/.github/ISSUE_TEMPLATE).

- Files such as: `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically.
- [Semantic Versions](https://semver.org/) specification
  with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter).

## 🛡 License

[![License](https://img.shields.io/github/license/parea-ai/parea-sdk)](https://github.com/parea-ai/parea-sdk/blob/master/LICENSE)

This project is licensed under the terms of the `Apache Software License 2.0` license.
See [LICENSE](https://github.com/parea-ai/parea-sdk/blob/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{parea-sdk,
  author = {joel-parea-ai},
  title = {Parea python sdk},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/parea-ai/parea-sdk}}
}
```
