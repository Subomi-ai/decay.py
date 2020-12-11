import matplotlib.pyplot as plt

# Explain the purpose of the program
print("This is a program to plot the decay rate")

# Ask the user for the initial concentration A
initial_concentration =  int(input("Please enter initial concentration"))

# Ask the user for the decay rate
decay_rate = float(input("Please enter the decay rate"))

# Ask the user for the time taken t
time_taken = int(input("Please enter time taken"))

remaining_concentration= initial_concentration
print("Time taken\t initial concentration\t No of bacteria decayed\t remaining concentration")
time_in_seconds=[]
concentration=[]
for i in range(time_taken+1):
    initial_concentration = round(remaining_concentration)
    number_of_bacteria_decayed = round(initial_concentration * decay_rate)
    remaining_concentration = round(initial_concentration - number_of_bacteria_decayed)
    print(i,"\t\t", initial_concentration,"\t\t", number_of_bacteria_decayed, "\t\t\t", remaining_concentration)
    time_in_seconds.append(i)
    concentration.append(initial_concentration)
plt.plot(time_in_seconds,concentration)
plt.xlabel("time_taken")
plt.ylabel("concentration")
plt.title("decay rate")
plt.show()
