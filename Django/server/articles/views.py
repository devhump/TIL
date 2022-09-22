from django.shortcuts import render
import random
import datetime

# Create your views here.
def index(request):
  greetings = ["안녕하세요", "Bonjour", "Hola"]
  greeting1 = random.choice(greetings)

  poketmon = [
    "https://mblogthumb-phinf.pstatic.net/20160817_259/retspe_14714118890125sC2j_PNG/%C7%C7%C4%AB%C3%F2_%281%29.png?type=w800",
    "https://mblogthumb-phinf.pstatic.net/MjAxOTAxMTFfMzAw/MDAxNTQ3MTg4MzUxNDk3.MDppdFgXR_oSpWQ-btdzfzHCtJ6j9cPHtYNJ_aOfxPwg.jodOhnYfP2KUuTngksUgluw-RKHyOYU9lUtHhqMOfP0g.JPEG.jurong25/20190111_152821.jpg?type=w800",
    "https://img1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/cnoC/image/8Ql-wYAJmiMkSg4gvS6zhMewDg4.JPEG",
    "data:image/jpeg;base64,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",
  ]
  
  start_pock = random.choice(poketmon)

  context ={
    'greetings' : greetings,
    'greeting1' : greeting1,
    'pocketmon' : start_pock,
  }

  return render(request, 'index.html', context)


def todaydinner(request):
  # todayis = datetime.datetime.today()
  food_num = random.randrange(0,5)
  food_img = [
    "https://src.hidoc.co.kr/image/lib/2021/8/27/1630049987719_0.jpg",
    "http://img.segye.com/content/image/2020/07/15/20200715519859.jpg",
    "http://image.g9.co.kr/g/1832366398/n?ts=1634380390000",
    "https://recipe1.ezmember.co.kr/cache/recipe/2018/09/14/caddf21e43f4e734ff3ee24b8b2a4d501.jpg",
    "https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202112/27/a99042fd-9510-42e9-97d6-6ae45ad666fc.jpg",
  ]
  food_list = [
    "삼겹살",
    "평양냉면",
    "돈까스",
    "제육덮밥",
    "치킨",
  ]

  context = {
    'food_img' : food_img[food_num],
    'food_name' : food_list[food_num],
  }

  return render(request, 'todaydinner.html', context)

def lotto(request):

  def lotto_oneline():
    lotto_num_list = random.sample(range(1,47), 6)
    # lotto_num_list = [3, 11, 15, 29, 35, 10]
    lotto_num_list.sort() 
    #sort 해서 인덱스 순서대로 확인

    lotto_lastweek = [3, 11, 15, 29, 35, 44]
    lastweek_bonus = 10
    _bonus = lastweek_bonus

    cnt = 0
    if lastweek_bonus in lotto_num_list: #보너스 번호 포함 여부에 따라 분기 
      lotto_num_list.remove(lastweek_bonus)
      lastweek_bonus = True 

      for i in range(len(lotto_num_list)):

        if lotto_num_list[i] == lotto_lastweek[i]:
          cnt += 1
        else:
          break

      lotto_num_list.append(_bonus)
      lotto_num_list.sort()
    else:
      lastweek_bonus = False

      for i in range(len(lotto_num_list)):

        if lotto_num_list[i] == lotto_lastweek[i]:
          cnt += 1
        else:
          break

    if cnt == 6:
      result = '1등'
    elif cnt == 5 and (lastweek_bonus == True):
      result = '2등'
    elif cnt == 5:
      result = '3등'
    elif cnt == 4:
      result = '4등'
    elif cnt == 3:
      result = '5등'
    else:
      result = '꽝'
    
    return [lotto_num_list, result]

  _result1 = lotto_oneline()
  _result2 = lotto_oneline()
  _result3 = lotto_oneline()
  _result4 = lotto_oneline()
  _result5 = lotto_oneline()
  
  
  context = {
    'lotto_nums_1' : _result1[0],
    'result_1' : _result1[1],

    'lotto_nums_2' : _result2[0],
    'result_2' : _result2[1],

    'lotto_nums_3' : _result3[0],
    'result_3' : _result3[1],

    'lotto_nums_4' : _result4[0],
    'result_4' : _result4[1],

    'lotto_nums_5' : _result5[0],
    'result_5' : _result5[1],
  }
  return render(request, 'lotto.html', context)