# Project Name : Elephants Tasks
# Version = 121

import datetime
from datetime import date , timedelta



def sessions_function(number_of_sessions):
    
    if len(number_of_sessions) < 7 :
        
        Average_number_of_sessions_per_week = 'Later'
        
        Average_number_of_minutes_per_week = 'Later'


    else :
        
        Average_number_of_sessions_per_week = sum(number_of_sessions[-7:]) / 7
        
        Average_number_of_minutes_per_week = sum(number_of_sessions[-7:] * 30) / 7 



    def total_completed (total_number_of_completed_units):

        def elephant_tasks(total_number_of_units):



            # Days
            now_day = datetime.date.today()
            start_day = datetime.date(2023 , 9 , 23)
            end_day = datetime.date(2023 , 12 , 15)

            number_of_days_left = (end_day - now_day).days + 1
            
            
            
            # Main Control Panel
            if len(total_number_of_completed_units) == 1 :
                print("Enter The Completed Units")

                   
            number_of_units_completed = sum(total_number_of_completed_units)
            number_of_units_remaining = total_number_of_units - number_of_units_completed
            daily_ration = number_of_units_remaining / number_of_days_left
            completion_rate = number_of_units_completed / total_number_of_units
            today_progress = total_number_of_completed_units[-1]
                
            ### LAST WEEK    
            completion_rate_last_week = (sum(total_number_of_completed_units[-7:]) / total_number_of_units)
                    
            average_last_week = (sum(total_number_of_completed_units[-7:]) / 7)
                    
            expected_last_week =  (number_of_units_remaining / (sum(total_number_of_completed_units[-7:]) / 7))
                
            days_after = (date.today()+timedelta(days= expected_last_week))

            expected_next_week = completion_rate + completion_rate_last_week

            # if expected_next_week > 1 :
            #     expected_next_week = (completion_rate + completion_rate_last_week ) - completion_rate
            
            
            

                   


            if len(total_number_of_completed_units) < 7:
                completion_rate_last_week = 'Later'
                average_last_week = 'Later'
                expected_last_week = 'Later'
                expected_next_week = 'Later'
                days_after = 'Later'
                            
                            
                print('\n1 - Daily Ration ({:.4}) | Today\'s Progress ({}) | Number Of Days Left ({})({}) '.format(daily_ration , today_progress , end_day , number_of_days_left ))
                print('\n2 - Average Daily Weekly Progress : ({}) | Expected Based On Last Week : ({})({})'.format( average_last_week  , days_after , expected_last_week))
                print('\n3 - Completion Rate ({:.2%}) | Last Week : ({}) | Expected Next Week ({}) '.format(completion_rate, completion_rate_last_week , expected_next_week))
                print('\n4 - Number Of Sessions : Today ({}) | AVG Weekly ({}) | AVG Minutes ({})'.format(number_of_sessions[-1] , Average_number_of_sessions_per_week , Average_number_of_minutes_per_week  ))
                print('\n5 - Number Of Units : Completed ({}) | Full ({}) | Remaining ({})'.format(number_of_units_completed , total_number_of_units , number_of_units_remaining ))
                print('\n6 - Number Of Days From The Start : ({})\n'.format((now_day - start_day).days))

                    

                
            
            # Number Of Days Left
                
            if number_of_days_left < 1:
                print('You have passed the deadline \nModify at end_day')

            elif number_of_days_left > 0:

                daily_ration = number_of_units_remaining / number_of_days_left



            # Output Messages
            
         
            if len(total_number_of_completed_units) >= 7 :
                print('\n1 - Daily Ration ({:.4}) | Today\'s Progress ({}) | Number Of Days Left ({})({}) '.format(daily_ration , today_progress , end_day , number_of_days_left ))
                print('\n2 - Average Daily Weekly Progress ({:.4}) | Expected From Last Week ({})({:.4})'.format( average_last_week  , days_after , expected_last_week))
                print('\n3 - Completion Rate ({:.2%}) | Last Week : (+{:.2%}) | Expected Next Week (+{:.2%}) '.format(completion_rate, completion_rate_last_week , expected_next_week))
                print('\n4 - Number Of Sessions : Today ({}) | AVG Weekly ({:.5}) | AVG Minutes ({:.5})'.format(number_of_sessions[-1] , Average_number_of_sessions_per_week , Average_number_of_minutes_per_week  ))
                print('\n5 - Number Of Units : Completed ({}) | Full ({}) | Remaining ({})'.format(number_of_units_completed , total_number_of_units , number_of_units_remaining ))
                print('\n6 - Number Of Days From The Start : ({})\n'.format((now_day - start_day).days))
            
            
# Test Data


        elephant_tasks( 280 )
    total_completed([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,0])
sessions_function([5,5,5,5,5,5,5])