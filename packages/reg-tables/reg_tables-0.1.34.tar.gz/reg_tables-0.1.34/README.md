## Description

A simple [linearmodels](https://pypi.org/project/linearmodels/) extension to run panel regressions with different specifications and export the results in a professional-looking latex table

## Installation
```
pip install reg_tables
```

## Sample Usage

```python
from reg_tables import *

# Generate Random panel
N = 10**3
df = pd.DataFrame({
    'x1': np.random.randn(N),
    'x2': np.random.randn(N),
})
df['entity'] = np.random.randint(0,10,N)
df['time'  ] = np.random.randint(0,50,N)

# Generate the `y` variable 
df['y'     ] = 2 * df['x1'] - 0.5 * df['x2'] + np.random.randn(N)

# Generate the `y2`, with some fixed effects 
df['y2'    ] = df['y'] + (df['entity'] % 3)*10 + np.where(df['time']>10, -50, 0)

# Set the panel's double-index
df = df.set_index(['entity', 'time'])

# Define the baseline specification
baseline = Spec( df, 'y2', ['x1', 'x2'], double_cluster=True )

# The renaming dictionary
rename   = {
    'y2' : 'Salary',
    'x1' : 'Education',
    'x2' : 'Age',
}

# Create the model
model = Model(baseline, rename_dict=rename)

# Define some other regression specifications
model.add_spec(y='y2', entity_effects=True)
model.add_spec(y='y2', time_effects=True)
model.add_spec(y='y2', entity_effects=True, time_effects=True)

# Run all the specifications
res = model.run()
res
```



## Classes and Methods

This package consists of two classes: `Spec` and `Model`. 

`Spec` defines the regression specifications, including the panel dataset, the independent variable, and the independent variables. Optional arguments for this class include specifying whether the regressions should be performed with entity effects, time effects or both (`entity_effects`, `time_effects` or `all_effects` arguments respectively). Methods for `Spec` class include `.run`, which runs the regression and `.rename` – a method to rename variable according to the dictionary passed.

The `Model` class is a wrapper around the `compare` function of linearmodels. When creating `Model`, one has to specify the baseline regression specification, passed as a `Spec` object. Optional arguments include passing a `rename_dict`, according to which the variables are going to be renamed, as well as setting an `all_effects` Boolean variable, which will add the four versions of baseline Spec object with all possible combinations of entity and time effects to the model. The `Model` class has `.rename`, `.add_spec` and `.remove_spec` methods. The latter has a mandatory index argument and second optional index argument, which, if passed would work as a end point for slice.  The `.run` method executes all Spec objects within Model and outputs them to a table. Optional argument `coeff_decimals` allows to specify the number of decimals for coefficient estimates and t-values, while `latex_path` allows to save the output table to a disk.
