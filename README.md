# Emerging Tech Topics Forum: Dask

### Tagline
`Dask` is a python package aimed to make parallel computing and memory management,
approachable and native. `Dask` workflows look very similar to pure Python. Crucialy,
this includes extension of some of the most important and widley used Python packages
for data management; `numpy` and `pandas`. [Visit their site here](https://www.dask.org/).

### Core Principles
The two key ideas that summarize `Dask` are 
* **chunking / partitioning**, 
* **lazy loading / lazy execution**,

and these go hand in hand.

When you read in data, if you would normaly be creating a `numpy.array`, you'll instead make
a `dask.array`, and similarly a `dask.dataframe` rather than a `pandas.dataframe`, depending on
your needs. For simplicity let's consider a `dask.array`, which when read in can by 'chunked'.
This entails breaking up your data into subsets, which can be saved out of memory, on disk
or another machine. This is the beginning of what we mean by lazy loading. We don't require 
an entire `dask.array` to be loaded into memory at once, and in fact will not access those
sections of data until called upon.

Again, `Dask` arrays and dataframes are extensions of those from `numpy` and `pandas`. In fact,
they are comprised of them! This does not mean that every function from `numpy` and `pandas` is
available in `Dask`, however. Since `Dask` is targeted at tackling large data issues, some
functions simply don't make sense to pull over, like `to_list()`, which would be extremely 
costly for a large array. You can learn more about these objects on their site for 
[dask.arrays](https://docs.dask.org/en/stable/array.html) and 
[dask.dataframes](https://docs.dask.org/en/stable/dataframe.html).





