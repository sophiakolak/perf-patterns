#install ggplot (if needed)
library.install(ggplot2)
#load data
df <- read.csv("../av_score_subs.csv")
#get correlation 
cor(df$av_num_subs, df$av_score)
library(ggplot2)
#make plot
ggplot(df, aes(x=df$av_score, y=df$av_num_subs)) + 
  labs(title = "Score versus # of attempts", 
       x = "Average score per challenge", 
       y = "Average # of submissions per user") + 
      geom_point() + geom_smooth(method=lm)