import pandas as pd
from pandas import ExcelWriter

df1 = pd.DataFrame([["Hossein", "26"], ["Reza", "30"]], columns=["Name", "Age"])
df2 = pd.DataFrame([["173", "60"], ["165", "55"], ["180", "80"]], columns=["Height", "Weight"])
with ExcelWriter("exportData.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Sheet1")
    df2.to_excel(writer, sheet_name="Sheet2")
