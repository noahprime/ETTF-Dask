# Emerging Tech Topics Forum: Dask

### Tagline
`Dask` is a python package aimed to make parallel computing and memory management,
approachable and native. `Dask` workflows look very similar to pure Python. Crucially,
this includes extension of some of the most important and widely used Python packages
for data management; `numpy` and `pandas`. [Visit their site here](https://www.dask.org/).

### Core Principles
The two key ideas that summarize `Dask` are 
* **chunking / partitioning**, 
* **lazy loading / lazy execution**,

and these go hand in hand. Data is split into smaller sets and kept on disc instead of in memory.
When operations are called on these data, tasks are added to a growing list. Not until the user
explicitly asks to compute the data do these computations happen, and data is read in as needed.
This enables a scheduler to manage and distribute tasks to workers.

See the [`getting_started` notebook](https://github.com/noahprime/ETTF-Dask/blob/main/notebooks/getting_started.ipynb)
for examples of `Dask`'s functionality.





