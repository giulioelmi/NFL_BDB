import pandas as pd
import glob
from merge import vertical_merge

df_input = vertical_merge("data/input")
df_output = vertical_merge("data/output")

df_output.describe()