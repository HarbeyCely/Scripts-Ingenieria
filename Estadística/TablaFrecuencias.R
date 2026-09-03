library(readxl)
MatrizP4000 <- read_excel("MatrizP4000.xlsx", 
                          sheet = "Area")
View(MatrizP4000)

## attach sirve para capturar las columnas como variables

attach(MatrizP4000)
names(MatrizP4000)
library(fdth)
tipo=as.factor(P4000)
tipo
tabla1=fdt_cat(tipo, sort=FALSE)
tabla1

                                                ##help("fdt_cat")
