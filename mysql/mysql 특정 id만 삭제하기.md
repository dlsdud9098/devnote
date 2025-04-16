# 📌 mysql에서 특정 행만 지우기

## ✅ 오늘 배운 내용
- 특정 id를 가진 데이터를 제거한다.
- python으로 사용한다.

## 🔍 상세 정리
- 테이블 안에 있던 기존 데이터들을 합치고, 그 데이터로 바꿔주려고 한다.
- 기본적으로 ```delete from table;```를 통해 데이터를 제거할 수 있지만 이번에는 특정 id만을 제거하려고 한다.
```python
# 삭제할 인덱스 리스트
delete_index = []

# 첫 번째 기록창 (2002~)
cur.execute('select * from KBO_TABLE where G >= 0 and year >= 2002;')
result = cur.fetchall()
df1 = pd.DataFrame(result)
delete_index.extend(df1['id'].to_list())

# 두 번째 기록창(2002~ , 다음 기록)
cur.execute('select * from KBO_TABLE where BB >= 0 and year >= 2002;')
result = cur.fetchall()
df2 = pd.DataFrame(result)
delete_index.extend(df2['id'].to_list())

# 세 번째 기록창(2002~ , 세부기록)
cur.execute('select * from KBO_TABLE where XBH >= 0 and year >= 2002;')
result = cur.fetchall()
df3 = pd.DataFrame(result)
delete_index.extend(df3['id'].to_list())

print(delete_index)
```
 이렇게 만들어 놓은 id 목록들을 삭제한다.

```python
query = "DELETE FROM your_table_name WHERE id IN (%s)" % ', '.join(['%s'] * len(delete_index))
cursor.execute(query, delete_index)
conn.commit()
```

## 🤔 회고 & 적용할 것
- 어디에 적용할 수 있을까?
- 추가로 공부할 것?