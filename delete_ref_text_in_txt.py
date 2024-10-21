import os
if not os.path.isdir("./txt_not_cleaned"):
  os.mkdir("./txt_not_cleaned")

if not os.path.isdir("./txt_not_translated"):
  os.mkdir("./txt_not_translated")  # 清洁后的文档放在这里
  
# 清除格式
import re
# 人名-年份格式，单引号和双引号不影响使用
pattern1 = r' \([A-Z][^()\n]+\d{4}\)' # Define the pattern to match, 首字母开头大写，结尾四个数字
pattern2 = r' \(for a review, see +[A-Z][^()\n]+\d{4}\)' # 开头是for a review
pattern3 = r' \(von[^()\n]+\d{4}\)' # 开头小写von，结尾四个数字
pattern4 = r' \([A-Z][^()\n]+\d{4}[a-z]\)' # 首字母开头大写，结尾四个数字+一个小写字母(如2010b)
pattern5 = r' \(e.g., +[A-Z][^()\n]+\d{4}\)' # 开头是e.g.
# 数字格式
pattern6 = r"(?<=[A-Za-z,.])\d+(?:\s*,\s*\d+)*(?=[,. ])" # 以1,2,3形式来写的参考文献，前接一个字母或标点，后接标点或空格（常见于Nature和PNAS）
pattern7 = r"(?<=[A-Za-z])\d+(?=[,. ])"# 以gratitude84形式来写的参考文献，前接一个字母，后接标点或空格
pattern8 = r"\[\d+\.?(?:, ?\d+\.?)*\]" # 以[10., 11.]形式来写的参考文献（常见于Trends系列）（也可匹配[10,11]，[10, 11]形式）
pattern9 = r"\[\d{1,3}\.?\]" # 以[10.]形式来写的参考文献（也可匹配[10]形式）
pattern10 = r"\[\d+(?:[-–,]\s*\d+)*\]"  # 以[4, 6–9]形式来写的参考文献（常见Plos）
pattern11 = r"\(\d+,\s*\d+(?:,\s*\d+)*\)" # 以(10,11)或(10, 11)形式来写的参考文献

patterns = [pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7, pattern8, pattern9, pattern10, pattern11]  # 放到列表中


# loop over all files in folder "txt_not_cleaned"
for filename in os.listdir("./txt_not_cleaned"):
    if filename.endswith(".txt"):
        # read the contents of the file in folder A
        with open(os.path.join("./txt_not_cleaned", filename), 'r', encoding='utf-8') as input_file, open(os.path.join("./txt_not_translated", filename),'w', encoding='utf-8') as output_file:
            for line in input_file.readlines():
              line_processing=line

              for pattern in patterns:                  
                # 显示匹配结果
                matches = re.findall(pattern, line_processing)
                if matches:
                  print(f"{matches}")
                  # 删除匹配结果
                  line_processing = re.sub(pattern, '', line_processing)
                
              processed_line = line_processing
              output_file.write(processed_line)