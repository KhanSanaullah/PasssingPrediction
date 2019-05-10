TotalMarks = int(input('Enter Total Marks '))
PassingMarks = int(input('Enter Passing Marks '))
TotalObtainMarks = int(input('Enter Total Obtain Marks Marks '))
RemainingMarks = int(input('Enter Remaining Marks '))

RequiredMarks=PassingMarks-TotalObtainMarks

Percent = round((RequiredMarks/RemainingMarks)*100)
if Percent > 100:
    print('You are Fail')
else:
  Percentage = 100-Percent
  print('')
  print('You have '+str(Percentage)+' % chance to pass this Course')