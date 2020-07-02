print("How many shop hours did you have this week?", end=' ')
shophours = int(input())

print("How many install hours did you have this week?", end=' ')
installhours = int(input())
#this line does work the way I would like it to. I would like it to multiply and sum up the entire paycheck by assigning the input value to the variable.
print(f"So if you put in {shophours} shop hours and {installhours} install hours then your paycheck should be", (int(shophours)*18 + int(installhours)*28)*.85)
