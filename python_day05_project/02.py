fruits_list = []
berry_list = []
cnt = 0 

with open('data/fruits.txt', 'r', encoding= 'utf-8') as f:
    
    fruits_list = f.read().split(sep='\n')
    # 전체를 읽어오면서 \n 단위로 잘라 리스트에 추가
    for name in fruits_list:
        if name.endswith('berry'):
            berry_list.append(name)

with open('02.txt', 'w', encoding= 'utf-8') as f:
    
    f.write(f"{str(len(set(berry_list)))}\n")
    berry_list = set(berry_list)
    # set 사용 => 중복된 값 제거 
    for name in berry_list:
        f.write(f"{name}\n")
    