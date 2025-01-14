![example workflow](https://github.com/earthwave/xcube_4d_viewer/actions/workflows/xcube_4d_viewer_test.yml/badge.svg)
![example workflow](https://github.com/earthwave/xcube_4d_viewer/actions/workflows/xcube_4d_viewer_deploy.yml/badge.svg)
# xcube_4d_viewer
This repository is a plugin for the xcube server.

xcube (https://xcube.readthedocs.io/en/latest/overview.html) is a Python package for generating and exploiting data
cubes powered by xarray, dask, and zarr. It also provides a web API and server which can be used to access and
visualise these data cubes.

This repository serves as an API extension to the xcube server, allowing xcube data cubes to be analysed and
visualised within Earthwave's 4D viewer. It computes configuration details and
heatmap/3D heatmap/terrain tiles from the server's data cubes and provides them in a format expected by the 4D viewer.

To make use of the API, a new MiddleTierURL key should be set in the xcube server config file. Please contact support@earthwave.co.uk for the current URL of the Middle Tier service.

Additionally, it is expected that the xcube server will be run with an externally accessible address, set through the --address flag of the xcube serve command (https://xcube.readthedocs.io/en/latest/cli/xcube_serve.html).

This work is done as part of the DeepESDL project (https://deepesdl.readthedocs.io/en/latest/).
