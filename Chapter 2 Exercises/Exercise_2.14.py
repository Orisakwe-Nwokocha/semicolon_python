age = int(input("Enter your age:\n"))

maximum_heart_rate = 220 - age
low_target_heart_rate = 0.50 * maximum_heart_rate
high_target_heart_rate = 0.85 * maximum_heart_rate


print("The maximum heart rate is", maximum_heart_rate, "beats per minute""\n""The range of the target heart rate is", "%.0f" % low_target_heart_rate+"-"+"%.0f" % high_target_heart_rate, "beats per minute")