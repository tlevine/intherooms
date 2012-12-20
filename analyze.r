#!/usr/bin/Rscript --vanilla
library(sqldf)
library(ggplot2)

timely <- sqldf('select Day, Time, count(*) AS count from meeting_search group by Day, Time;', dbname = 'intherooms.db')
p.timely <- ggplot(timely) + aes(x = Day, y = Time, size = count) + geom_point()

daily <- sqldf('select Day, count(*) AS count from meeting_search group by Day;', dbname = 'intherooms.db')
daily$Day <- factor(daily$Day, levels = c("SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"))
p.daily <- ggplot(daily) + aes(x = Day, y = count) + geom_point()
