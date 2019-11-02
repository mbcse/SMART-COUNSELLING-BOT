drop table new_questions;

create table new_questions (question_id int , question varchar(1000) , weight int, category varchar(100));
insert into new_questions values((1,"how are you doing today" , 3 , "N"),
								 (2,"what do you do to relax" , 1 , "N"),
                                 (3,"how easy is it for you to get a good night's sleep" , 4 ,"N"),
                                 (4,"when was the last time you argued with someone and how did you feel " ,4, "N"),                                 
                                 (5,"what do you do when you are annoyed " , 2 ,"N"),
                                 (6,"have you been diagnosed with depression " , 5 , "N"),
                                 (7,"how many times in the last 30 days did you feel nervous or depressed " , 4 ,"K" ),
								 (8,"how often did you feel that everything was an effort" , 3 ,"K"),
                                 (9 ,"do you ever feel so sad that nothing could cheer you up and how often does that happen" , 2,"K"),
                                 (10 ,"how often do you feel worthless" , 5 ,"K"));
                                 
                                 #1-least : 1; 2 less:2 ; 3- nuetral: 2 , 4 - more : 3, 5 - most : 2
                                  
                                 
                                
		
							
