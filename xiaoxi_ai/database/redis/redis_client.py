import redis

# 连接到Redis服务器
r = redis.Redis(
    host='192.168.0.188',
    port=6379,
    db=12,
    password='aoji123!@#'
)
if __name__ == "__main__":
    # 测试连接
    try:
        # 使用 ping() 方法检查连接是否成功
        r.ping()
        print("连接成功！")
    except redis.ConnectionError:
        print("连接失败！")

    # 设置一个键值对
    r.set('foo', 'bar')

    # 获取键对应的值
    value = r.get('foo')
    print(f'键foo的值是: {value.decode("utf-8")}')
