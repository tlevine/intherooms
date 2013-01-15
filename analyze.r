#!/usr/bin/Rscript --vanilla
library(sqldf)
library(ggplot2)
library(stringr)

timely <- sqldf('select Day, Time, count(*) AS count from meeting_search group by Day, Time;', dbname = 'intherooms.db')
p.timely <- ggplot(timely) + aes(x = Day, y = Time, size = count) + geom_point()

daily <- sqldf('select Day, count(*) AS count from meeting_search group by Day;', dbname = 'intherooms.db')
daily$Day <- factor(daily$Day, levels = c("SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"))
p.daily <- ggplot(daily) + aes(x = Day, y = count) + geom_point()

meeting.descriptions = data.frame(
  desc = sqldf('SELECT "Meeting Description" FROM meeting', dbname = 'intherooms.db')[,1]
)
# sort(table(meeting.descriptions))
meeting.descriptions$ncolon <- str_count(meeting.descriptions$desc, ':')
why.colons <- sqldf('select * from [meeting.descriptions] group by ncolon')
# It looks like there are supposed to be three fields: Details, Format and Language.
# The details sometimes include more colons.
