   
fruits_list = []

with open('data/fruits.txt', 'r', encoding= 'utf-8') as f:
    fruits_list = f.read().split(sep='\n')
    # 전체를 읽어오면서 \n 단위로 잘라 리스트에 추가
        
with open('01.txt', 'w', encoding= 'utf-8') as f:
    f.write(str(len(fruits_list)))
    

