def gradingSystem(marks):
    if marks >= 90 and marks <=100:
        print('4')
    elif marks >= 85 and marks < 90:
        print('3.7')
    elif marks >= 80 and marks <85:
        print('3.3')
    elif marks >= 75 and marks < 80:
        print('3.0')
    elif marks >= 65 and marks < 75:
        print('2.5')
    elif marks >= 50 and marks < 65:
        print('2.0')
    elif marks >=0 and marks <50:
        print('fail')
    else:
        print('Invalid Marks')
        
gradingSystem(110) #testing purpose
    
    # when marks = 92  then code coverage  => 3/17*100  = 17.6%
    # when marks = 87  then code coverage  => 4/17*100  = 23.5%
    # when marks = 83  then code coverage  => 5/17*100  = 29.4%
    # when marks = 77  then code coverage  => 6/17*100  = 35.3%
    # when marks = 70  then code coverage  => 7/17*100  = 41.2%
    # when marks = 60  then code coverage  => 8/17*100  = 47.0%
    # when marks = 45  then code coverage  => 9/17*100  = 52.9%
    # when marks = -10 then code coverage  => 10/17*100 = 59.0%
    # when marks = 110 then code coverage  => 10/17*100 = 59.0%
