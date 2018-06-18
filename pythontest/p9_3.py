import matplotlib.pyplot as plt
steps = [6543, 7000, 8900, 10789, 3467, 11045, 5095]
labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
num_bars = len(steps)
positions = range(1, num_bars+1)
plt.bar(positions, steps, align='center')
#以下は変更前(p9_3)のコード
#plt.barh(positions, steps, align='center')

plt.xticks(positions, positions)
#以下は変更前(p9_3)のコード
#plt.yticks(positions, labels)
plt.xlabel('Steps')
plt.ylabel('Day')
plt.title('Number of steps walked')

plt.grid()
plt.show()
