from pathlib import Path
import pandas as pd

# 找到当前 Python 文件所在的文件夹
folder = Path(__file__).parent

# 拼出 CSV 文件的路径
input_file = folder / "raw_cases.csv"

# 把 CSV 读取成 Pandas 表格
df = pd.read_csv(input_file, encoding="utf-8")

# 查看表格和数据数量
print(df)
print("行数、列数：", df.shape)


# 分别检查两列是否缺失
missing_question = df["question"].isna()
missing_answer = df["expected_answer"].isna()

# 任意一列缺失，这一行就需要检查
invalid_mask = missing_question | missing_answer

# 取出需要检查的行
invalid_cases = df[invalid_mask]

print("缺少问题或预期答案的记录：")
print(invalid_cases)

print("问题记录数量：", len(invalid_cases))


# 判断问题和答案是否都重复
duplicate_mask = df.duplicated(
    subset=["question", "expected_answer"],
    keep="first"
)

print("需要去掉的重复记录：")
print(df[duplicate_mask])









# 第一步：排除缺少问题或答案的记录
valid_df = df.dropna(subset=["question", "expected_answer"])

# 第二步：去掉重复内容，保留首次出现的记录
clean_df = valid_df.drop_duplicates(
    subset=["question", "expected_answer"],
    keep="first"
)

print("清洗后的记录：")
print(clean_df)
print("剩余条数：", len(clean_df))




# 按问题分组，统计每个问题有多少种不同答案
answer_counts = clean_df.groupby("question")["expected_answer"].nunique()

print("每个问题对应的不同答案数量：")
print(answer_counts)

# 找到答案种类超过 1 的问题，取出问题文本
review_questions = answer_counts[answer_counts > 1].index

# 找出表格中属于这些问题的行
review_mask = clean_df["question"].isin(review_questions)

review_cases = clean_df[review_mask]

print("需要核对的完整记录：")
print(review_cases)


# 找到答案种类超过 1 的问题，取出问题文本
review_questions = answer_counts[answer_counts > 1].index

# 找出表格中属于这些问题的行
review_mask = clean_df["question"].isin(review_questions)

review_cases = clean_df[review_mask]

print("需要核对的完整记录：")
print(review_cases)




# 排除需要核对的行，得到通过当前检查的记录
ready_cases = clean_df[~review_mask]

print("通过检查的记录数量：", len(ready_cases))

# 保存两张表
ready_cases.to_csv(
    folder / "clean_cases.csv",
    index=False,
    encoding="utf-8-sig"
)

review_cases.to_csv(
    folder / "review_cases.csv",
    index=False,
    encoding="utf-8-sig"
)

print("保存完成")