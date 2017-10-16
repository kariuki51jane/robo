import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Generate universe variables
#   * Quality and service on subjective ranges [0, 10]
#   * Tip has a range of [0, 25] in units of percentage points


distance=80
energy=0
temperature=30




x_distance = np.arange(0, 300, 1)
x_energy = np.arange(0, 100, 1)
x_temperature=np.arange(20,30,1)
x_speed  = np.arange(0, 1, 0.1)

# Generate fuzzy membership functions for distance
distance_lo = fuzz.trimf(x_distance, [0, 0, 150])
distance_md = fuzz.trimf(x_distance, [0, 150, 300])
distance_hi = fuzz.trimf(x_distance, [150, 300, 300])

energy_lo = fuzz.trimf(x_energy, [0, 0, 50])
energy_md = fuzz.trimf(x_energy, [0,50, 100])
energy_hi = fuzz.trimf(x_energy, [50, 100, 100])

temperature_lo = fuzz.trimf(x_temperature, [20, 20, 25])
temperature_md = fuzz.trimf(x_temperature, [20, 25, 30])
temperature_hi = fuzz.trimf(x_temperature, [25, 30, 30])

speed_lo = fuzz.trimf(x_speed, [0, 0, 0.5])
speed_md = fuzz.trimf(x_speed, [0, 0.5, 1])
speed_hi = fuzz.trimf(x_speed, [0.5, 1, 1])

# Visualize these universes and membership functions
fig, (ax0, ax1, ax2,ax3) = plt.subplots(nrows=4, figsize=(8, 9))

ax0.plot(x_distance, distance_lo, 'b', linewidth=1.5, label='Long')
ax0.plot(x_distance, distance_md, 'g', linewidth=1.5, label='Mid')
ax0.plot(x_distance, distance_hi, 'r', linewidth=1.5, label='Short')
ax0.set_title('Distance to Travel')
ax0.legend()

ax1.plot(x_energy, energy_lo, 'b', linewidth=1.5, label='Low')
ax1.plot(x_energy, energy_md, 'g', linewidth=1.5, label='Medium')
ax1.plot(x_energy, energy_hi, 'r', linewidth=1.5, label='High')
ax1.set_title('Energy')
ax1.legend()

ax2.plot(x_temperature, temperature_lo, 'b', linewidth=1.5, label='Low')
ax2.plot(x_temperature, temperature_md, 'g', linewidth=1.5, label='Medium')
ax2.plot(x_temperature, temperature_hi, 'r', linewidth=1.5, label='High')
ax2.set_title('Temperature')
ax2.legend()


ax3.plot(x_speed, speed_lo, 'b', linewidth=1.5, label='Low')
ax3.plot(x_speed, speed_md, 'g', linewidth=1.5, label='Medium')
ax3.plot(x_speed, speed_hi, 'r', linewidth=1.5, label='High')
ax3.set_title('Speed Altering Factor')
ax3.legend()

# Turn off top/right axes
#for ax in (ax0, ax1, ax2,ax3):
#    ax.spines['top'].set_visible(False)
#    ax.spines['right'].set_visible(False)
#    ax.get_xaxis().tick_bottom()
#    ax.get_yaxis().tick_left()

#plt.tight_layout()




#Rule Application

# We need the activation of our fuzzy membership functions at these values.
# The exact values 6.5 and 9.8 do not exist on our universes...
# This is what fuzz.interp_membership exists for!

#distance
distance_level_lo = fuzz.interp_membership(x_distance, distance_lo, distance)
distance_level_md = fuzz.interp_membership(x_distance, distance_md, distance)
distance_level_hi = fuzz.interp_membership(x_distance, distance_hi, distance)


#energy
energy_level_lo = fuzz.interp_membership(x_energy, energy_lo, energy)
energy_level_md = fuzz.interp_membership(x_energy, energy_md, energy)
energy_level_hi = fuzz.interp_membership(x_energy, energy_hi, energy)


#temperature
temperature_level_lo = fuzz.interp_membership(x_temperature, temperature_lo, temperature)
temperature_level_md = fuzz.interp_membership(x_temperature, temperature_md, temperature)
temperature_level_hi = fuzz.interp_membership(x_temperature, temperature_hi, temperature)


#if energy level is medium and distance is high and temperature is medium speed medium
active_rule1 = max(distance_level_hi,energy_level_md,temperature_level_md)
speed_activation_md = np.fmin(active_rule1, speed_md)  


#if energy level is medium and distance is low and temperature is medium speed high
active_rule2 = max(distance_level_lo,energy_level_md,temperature_level_md)
speed_activation_hi = np.fmin(active_rule2, speed_hi) 

#if energy level is medium and distance is high and temperature is medium speed medium
active_rule3 = max(distance_level_hi,energy_level_lo,temperature_level_md)
speed_activation_lo = np.fmin(active_rule3, speed_lo) 



speed0 = np.zeros_like(x_speed)





# Visualize this
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.fill_between(x_speed, speed0, speed_activation_lo, facecolor='b', alpha=0.7)
ax0.plot(x_speed, speed_lo, 'b', linewidth=0.5, linestyle='--', )
ax0.fill_between(x_speed, speed0, speed_activation_md, facecolor='g', alpha=0.7)
ax0.plot(x_speed, speed_md, 'g', linewidth=0.5, linestyle='--')
ax0.fill_between(x_speed, speed0, speed_activation_hi, facecolor='r', alpha=0.7)
ax0.plot(x_speed, speed_hi, 'r', linewidth=0.5, linestyle='--')
ax0.set_title('Output membership activity')



# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()




#defuzzufication



# Aggregate all three output membership functions together
aggregated = np.fmax(speed_activation_lo,np.fmax(speed_activation_md, speed_activation_hi))

# Calculate defuzzified result
speed = fuzz.defuzz(x_speed, aggregated, 'centroid')
speed_activation = fuzz.interp_membership(x_speed, aggregated, speed)  # for plot

# Visualize this
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(x_speed, speed_lo, 'b', linewidth=0.5, linestyle='--', )
ax0.plot(x_speed, speed_md, 'g', linewidth=0.5, linestyle='--')
ax0.plot(x_speed, speed_hi, 'r', linewidth=0.5, linestyle='--')
ax0.fill_between(x_speed, speed0, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([speed, speed], [0, speed_activation], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Aggregated membership and result (line)')

# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

plt.show()


