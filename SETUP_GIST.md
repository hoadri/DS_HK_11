## Installation

To install, simply run:

```
pip install jupyter-notebook-gist
jupyter serverextension enable --py jupyter_notebook_gist
sudo jupyter nbextension install --py jupyter_notebook_gist
jupyter nbextension enable --py jupyter_notebook_gist
jupyter nbextension enable --py widgetsnbextension
```

To double-check if the extension was correctly installed run:

```
jupyter nbextension list
```

Expected to see:

```
Known nbextensions:
  config dir: /Users/Usr/.jupyter/nbconfig
    notebook section
      jupyter-js-widgets/extension  enabled
      - Validating: OK
      jupyter-notebook-gist/extension  enabled
      - Validating: OK
  config dir: /Users/Usr/anaconda/etc/jupyter/nbconfig
    notebook section
      jupyter-js-widgets/extension  enabled
      - Validating: OK
```

To double-check if the extension was correctly installed run:

```
jupyter serverextension list
```

Expected to see:

```
config dir: /Users/Usr/.jupyter
    jupyter_notebook_gist  enabled
    - Validating...
      jupyter_notebook_gist  OK
```

## Configuration

Get your GitHub client id and secret. You can create one [here](https://github.com/settings/applications).

Here's an [example](https://cloud.githubusercontent.com/assets/969479/14916551/add90efc-0df0-11e6-8cfb-277754a48b66.png) of an OAuth application created by @mreid-moz for testing.

To run your notebok server:

```
jupyter notebook --NotebookGist.oauth_client_id="id_here" --NotebookGist.oauth_client_secret="secret_here"
```

## Check

Make sure the `notebook.json` under `~/.jupyter/nbconfig/` looks like the following:

```
{
  "oauth_client_id": "id_here", 
  "load_extensions": {
    "jupyter-js-widgets/extension": true, 
    "jupyter-notebook-gist/extension": true
  }, 
  "oauth_client_secret": "secret_here"
}
```