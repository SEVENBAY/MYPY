import xlrd
import re


"""
将excel文件中的内容填充到sql语句中
"""
p1 = "(.*?)（"
p2 = "（(.*)）"

old_file = r"C:\Users\Administrator\Desktop\X86脚本\系统及对应业务部门联系人_20180521V1.1.xlsx"
new_file = r"C:\Users\Administrator\Desktop\new.txt"

old_book = xlrd.open_workbook(old_file)
old_book_sheet = old_book.sheets()[0]
sheet_rows = old_book_sheet.nrows
sheet_cols = old_book_sheet.ncols
f = open(new_file,"w+")
for i in range(1,sheet_rows):
    str1 = old_book_sheet.row_values(i)[0].replace(" ", "")
    str2 = old_book_sheet.row_values(i)[1].replace(" ", "").replace("\n", "")
    a = re.search(p1,str1).group(1)
    b = re.search(p2,str1).group(1)
    c = "insert into MD_FLOW_PROB_CFG_SYS(id,system_code,system_name,dept_name)" \
        "values(SEQ_ANNOUNCE.nextval,'{0}','{1}','{2}');"
    result = c.format(a,b,str2)
    f.write(result+"\n")
f.close()
print("写入完成！")
