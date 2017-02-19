def foo(date_time, temperature, threshold):
	result = []
	previous = None

	for t in range(0, len(date_time)):
		if temperature[t] > threshold:
			if previous < threshold:
				result.append(date_time[t])
		previous = temperature[t]
	return result

# for testing purposes
if __name__ == '__main__':
	T = [1460545900, 1460545910, 1460545920, 1460545930, 1460545940, 1460545950]
	R = [0, 7, 12, 18, 8, 17]
	Q = 10 
	print('> {}'.format(foo(T,R,Q)))