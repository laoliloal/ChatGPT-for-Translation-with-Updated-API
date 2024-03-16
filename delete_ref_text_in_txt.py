import os
if not os.path.isdir("./txt_not_cleaned"):
  os.mkdir("./txt_not_cleaned")

if not os.path.isdir("./txt_not_translated"):
  os.mkdir("./txt_not_translated")  # 清洁后的文档放在这里
  
# 清除格式
import re
pattern1 = r' \([A-Z][^()\n]+\d{4}\)' # Define the pattern to match, 首字母开头大写，结尾四个数字
pattern2 = r' \(for a review, see +[A-Z][^()\n]+\d{4}\)' # 开头是for a review
pattern3 = r' \(von[^()\n]+\d{4}\)' # 开头大写von，结尾四个数字
pattern4 = r' \([A-Z][^()\n]+\d{4}b\)' # 首字母开头大写，结尾四个数字+b(如2010b)
pattern5 = r' \(e.g., +[A-Z][^()\n]+\d{4}\)' # 开头是e.g.
pattern6 = r"(?<=\w)\d+(?:,\d+)*(?=[,. ])" # 以1,2,3形式来写的参考文献（常见于Nature和PNAS）

# loop over all files in folder "txt_not_cleaned"
for filename in os.listdir("./txt_not_cleaned"):
    if filename.endswith(".txt"):
        # read the contents of the file in folder A
        with open(os.path.join("./txt_not_cleaned", filename), 'r', encoding='utf-8') as input_file, open(os.path.join("./txt_not_translated", filename),'w', encoding='utf-8') as output_file:
            for line in input_file.readlines():
              matches1 = re.findall(pattern1, line)
              matches2 = re.findall(pattern2, line)
              matches3 = re.findall(pattern3, line)
              matches4 = re.findall(pattern4, line)
              matches5 = re.findall(pattern5, line)
              matches6 = re.findall(pattern6, line)

              for match in (matches1+matches2+matches3+matches4+matches5+matches6):
                  print(match)

              processed_line = re.sub(pattern1, '', line) # delete
              processed_line = re.sub(pattern2, '', processed_line) # delete
              processed_line = re.sub(pattern3, '', processed_line) # delete
              processed_line = re.sub(pattern4, '', processed_line) # delete
              processed_line = re.sub(pattern5, '', processed_line) # delete
              processed_line = re.sub(pattern6, '', processed_line) # delete

              output_file.write(processed_line)