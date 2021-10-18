import cv2

img = cv2.imread('F:\\FFOutput\\aesthetic_o_vibes\\1.jpg',0)

s = set()
thresh = 127
im = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]

# cv2.imshow("img",im)
# cv2.waitKey(0)

import xlsxwriter

workbook = xlsxwriter.Workbook('k.xlsx')
worksheet = workbook.add_worksheet('sheet1')
worksheet.set_column('A:A', 15)
worksheet.set_column('B:B', 10)
for i in range(1,5):
    worksheet.write(i-1,0,i)
    worksheet.insert_image(i-1,1,f"F:\\FFOutput\\aesthetic_o_vibes\\{i}.jpg",{'x_scale': 0.3, 'y_scale': 0.3})
workbook.close()    