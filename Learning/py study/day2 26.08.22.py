#Day 2 : 批量舵机PWM计算+简单轨迹规划

print("\n【批量计算PWM】")
for i, angle in enumerate(joint_angles):
    pwm_us=500+(angle/180)*2000
    duty=(pwm_us/20000.0)*100
    print(f"joint{i}:{angle:3}°→PWM{pwm_us:6.1f} us ({duty:.2f}%)")
    