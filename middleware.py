# 定义自己的中间件
def simple_middleware(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。
    print('中间件11111111---------init--------DEBUG模式 执行两次')
    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用。
        print('中间件111111------处理请求对象之前-------')

        response = get_response(request)

        # 此处编写的代码会在每个请求处理视图之后被调用。
        print('中间件111111------处理请求对象之后-------')
        return response

    return middleware

def simple_middleware_two(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。
    print('中间件22222222---------init--------DEBUG模式 执行两次')
    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用。
        print('中间件22222222------处理请求对象之前-------')

        response = get_response(request)

        # 此处编写的代码会在每个请求处理视图之后被调用。
        print('中间件22222222------处理请求对象之后-------')
        return response

    return middleware