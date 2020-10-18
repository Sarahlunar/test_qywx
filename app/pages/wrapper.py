from appium.webdriver.common.mobileby import MobileBy


def handle_black(func):
    def wrapper(*args, **kwargs):
        from app.pages.base import Base
        _black_list = [(MobileBy.XPATH, '//*[@text="确定"]'),
                       (MobileBy.XPATH, '//*[@text="下次再说"]'),
                       (MobileBy.XPATH, '//*[@text="好的"]')
                       ]
        _max_try = 3
        _cur_try = 0
        instance: Base = args[0]
        try:
            el = func(*args, **kwargs)
            _cur_try = 0
            instance._driver.implicitly_wait(1)
            return el
        except Exception as e:
            # 出现异常,隐士等待时间修改为1
            instance._driver.implicitly_wait(1)
            # 如果重试次数超出了最大次数, 抛出异常
            if _cur_try > _max_try:
                raise e
            _cur_try += 1
            # 判断黑名单
            for b in _black_list:
                els = instance._driver.find_elements(*b)
                # 如果存在弹窗, 点击并重新执行find方法
                if len(els) > 0:
                    els[0].click()
                    return wrapper(*args, **kwargs)
            raise e
    return wrapper
