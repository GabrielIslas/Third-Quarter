## -------------------------------------------------------------
## Stat/Q Sci 403 Lab 7 | Spring 2017 | University of Washington
## -------------------------------------------------------------
###                                   ###
### Part 1: Bootstrapping Correlation ###
###                                   ###
data1 = faithful
head(data1)

cor(data1)
cor(data1)[1,2]

data1_cor = cor(data1)[1,2]

## uncertainty of cor
n = nrow(data1)

w = sample(n,n,replace=T)
w
table(w)

data1_BT = data1[w,]
cor(data1_BT)
cor(data1_BT)[1,2]

B = 10000
data1_cor_BT = rep(NA, B)
for(i_BT in 1:B){
  w = sample(n,n,replace=T)
  data1_BT = data1[w,]
  data1_cor_BT[i_BT] = cor(data1_BT)[1,2]
}

hist(data1_cor_BT, col="orange")
abline(v=data1_cor,lwd=6, col="blue")

var(data1_cor_BT)

mean((data1_cor_BT-data1_cor)^2)

data1_cor - qnorm(0.95)*sd(data1_cor_BT)
data1_cor + qnorm(0.95)*sd(data1_cor_BT)

quantile(data1_cor_BT, c(0.05,0.95))


### partial correlations
data2 = iris[,1:4]
head(data2)
cor(data2)

lower.tri(cor(data2))

cor(data2)[lower.tri(cor(data2))]
  # getting the elements in the lower triangle

data2_cor = cor(data2)[lower.tri(cor(data2))]

n = nrow(data2)

data2_cor_BT = matrix(NA, nrow=B, ncol=length(data2_cor))

head(data2_cor_BT)
for(i_BT in 1:B){
  w = sample(n,n,replace=T)
  data2_BT = data2[w,]
  data2_cor_BT[i_BT,] = cor(data2_BT)[lower.tri(cor(data2_BT))]
}
head(data2_cor_BT)

# variance matrix
var(data2_cor_BT)
  # this gives you variance-covariance matrix

diag(var(data2_cor_BT))
  # this gives you the variance of each 'variable'

data_cor_var = matrix(0, nrow=4,ncol=4)
colnames(data_cor_var) = colnames(cor(data2))
rownames(data_cor_var) = rownames(cor(data2))

data_cor_var

data_cor_var[lower.tri(data_cor_var)] = diag(var(data2_cor_BT))

data_cor_var

data_cor_var = data_cor_var + t(data_cor_var)
  # symmetrize the matrix

data_cor_var
  # this gives you the variance of each "partial correlation"
cor(data2)

## CI of partial correlations
data_cor_lower = cor(data2) - qnorm(0.95)*sqrt(data_cor_var)
data_cor_upper = cor(data2) + qnorm(0.95)*sqrt(data_cor_var)

data_cor_lower
data_cor_upper

### Think about how to use the quantile approach to construct
### a CI.

#### Exercise 1:
#### We will analyze the dataset 'quakes'. In particular, we focus on
#### the partial correlation between variable 'mag' and 'stations'.
#### (1) What is the value of partial correlation?
{data_ex1 = quakes[,4:5]
cor(data_ex1)
}
#### (2) Use the bootstrap to compute the distribution of the partial 
####     correlation. Attach a vertical line indicating the original value.
{data_ex1_cor = cor(data_ex1)[1,2]
n = nrow(data_ex1)
B = 10000
data_ex1_cor_BT = rep(NA, B)
for(i_BT in 1:B){
  w = sample(n,n,replace=T)
  data_ex1_BT = data_ex1[w,]
  data_ex1_cor_BT[i_BT] = cor(data_ex1_BT)[1,2]
}
hist(data_ex1_cor_BT, col="orchid")
abline(v=data_ex1_cor,lwd=6, col="blue")}
#### (3) Use the bootstrap to compute the variance and MSE of the partial
####     correlation.
{var(data_ex1_cor_BT)
mean((data_ex1_cor_BT-data_ex1_cor)^2)
}
#### (4) Use the bootstrap to construct a 95% CI of the partial correlation.
{data_ex1_cor - qnorm(0.95)*sd(data_ex1_cor_BT)
data_ex1_cor + qnorm(0.95)*sd(data_ex1_cor_BT)

quantile(data_ex1_cor_BT, c(0.05,0.95))
}

###                                           ###
### Part 2: Empirical Bootstrap in Regression ###
###                                           ###
head(data1)
fit = lm(waiting~eruptions, data=data1)

summary(fit)
summary(fit)$coefficients

fit_coeff = fit$coefficients
n = nrow(data1)

coeff_BT = matrix(NA, nrow=B, ncol=2)
for(i_BT in 1:B){
  w = sample(n,n,replace=T)
  data1_BT = data1[w,]
  fit_BT = lm(waiting~eruptions, data=data1_BT)
  coeff_BT[i_BT,] = fit_BT$coefficients
}
head(coeff_BT)
colnames(coeff_BT) = c("Intercept","Slope")
head(coeff_BT)

var(coeff_BT)

quantile(coeff_BT[,1],c(0.05,0.95))
quantile(coeff_BT[,'Intercept'],c(0.05,0.95))

quantile(coeff_BT[,'Slope'],c(0.05,0.95))

confint(fit,level = 0.9)
  
hist(coeff_BT[,'Intercept'], col="tan")
abline(v=fit_coeff[1], lwd=6, col="purple")

hist(coeff_BT[,'Slope'], col="palegreen")
abline(v=fit_coeff[2], lwd=6, col="brown")


plot(coeff_BT, cex=0.5)
points(x=fit_coeff[1], y=fit_coeff[2], cex=5, pch="+", col="red")

#### Exercise 2:
#### We will analyze the dataset 'quakes' again. In this case, we use
#### response Y = 'mag', and two covariates X1 = 'depth', X2 = 'stations'.
#### (1) What is the fitted value of the parameters?
{data_ex2 = quakes[,3:5]
fit_ex2 = lm(mag~depth+stations, data=data_ex2)
summary(fit_ex2)
coeff_ex2 = fit_ex2$coefficients
}
#### (2) Use the empirical bootstrap to estimate the distribution of the three 
####     parameters.
{n = nrow(data_ex2)
coeff_ex2_BT = matrix(NA, nrow=B, ncol=3)
for(i_BT in 1:B){
  w = sample(n,n,replace=T)
  data_ex2_BT = data_ex2[w,]
  fit_BT = lm(mag~depth+stations, data=data_ex2_BT)
  coeff_ex2_BT[i_BT,] = fit_BT$coefficients
}
head(coeff_ex2_BT)
hist(coeff_ex2_BT[,1], col="skyblue")
abline(v=coeff_ex2[1], lwd=6)
}
#### (3) What are the variance and MSE of these parameter estimates?
{diag(var(coeff_ex2_BT))
mean((coeff_ex2_BT[,1]-coeff_ex2[1])^2)
}
#### (4) What are 90% CIs of these parameters?
{quantile(coeff_ex2_BT[,1],c(0.05,0.95))
}
###                                     ###
### Part 3: Residual and Wild Bootstrap ###
###                                     ###
head(data1)
fit = lm(waiting~eruptions, data=data1)

fit$residuals
w = sample(n,n,replace=T)
fit$residuals[w]

predict(fit)

y_predict = predict(fit)
y_bt = y_predict+fit$residuals[w]

fit_coeff = fit$coefficients
n = nrow(data1)

coeff_BT_res = matrix(NA, nrow=B, ncol=2)
for(i_BT in 1:B){
  w = sample(n,n,replace=T)
  y_bt = y_predict+fit$residuals[w]
  data1_BT = data.frame(eruptions=data1$eruptions,
                        waiting=y_bt)
  fit_BT = lm(waiting~eruptions, data=data1_BT)
  coeff_BT_res[i_BT,] = fit_BT$coefficients
}
head(coeff_BT_res)
colnames(coeff_BT_res) = c("Intercept","Slope")

## results
var(coeff_BT_res)

quantile(coeff_BT_res[,'Intercept'],c(0.05,0.95))
quantile(coeff_BT_res[,'Slope'],c(0.05,0.95))

confint(fit,level = 0.9)

hist(coeff_BT_res[,'Intercept'], col="tan")
abline(v=fit_coeff[1], lwd=6, col="purple")

hist(coeff_BT_res[,'Slope'], col="palegreen")
abline(v=fit_coeff[2], lwd=6, col="brown")

plot(coeff_BT_res, cex=0.5)
points(x=fit_coeff[1], y=fit_coeff[2], cex=5, pch="+", col="red")


### Wild bootstrap
n= nrow(data1)
y_predict = predict(fit)
y_bt = y_predict+fit$residuals*rnorm(n)

fit_coeff = fit$coefficients
n = nrow(data1)

coeff_BT_wild = matrix(NA, nrow=B, ncol=2)
for(i_BT in 1:B){
  w = sample(n,n,replace=T)
  y_bt = y_predict+fit$residuals*rnorm(n)
  data1_BT = data.frame(eruptions=data1$eruptions,
                        waiting=y_bt)
  fit_BT = lm(waiting~eruptions, data=data1_BT)
  coeff_BT_wild[i_BT,] = fit_BT$coefficients
}
head(coeff_BT_wild)
colnames(coeff_BT_wild) = c("Intercept","Slope")

## results
var(coeff_BT_wild)

quantile(coeff_BT_wild[,'Intercept'],c(0.05,0.95))
quantile(coeff_BT_wild[,'Slope'],c(0.05,0.95))

confint(fit,level = 0.9)

hist(coeff_BT_wild[,'Intercept'], col="tan")
abline(v=fit_coeff[1], lwd=6, col="purple")

hist(coeff_BT_wild[,'Slope'], col="palegreen")
abline(v=fit_coeff[2], lwd=6, col="brown")

plot(coeff_BT_wild, cex=0.5)
points(x=fit_coeff[1], y=fit_coeff[2], cex=5, pch="+", col="red")


### comparison
var(coeff_BT_wild)
var(coeff_BT_res)
var(coeff_BT)
summary(fit)$coeff[,2]^2

#### Exercise 3:
#### We will analyze the dataset 'quakes' again. In this case, we use
#### response Y = 'mag', and two covariates X1 = 'depth', X2 = 'stations'.
#### (1) Use the residual bootstrap to show the distribution of the estimated
####     parameters. 
{data_ex2 = quakes[,3:5]
fit_ex2 = lm(mag~depth+stations, data=data_ex2)
coeff_ex2 = fit_ex2$coefficients
y_predict = predict(fit_ex2) 
n = nrow(data_ex2)
coeff_ex2_BT_emp = matrix(NA, nrow=B, ncol=3)
for(i_BT in 1:B){
  w = sample(n,n,replace=T)
  y_bt = y_predict+fit_ex2$residuals[w]
  data_ex2_BT = data.frame(depth=data_ex2$depth, stations=data_ex2$stations,
                        mag=y_bt)
  fit_BT = lm(mag~depth+stations, data=data_ex2_BT)
  coeff_ex2_BT_emp[i_BT,] = fit_BT$coefficients
}

hist(coeff_ex2_BT_emp[,1], col="tan")
abline(v=coeff_ex2[1],lwd=6, col="limegreen")
}
#### (2) Use the residual bootstrap to estimate the variance of the
####     estimated parameters.
{diag(var(coeff_ex2_BT_emp))
}
#### (3) Use the wild bootstrap to do the task (1) and (2) again.
{coeff_ex2_BT_wild = matrix(NA, nrow=B, ncol=3)
for(i_BT in 1:B){
  w = sample(n,n,replace=T)
  y_bt = y_predict+fit_ex2$residuals*rnorm(n)
  data_ex2_BT = data.frame(depth=data_ex2$depth, stations=data_ex2$stations,
                           mag=y_bt)
  fit_BT = lm(mag~depth+stations, data=data_ex2_BT)
  coeff_ex2_BT_wild[i_BT,] = fit_BT$coefficients
}

hist(coeff_ex2_BT_wild[,1], col="tan")
abline(v=coeff_ex2[1],lwd=6, col="limegreen")

diag(var(coeff_ex2_BT_wild))
}
#### (4) Use a matrix to compare the variance estimated by the three 
#####    bootstrap method and the square of s.e. from the summary() function.
{summary(fit_ex2)$coeff
cf_matrix = cbind(summary(fit_ex2)$coeff[,2]^2,diag(var(coeff_ex2_BT)),
                  diag(var(coeff_ex2_BT_emp)),diag(var(coeff_ex2_BT_wild)))
colnames(cf_matrix) = c("Square of se","Empirical","Residual","Wild")
cf_matrix
}
#### (5) Use a single plot to show the three bootstrap distributions of Intercept.
{boxplot(coeff_ex2_BT[,1], coeff_ex2_BT_emp[,1], coeff_ex2_BT_wild[,1],
        main="Intercept", col=c("skyblue","limegreen","orange"),
        names=c("Empirical","Residual","Wild"))
abline(h=coeff_ex2[1], lwd=6, col="purple")
  # you can easily change to other parameters
}

###                                               ###
### Part 4: Bootstrapping the Logistic Regression ###
###                                               ###
D = read.csv("binary.csv")

data3 = D[,c(1,3)]
head(data3)
fit_logistic = glm(admit ~ gpa, data=data3, 
                   family = "binomial")
summary(fit_logistic)

fit_coeff = fit_logistic$coefficients

n = nrow(data3)
predict(fit_logistic, type="response")

Y_bt = rbinom(n, size=1, prob = predict(fit_logistic,type="response"))
Y_bt


## parametric bootstrap
coeff_BT_logistic = matrix(NA, nrow=B, ncol=2)
for(i_BT in 1:B){
  y_bt = rbinom(n, size=1, prob = predict(fit_logistic,type="response"))
  data3_BT = data.frame(admit = y_bt,gpa=data3$gpa)
  fit_BT = glm(admit ~ gpa, data=data3_BT, 
               family = "binomial")
  coeff_BT_logistic[i_BT,] = fit_BT$coefficients
}
head(coeff_BT_logistic)
colnames(coeff_BT_logistic) = c("Intercept","Slope")


## estimate
var(coeff_BT_logistic)

quantile(coeff_BT_logistic[,'Intercept'],c(0.05,0.95))
quantile(coeff_BT_logistic[,'Slope'],c(0.05,0.95))

confint(fit_logistic,level = 0.9)

hist(coeff_BT_logistic[,'Intercept'], col="tan")
abline(v=fit_coeff[1], lwd=6, col="purple")

hist(coeff_BT_logistic[,'Slope'], col="palegreen")
abline(v=fit_coeff[2], lwd=6, col="brown")

plot(coeff_BT_logistic, cex=0.5)
points(x=fit_coeff[1], y=fit_coeff[2], cex=5, pch="+", col="red")


### Empirical bootstrap
n = nrow(data3)
coeff_BT_lemp = matrix(NA, nrow=B, ncol=2)
for(i_BT in 1:B){
  w = sample(n,n,replace = T)
  data3_BT = data3[w,]
  fit_BT = glm(admit ~ gpa, data=data3_BT, 
               family = "binomial")
  coeff_BT_lemp[i_BT,] = fit_BT$coefficients
}
head(coeff_BT_lemp)
colnames(coeff_BT_lemp) = c("Intercept","Slope")


## estimate
var(coeff_BT_lemp)

quantile(coeff_BT_lemp[,'Intercept'],c(0.05,0.95))
quantile(coeff_BT_lemp[,'Slope'],c(0.05,0.95))

confint(fit_logistic,level = 0.9)

hist(coeff_BT_lemp[,'Intercept'], col="tan")
abline(v=fit_coeff[1], lwd=6, col="purple")

hist(coeff_BT_lemp[,'Slope'], col="palegreen")
abline(v=fit_coeff[2], lwd=6, col="brown")

plot(coeff_BT_lemp, cex=0.5)
points(x=fit_coeff[1], y=fit_coeff[2], cex=5, pch="+", col="red")

#### Exercise 4:
#### Use the data as part 4 but now focus on Y='admit' and X='gre'.
#### (1) Fit a logistic regression. What are the fitted coefficients?
{data_ex4 = D[,c(1,2)]
fit_ex4 = glm(admit ~ gre, data=data_ex4, 
                   family = "binomial")
fit_ex4$coefficients

fit_coeff = fit_ex4$coefficients
}
#### (2) Use the parametric bootstrap to show the distribution of each 
####     coefficient.
{n = nrow(data_ex4)
coeff_BT_logistic = matrix(NA, nrow=B, ncol=2)
for(i_BT in 1:B){
  y_bt = rbinom(n, size=1, prob = predict(fit_ex4,type="response"))
  data_ex4_BT = data.frame(admit = y_bt,gre=data_ex4$gre)
  fit_BT = glm(admit ~ gre, data=data_ex4_BT, 
               family = "binomial")
  coeff_BT_logistic[i_BT,] = fit_BT$coefficients
}
head(coeff_BT_logistic)

hist(coeff_BT_logistic[,1], col="yellow")
abline(v=fit_coeff[1],lwd=6,col="dodgerblue")
}
#### (3) Use the empirical boostrap to show the distribution of each 
####     coefficient. 
{n = nrow(data_ex4)
coeff_BT_lemp = matrix(NA, nrow=B, ncol=2)
for(i_BT in 1:B){
  w = sample(n,n,replace=T)
  data_ex4_BT = data_ex4[w,]
  fit_BT = glm(admit ~ gre, data=data_ex4_BT, 
               family = "binomial")
  coeff_BT_lemp[i_BT,] = fit_BT$coefficients
}
head(coeff_BT_lemp)

hist(coeff_BT_lemp[,1], col="lightblue")
abline(v=fit_coeff[1],lwd=6,col="red")
}
#### (4) Use a matrix to compare the variance of each coefficients from 
####     square of s.e., parametric bootstrap, and empirical bootstrap.
{summary(fit_ex4)$coeff
cf_matrix = cbind(summary(fit_ex4)$coeff[,2]^2,diag(var(coeff_BT_logistic)),
                  diag(var(coeff_BT_lemp)))
colnames(cf_matrix) = c("Square of se","Parametric","Empirical")
cf_matrix
}

library(xtable)

xtable(var(coeff_BT_logistic))
