# FluffyModel: Hugging Face Space Automation Tool

`FluffyModel` is a user-friendly CLI tool designed to seamlessly set up an inference endpoint for open-source ML models. It leverages Gradio and Hugging Face spaces to achieve this.

As a developer, you might have wanted to integrate ML models into your web and mobile apps. However, doing so usually necessitates hosting the ML model on some platform. While there are numerous hosting providers available, including industry giants like Amazon AWS and Google GCP, the process can be intricate. Often, it demands the construction of a custom Flask REST API.

FluffyModel simplifies this process. It aids in creating, structuring, and setting up a Hugging Face space for swift deployment. With a single command, users can automate the typically manual process of creating and configuring a new Hugging Face space complete with a REST API endpoint.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- **REST API endpoint**: Use the endpoint to run an inference from any language.
- **Space Creation**: Quickly create a new Hugging Face space.
- **Predefined Structure**: Automatically structure the space with necessary files such as `requirements.txt`, `README.md`, and `app.py`.
- **Easy Deployment**: Commit and push changes to the space in one go.
- **Virtual Environment Setup**: Automatically set up a virtual environment within the space, ensuring dependencies are isolated.

## Prerequisites

Before using `FluffyModel`, ensure you have:

- Python 3.x installed.
- `git` installed and available in your system's PATH.
- A Hugging Face account and a corresponding API token.

## Installation

```bash
pip install FluffyModel
```

## Usage
Once installed, 'FluffyModel' can be used with a single command, where 'git-name' is name of the repository on huggingface.co.
e.g. If you want to create an endpoint for[Facebook's resnet](https://huggingface.co/facebook/detr-resnet-50) , then the gitname would be facebook/detr-resnet-50 

```bash
fluffymodel <git-name>
```

Here's what happens next:

-- **Space Creation**: A new Hugging Face space will be created.
-- **Repository Configuration**: The repository of the space is cloned, structured, and a virtual environment is set up.
-- **Push & Deploy**: All changes are committed and pushed to the space.
-- **Instructions Display**: A URL to the space and a curl command for the inference endpoint are displayed. Users can visit the URL to monitor the build and later test the endpoint using the provided curl command.

## Contributing
If you have suggestions, bug reports, or enhancements, please:
-- Open an Issue: Before making any changes, open an issue in the GitHub repository to discuss your proposed changes.
-- Fork & Clone: Fork the repository, clone it locally, and set up a virtual environment.
-- Make Changes: Implement your changes and test them thoroughly.
-- Submit a Pull Request: Once you're satisfied with your changes, submit a pull request for review.

## License
'FluffyModel' is licensed under the MIT License. All rights reserved.