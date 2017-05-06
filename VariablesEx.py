import tensorflow as tf

#값이 0인 스칼라로 초기화된 변수 생성
state = tf.Variable(0, name="counter")

# 'state'에 1을 더하는 op 생성
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

# init op생성
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    # init op실행
    sess.run(init_op)
    # 처음 state 값 출력
    print(sess.run(state))
    # 3번 update하며 state값 출력
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))