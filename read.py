data = []
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
print('檔案讀取完了,總共有',len(data),'筆資料')
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('平均留言是',sum_len/len(data))
