import tensorflow as tf

# graph 생성 
# 1x2행렬
matrix1 = tf.constant([[3. , 3.]])
# 2x1행렬
matrix2 = tf.constant([[2.],[2.]])
# 행렬 곱
product = tf.matmul(matrix1, matrix2)

# session에서 graph 실행
# session 생성
sess = tf.Session()
# op실행
result = sess.run(product)
print(result)
# session 닫기
sess.close()

# with구문으로 sess.close() 자동 실행 구문
# with tf.Session() as sess:
#     result = sess.run([product])
#     print(result)
