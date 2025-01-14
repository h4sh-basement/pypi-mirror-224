# Kodexa Command Line Tools

[![Kodexa CLI Python Package](https://github.com/kodexa-ai/kodexa-cli/actions/workflows/build-and-release.yml/badge.svg)](https://github.com/kodexa-ai/kodexa-cli/actions/workflows/build-and-release.yml)

![img.png](https://docs.kodexa.com/img.png)

Kodexa is a platform for building intelligent document processing pipelines. It is a set of tools and services that
allow you to build a pipeline that can take a document, extract the content, and then process it to extract the
information you need.

It is built on a set of core principles:

* **Document Centric** - Kodexa is built around the idea of a document. A document is a collection of content
  nodes that are connected together. This is a powerful model that allows you to build pipelines that can
  extract content from a wide range of sources.

* **Pipeline Oriented** - Kodexa is built around the idea of a pipeline. A pipeline is a series of steps that
  can be executed on a document. This allows you to build a pipeline that can extract content from a wide range
  of sources.

* **Extensible** - Kodexa is built around the idea of a pipeline. A pipeline is a series of steps that can be executed
  on a document. This allows you to build a pipeline that can extract content from a wide range of sources.

* **Label Driven** - Kodexa focuses on the idea of labels. Labels are a way to identify content within a document
  and then use that content to drive the processing of the document.

# Command Line Tools

This repository contains the command line tools for Kodexa. The tools are the primary way to interact with Kodexa. It
allows you to configure components and manage aspects of your Kodexa Platform installation.

## Documentation & Examples

Documentation is available at the [Kodexa Documentation Portal](https://docs.kodexa.com)

## Current Development

**BUILD VERSION FLOW**
![build-version-flow.png](docs%2Fbuild-version-flow.png)
Build version will differ based on the branches that are published to pypi.

**GITHUB PROCESS**
![github-process.png](docs%2Fgithub-process.png)
Changes that contain bugs, features, and fixes should first be pushed to the test branch.
Once these changes are thoroughly tested, they can be submitted as a pull request to the main branch. The pull request should be reviewed and approved by an appropriate person before the changes can be merged.

## Set-up

We use poetry to manage our dependencies, so you can install them with:

    poetry install

You can then run the tests with:

    poetry run pytest

# Contributing

We welcome contributions to the Kodexa platform. Please see our [contributing guide](CONTRIBUTING.md) for more details.

# License

Apache 2.0
