# import libraries
library(readr)
library(lubridate)
library(dplyr)
library(ggplot2)

construcoes_pb <- read_csv("~/Documents/Projects/Construções Paraiba/Data-Analysis-of-Constructions-in-Paraiba-Brazil/Data/construcoes_pb.csv")

############################## Data Cleaning ###################################
### remove id column
construcoes_pb <- construcoes_pb[,-1]

### change data types

# Set the locale to Portuguese (Portugal)
Sys.setlocale(locale = "pt_PT.UTF-8")

# Assume every date starts on day 1
# Convert data to date format
construcoes_pb$Inicio <- dmy(paste("1 ",construcoes_pb$Inicio))
construcoes_pb$Conclusao <- dmy(paste("1 ",construcoes_pb$Conclusao))

### I noticed Extensao was supposed to be in km but was in dm 
construcoes_pb$`Extensao(km)` <- construcoes_pb$`Extensao(km)`/100

### Switch valor and valor medido to float
# rewrite to correct format
construcoes_pb$Valor <- gsub("R\\$ ","",construcoes_pb$Valor,ignore.case = TRUE)
construcoes_pb$Valor <- gsub("\\.","",construcoes_pb$Valor) #in Brazil , means . and vice versa
construcoes_pb$Valor <- gsub("\\,","\\.",construcoes_pb$Valor)
# switch to num type
options(digits=12)
construcoes_pb$Valor <- as.numeric(construcoes_pb$Valor)
# Repeat steps to Valor Medido
construcoes_pb$`Valor Medido` <- gsub("R\\$ ","",construcoes_pb$`Valor Medido`,ignore.case = TRUE)
construcoes_pb$`Valor Medido` <- gsub("\\.","",construcoes_pb$`Valor Medido`) #in Brazil , means . and vice versa
construcoes_pb$`Valor Medido` <- gsub("\\,","\\.",construcoes_pb$`Valor Medido`)
construcoes_pb$`Valor Medido` <- as.numeric(construcoes_pb$`Valor Medido`)

View(construcoes_pb)

############################## Data Exploration ###################################
# Tipos de estagios: 
unique(construcoes_pb$Estagio) # "Concluída"    "Em execução"  "Em projeto"   "Em licitação" "A iniciar"  

# Focar nos que ainda vao aumentar o preco em execucao
em_execucao <- construcoes_pb[construcoes_pb$Estagio=='Em execução',]
em_execucao <- em_execucao[,-c(3,5,9,10)]
View(em_execucao)

# Visualizar os que ja foram concluidas
concluidas <- construcoes_pb[construcoes_pb$Estagio=='Concluída',]
concluidas <- concluidas[,-c(3,5,9,10)]
View(concluidas)


