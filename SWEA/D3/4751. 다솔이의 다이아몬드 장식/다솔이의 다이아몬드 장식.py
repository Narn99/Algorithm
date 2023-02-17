# 다솔이의 다이아몬드 장식
# 문자열을 다이아몬드로 감싸서 장식하고, 빈 곳은 .으로 채워넣음
# 첫 열만 작성한 뒤, 그 뒤는 반복문으로 늘려가면 될 듯.
# 5개씩 행마다 반복문으로 쭉 작성한 뒤에, 전치행렬로 바꾸면 되지 않을까
 
T = int(input())
 
for case in range(T) :
 
    word = list(input())
    long = len(word)
    dia = [list('..#..')]       # 문자열을 일일이 입력...?
    for i in range(long) :
        dia += [list('.#.#.'), list('#.')+[word[i]]+list('.#'), list('.#.#.'), list('..#..')]
 
    dia = list(zip(*dia))       # 5열짜리 행렬로 쭉 작성한 뒤에, 5행짜리 행렬로 전치
 
    for i in range(5) :
        print(''.join(dia[i]))