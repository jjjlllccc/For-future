print("请输入舵机角度（0-180）：")
angle=int(input())
if angle<0 or angle>180:
    print("输入角度不合法，请输入0-180之间的整数。")
else:
    pwm_us = 500+(angle/180)*2000
    duty_cycle = (pwm_us / 20000) * 100
    print("舵机角度：", angle, "°")
    print("PWM脉冲宽度：", pwm_us, "μs")
    print(f"占空比：{duty_cycle:.2f}%")