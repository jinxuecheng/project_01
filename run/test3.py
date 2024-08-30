
#这个脚本测试可行，主要用于循环表格A中每一行，将除第一格非空单元格拼接成，第一格单元格+所在列标题+单元格的数据写入表格B中
import pandas as pd
import sys
import io
# 设置标准输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# 读取表格A
df_a = pd.read_excel('万宁.xlsx')  # 替换为你的文件名

# 创建一个空的列表来存储结果
result = []

# 遍历每一行
for index, row in df_a.iterrows():
    first_col_value = row.iloc[0]  # 使用 iloc 获取第一列的值
    # 遍历除第一列以外的每一列
    for col in df_a.columns[1:]:
        col_value = row[col]
        if pd.notna(col_value):  # 检查当前单元格是否非空
            # 将数据添加到结果列表
            result.append([first_col_value, col, col_value])

# 将结果写入表格B
df_b = pd.DataFrame(result, columns=['第一列数据', '列标题', '非空数据'])
df_b.to_excel('万宁导出.xlsx', index=False)  # 替换为你想要的文件名

print('运行成功')