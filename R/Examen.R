# Obtener datos y crear dataframe a travez de csv

install.packages("readr")
library(readr)
top <- "C:\\Users\\HP15DA0023LA\\Documents\\GitHub\\Mysql-R\\data.csv"
top_csv <- read.csv(top)

#  hora de la graficada
plot(top_csv)