| `import pandas as pd`            | 导入 Pandas，简称 `pd`      
| -------------------------------- | ---------------------- 
| `pd.read_csv(path)`              | 读取 CSV，得到 DataFrame 表格 
| `df.shape`                       | 查看 `(行数, 列数)`          
| `df["question"]`                 | 取出一列                   
| `df.loc[4, "question"]`          | 取行索引为 4、指定列的单元格        
| `.isna()`                        | 判断是否缺失，返回 True/False   
| `.str.strip()`                   | 去掉文本首尾空白               
| `.replace("", pd.NA)`            | 把空字符串变成缺失值             
| `.duplicated(subset=[...])`      | 判断哪些行重复                
| `.dropna(subset=[...])`          | 排除指定列有缺失值的行            
| `.drop_duplicates(subset=[...])` | 返回去重后的表                
| `.groupby("question")`           | 按相同问题分组                
| `.nunique()`                     | 统计不同值的数量               
| `.index`                         | 取索引；分组结果里是问题文本         
| `.isin(values)`                  | 判断每个值是否在指定集合中          
| `.to_csv(path, index=False)`     | 保存 CSV，不写入行索           
