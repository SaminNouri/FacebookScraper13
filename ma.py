import xlsxwriter
import pandas as pd
from facebook_scraper import get_profile
from facebook_scraper import get_posts

workbook   = xlsxwriter.Workbook('b.xlsx')
worksheet1.write(0,0,'urls')
worksheet1 = workbook.add_worksheet()
df = pd.read_excel('b.xlsx')
listUsers=df['urls'].tolist()
import xlsxwriter
import pandas as pd
from facebook_scraper import get_profile
from facebook_scraper import get_posts

workbook   = xlsxwriter.Workbook('b.xlsx')
worksheet1 = workbook.add_worksheet()
df = pd.read_excel('b.xlsx')
listUsers=df['urls'].tolist()
i=1
for user in (listUsers):
    worksheet1.write(i,1,repr(get_profile(user, cookies="cookies.txt",friends=True)))
    worksheet1.write(i,0,user)
    worksheet1.write(i,2,repr(get_posts(user,cookies="cookies.txt")))
    i=i+1
workbook.close()
