# 1
# 데이터 준비: 성적이 담긴 리스트 만들기
scores = [85, 92, 55, 78, 40, 96, 73]

# 통계 계산: 총 학생 수, 최고점, 최저점, 평균 구하기
print('총 학생수: ', len(scores), '명')
print('최고점: ', max(scores), '점')
print('최저점: ', min(scores), '점')
avg = sum(scores) / len(scores)
print(f'평균: {avg:.1f} 점')

# 등급 출력: for문 + if문으로 각 점수의 등급 출력
for score in scores:
    if score >= 90:
        print('점수: ', score, '-> A학점')
    elif score >= 80:
       print('점수: ', score, '-> B학점')
    elif score >= 70:
        print('점수: ', score, '-> C학점')
    elif score >= 60:
        print('점수: ', score, '-> D학점')
    else:
        print('점수: ', score, '-> F학점')

# 정렬, 슬라이싱: 점수를 정렬하고 상위 3개만 뽑기
scores.sort(reverse = True)
print('상위 3개: ', scores[:3])