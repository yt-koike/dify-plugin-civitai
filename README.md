## CivitAI

**Author:** yt-koike
**Version:** 0.0.1
**Type:** tool

### Description

This is an unofficial CivitAI plugin for Dify and basically sugarcoats [CivitAI Rest API](https://developer.civitai.com/docs/api/public-rest).

### Setup

You can simply use this plugin by installing it.

![plugin](_assets/plugin.png)

### Nodes

This plugin has various nodes to use CivitAI API.
These output commonly used parameters but you can extract others from json.

![nodes](_assets/nodes.png)

## Images

Images node can fetch urls of the postes images on https://civitai.com/images

![images](_assets/images.png)

## Models

Model Details(Version) node can fetch models' names, versions and other related infos.

![models](_assets/models.png)

## Get Models by Hash
Get Models by Hash node can fetch details of a model by its hash.

![modelHash](_assets/modelHash.png)

## Model Details
Model Details(Version) node can fetch details of a model by its id.

![modelDetail](_assets/modelDetails.png)

## Model Details(Version)

Model Details(Version) node can fetch details about a model by its version.

![modelVersion](_assets/modelVersion.png)

## Tags

Tags node can fetch model tags.

![tags](_assets/tags.png)

### Required APIs and Credentials

This plugin requires the access to [CivitAI REST API](https://developer.civitai.com/docs/category/api).
CivitAI API key is optional and needed to make authorized requests.

### Reference

* Repository: https://github.com/yt-koike/dify-plugin-civitai
* Logo: Made on https://text-to-svg.com/
