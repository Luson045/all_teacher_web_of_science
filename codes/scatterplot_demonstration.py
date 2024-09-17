data = {'h_index' :  [4, 6, 17, 9, 6, 14, 7, 23, 10, 11, 9, 4, 21, 14, 4, 2, 4, 7, 3, 3, 2]
                , 'grade' : ['AP1', 'AP2', 'AP', 'AP', 'AP', 'AP', 'AP', 'P', 'AP', 'P', 'AP1', 'AP', 'AP2', 'AP2', 'AP', 'AP2', 'AP', 'AP2', 'AP2', 'AP', 'AP']
               , 'citations' : [39, 91, 978, 274, 24, 942, 145, 1670, 368, 921, 98, 26, 1512, 516, 43, 30, 33, 93, 59, 99, 20]
               , 'co-authors' : [120, 117, 285, 180, 84, 129, 471, 356, 69, 138, 32, 2, 452, 131, 84, 9, 15, 24, 8, 51, 4]}
df = pd.DataFrame(data)

plt.figure(figsize = (7, 5))
scatter = sns.scatterplot(data = df, x = 'co-authors', y = 'citations', hue = 'grade', palette = 'Set1', s = 50)

plt.title('Citations vs Co-authors by Grade', fontsize = 16, fontweight = 'bold')
plt.xlabel('Number of Co-authors', fontsize = 12)
plt.ylabel('Number of Citations', fontsize = 12)


plt.legend(title = 'Grade of Faculty', bbox_to_anchor = (1.05, 1), loc = 'best')
plt.tight_layout()
plt.show()
