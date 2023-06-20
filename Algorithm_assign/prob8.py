#text = 'Show your flowcharts and conceal your tables and I will be mystified. Show your tables and your flowcharts will be bvious.'

#파일 경로 입력
file_input = "Algorithm_assign\HarryPotter.txt"
#샘플파일 불러오기 open("입력한 파일 경로","r")
file = open(file_input,"r")
text = file.read().replace('\n', '')

#입력받은 text 해시테이블로 저장
text_list = text.split(' ')
table = {}
n = len(text_list)

#출발
k_list = (text_list[:2])
k = ' '.join(text_list[:2])
table[k] = [text_list[2]]

for i in range(3,n):
  del k_list[0] #맨 앞자리 지우기
  k_list.append(text_list[i])
  k = ' '.join(k_list)

  if k not in table:
    try:
      table[k] = [text_list[i+1]]
    except IndexError:
      table[k] = ['[end]']
  else:
      table[k] = table[k] + [text_list[i+1]]

#랜덤출력 함수 구현
import random

input = input("텍스트를 시작할 두 단어 입력 : ") #input을 입력받는다

def makeText (input):

  p_list = input.split(' ')

  #출발
  k_list = input.split(' ')
  next_text= random.choice(table[input])
  k_list.append(next_text)
  p_list.append(next_text)

  for i in range(2,n):
    del k_list[0]
    k = ' '.join(k_list)

    if k in table:
      next_text= random.choice(table[k])
      k_list.append(next_text)
      p_list.append(next_text)
      if len(p_list)>100:
        break
    else:
      break

  res = ' '.join(p_list)
  return print(res)

makeText(input)