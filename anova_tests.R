# Simple script I stole from http://www.stat.columbia.edu/~martin/W2024/R8.pdf
# Calculates two-way ANOVA results and makes box-plots for Alpha Diversity metrics.

dat = read.table("/Users/jimbo/Desktop/anova_data.txt",header=TRUE)
dat
par(mfrow=c(1,1))

# Plot box plots and interaction effects
plot(PD_whole_tree ~ Month, data=dat)
interaction.plot(dat$Month, dat$Basin, dat$shannon)
interaction.plot(dat$Basin, dat$Month, dat$shannon)

# two-way anova
results = lm(simpson_reciprocal ~ Basin + Month + Basin*Month, data=dat)
anova(results)
qqnorm(results$res)
qqline(results$res)

#normality assumptions
plot(qqnorm)
plot(results$fitted,results$res,xlab="Fitted",ylab="Residuals")
