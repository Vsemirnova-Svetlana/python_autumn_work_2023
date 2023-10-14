
st = [str(i) for i in [num for number in (list(map(int, i*([str(i)])) for i in range(1,11))) for num in number]]
print(', '.join(st))