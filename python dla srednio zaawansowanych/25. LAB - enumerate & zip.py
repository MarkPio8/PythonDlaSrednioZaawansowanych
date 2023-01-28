projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for project, leader  in zip(projects,leaders):
    print("The leader of {} is {}".format(project,leader))

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for date,project,leader in zip(dates,projects,leaders):
    print('The leader of {} started {} is {}'.format(project,date,leader))

for pos,(project,date,leader) in enumerate(zip(projects,dates,leaders)):
    print('{} - The leader of {} started {} is {}'.format(pos+1,project,date,leader))
