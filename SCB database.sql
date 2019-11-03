create database SCB;
create table questions 
(question_id int ,
question varchar(2000),
primary key (question_id));

insert into questions
values(1,"how often did you feel tired out for no good reason"),
(2,"how often did you feel nervous"),
(3,"how often did you feel so nervous that nothing could calm you down"),
(4,"how often did you feel hopeless"),
(5,"how often did you feel restless or fidgety"),
(6,"how often did you feel so restless you could not sit still?"),
(7,"how often did you feel depressed"),
(8,"how often did you feel that everything was an effort"),
(9,"how often did you feel so sad that nothing could cheer you up?"),
(10,"how often did you feel worthless");

#drop table questions;
#select * from questions;

create table answers
(answer_id int,
options varchar(2000),
primary key (answer_id));

#drop table answers;

insert into answers
values(1,"none of the time"),
(2,"a little of the time"),
(3,"some of the time"),
(4, "most of the time"),
(5, "all of the time");


#select * from answers;
#select * from questions;

create table score_card
(username varchar(200),
q1 int,
q2 int,
q3 int,
q4 int,
q5 int,
q6 int,
q7 int,
q8 int,
q9 int,
q10 int,
total_score int,
primary key(username));
