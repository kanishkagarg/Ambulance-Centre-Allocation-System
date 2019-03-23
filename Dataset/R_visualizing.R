data<-read.csv("locations_data.csv", header=T)
names(data)
##creating subset of data
accident <- data
names(accident)
#month
accident$Crash_Month <- factor(accident$Crash_Month
                          , levels=c(1,2,3,4,5,6,7,8,9,10,11,12)
                          , labels=c( "January","Feburary","March","April"
                                      ,"May","June","July","August"
                                      ,"September","October","November","December"))
#severity
accident$Crash_Severity <- factor(accident$Crash_Severity
                               , levels=c(1,2,3,4,5)
                               , labels=c( "Property damage only","Minor injury","Medical treatment","Hospitalisation"
                                           ,"Fatal"))
#Lighting Condition
accident$Crash_Lighting_Condition <- factor(accident$Crash_Lighting_Condition
                                  , levels=c(1,2,3,4,5)
                                  , labels=c( "Unknown","Daylight","Dawn/Dusk","Darkness - Lighted"
                                              ,"Darkness - Not lighted"))
#Lighting Condition
accident$Crash_Speed_Limit <- factor(accident$Crash_Speed_Limit
                                            , levels=c(1,2,3,4,5)
                                            , labels=c( "0 - 50 km/h","60 km/h","70 km/h","80 - 90 km/h"
                                                        ,"100 - 110 km/h"))
#Removing null values
accident <- accident[rowSums(is.na(accident)) == 0,]
png(file = "barchart_stacked.png")
barplot(accident$Count_Casualty_Total, main = "Total Casualty", names.arg = accident$Crash_Month, xlab = "Month", ylab = "Casualty", col="blue")
dev.off()
#####  Fatalities by hour  ##############
library(ggplot2)
library(data.table)
hour<-as.factor(accident$Crash_Hour)
data_hour<-data.table(hour,accident$Count_Casualty_Total)
data_hour<-data_hour[,sum(V2),by=hour]
names(data_hour)<-c("HOUR","fatals")
png(filename="hour.png" , width=1000, height=500)
ggplot(data=data_hour, aes(x=data_hour$HOUR, y=data_hour$fatals, fill=data_hour$HOUR)) +
  geom_bar(stat="identity")+xlab("Time of day") + ylab("Total Casualty") +
  ggtitle("FATALITIES")+theme( plot.title = element_text(size=14, face="bold") , 
                               axis.text.x= element_text(angle=0, size=12), 
                               axis.text.y= element_text(angle=0, size=12)
                               ,legend.position="right")
dev.off()
