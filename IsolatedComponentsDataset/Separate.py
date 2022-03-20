#%%
from fileinput import filename
import pandas
import os
#%%
PREFIX = 'train'
#%%
df = pandas.read_csv(f'./{PREFIX}/_classes.csv')

#%%
component_classes = [
    "Label",
    "Button",
    "TextBox",
    "Image",
    "CheckBox",
    "ListPicker",
    "Slider",
    "Switch",
    "Map"
]

#%%
for component_class in component_classes:
    os.makedirs(os.path.join(PREFIX, component_class))

# %%
for index, item in df.iterrows():
    filename = item.get('filename')
    filepath = os.path.join(PREFIX, filename)
    for row, value in item.iteritems():
        if value == 1:
            component_class = row.strip()
            new_filepath = os.path.join(PREFIX, component_class, filename)
            break
# %%
