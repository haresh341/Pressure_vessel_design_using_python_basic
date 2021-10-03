from tkinter import *
import math

# root window
root = Tk()

# title
root.title("Pressure Vessel Design")

## step 1 -  basic wind speed
wind_speed_data = {"Ahmedabad": 47,
                   "Calcutta": 50,
                   "Surat": 44,
                   "Mysore": 33,
                   "Bangalore": 33,
                   "Chennai": 50,
                   "Chandigarh": 47,
                   "Delhi NCR": 47,
                   "Hyderabad": 44,
                   "Jaipur": 47,
                   "Mumbai": 44,
                   "Pune": 39,
                   "Nagpur": 44,
                   "Nashik": 39,
                   }
seismic_intensity_data = {"Low": 0.1,
                          "Moderate": 0.16,
                          "Severe": 0.24,
                          "Very Severe": 0.26,
                          }
building_type_data = {"Default": 1,
                      "Important Building": 1.5
                      }
building_frame_type_data = {"Ordinary RC moment-resitng frame(OMRF)": 3,
                            "Special RC moment-resisting frame(SMRF)": 5,
                            "Steel frame with Concentric braces": 4,
                            "Steel frame with Eccentric braces": 5,
                            "Steel moment resisting frame designed as per SP 6(6)": 5
                            }
young_modulus_data = {"ASTM A228": 210,
                      "ASTM A36": 200,
                      "AISI 1010": 205,
                      "AISI 1018": 205,
                      "AISI 1020": 205,
                      "AISI 1025": 200,
                      "AISI 1040": 200,
                      "AISI 1045": 205,
                      "Grade 316": 193,
                      "Grade 405": 200,
                      "Grade 440c": 200,
                      "Aluminium": 69,
                      "Copper": 117,
                      "Brass": 120,
                      "Iron": 170,
                      "Nickel": 210,
                      "Steel": 200,

                      }
location_city = StringVar()
location_city.set("Choose City")

# dropdwon menu for location
frame_step_one = Frame(root, highlightbackground="black", highlightthickness=2)
frame_step_one.grid(row=0, column=0, ipadx=20, ipady=10, padx=20, pady=10)
step_one_label = Label(frame_step_one, text="Wind load Caclulation")
step_one_label.grid(row=0, column=0)

# location label
location_label = Label(frame_step_one, text="Choose location")
location_dropdown = OptionMenu(frame_step_one, location_city, *wind_speed_data.keys())
location_label.grid(row=1, column=0, padx=30, pady=10)
location_dropdown.grid(row=1, column=1, padx=30, pady=10)

# get wind speed from chosen city location
wind_speed = IntVar()
wind_speed_string = StringVar()


# get wind speed
def get_wind_speed(*args):
    wind_speed = 0
    for city, _wind_speed in wind_speed_data.items():
        if city == location_city.get():
            wind_speed = _wind_speed
            print(_wind_speed)
            wind_speed_string = str(wind_speed) + "m/s"

            wind_speed_value_label = Label(frame_step_one, text=wind_speed_string)
            wind_speed_value_label.grid(row=2, column=1, padx=30, pady=10)
            # step 2.Calculating design wind speed


location_city.trace('w', get_wind_speed)

# print(wind_speed)
# wind speed label
wind_speed_label = Label(frame_step_one, text="Wind Speed")
wind_speed_label.grid(row=2, column=0, padx=30, pady=10)

# risk factor
class_of_structures = {}

## step 2 - calculate design wind speed

risk_level_k1 = 1
terrain_structure_k2 = 1
local_topography_k3 = 1

# risk level(k1) label
risk_level_k1_label = Label(frame_step_one, text="Risk Level(k1)")
risk_level_k1_label.grid(row=3, column=0, padx=30, pady=10)
risk_level_k1_value_label = Label(frame_step_one, text=wind_speed_string)
risk_level_k1_value_label.grid(row=3, column=1, padx=30, pady=10)

# terrain structure(k2) label
terrain_structure_k2_label = Label(frame_step_one, text="Terrain Structure(k2)")
terrain_structure_k2_label.grid(row=4, column=0, padx=30, pady=10)
terrain_structure_k2_value_label = Label(frame_step_one, text=wind_speed_string)
terrain_structure_k2_value_label.grid(row=4, column=1, padx=30, pady=10)

# local topography(k3) label
local_topography_k3_label = Label(frame_step_one, text="Local Topgraphy(k3)")
local_topography_k3_label.grid(row=5, column=0, padx=30, pady=10)
local_topography_k3_value_label = Label(frame_step_one, text=wind_speed_string)
local_topography_k3_value_label.grid(row=5, column=1, padx=30, pady=10)

# design wind speed calculation
basic_wind_speed_vb = wind_speed.get()
design_wind_speed_vz = basic_wind_speed_vb * risk_level_k1 * terrain_structure_k2 * local_topography_k3;

# design wind speed label
design_wind_speed_label = Label(frame_step_one, text="Design Wind Speed")
design_wind_speed_label.grid(row=6, column=0, padx=30, pady=10)
design_wind_speed_value_label = Label(frame_step_one, text=wind_speed_string)
design_wind_speed_value_label.grid(row=6, column=1, padx=30, pady=10)

## step 3 - calculate design wind pressure
design_wind_pressure_pz = 0.6 * design_wind_speed_vz * design_wind_speed_vz

# design wind pressure label
design_wind_pressure_pz_label = Label(frame_step_one, text="Design Wind Pressure")
design_wind_pressure_pz_label.grid(row=7, column=0, padx=30, pady=10)
design_wind_pressure_pz_value_label = Label(frame_step_one, text=wind_speed_string)
design_wind_pressure_pz_value_label.grid(row=7, column=1, padx=30, pady=10)

## step 4 - calculate equivalent wind diameter

# calculation
insulated_od_of_column = 1;
equivalent_wind_diameter_de = 1.2 * insulated_od_of_column

# calculate shape factor
shape_factor_cf = 0.7

# insulated od of column label
insulated_od_of_column_label = Label(frame_step_one, text="Insulated od of column")
insulated_od_of_column_label.grid(row=8, column=0, padx=30, pady=10)
insulated_od_of_column_value_label = Label(frame_step_one, text=wind_speed_string)
insulated_od_of_column_value_label.grid(row=8, column=1, padx=30, pady=10)

# equivalent wind diameter label
equivalent_wind_diameter_de_label = Label(frame_step_one, text="Equivalent wind diameter")
equivalent_wind_diameter_de_label.grid(row=9, column=0, padx=30, pady=10)
equivalent_wind_diameter_de_value_label = Label(frame_step_one, text=wind_speed_string)
equivalent_wind_diameter_de_value_label.grid(row=9, column=1, padx=30, pady=10)

# equivalent wind diameter label
shape_factor_cf_label = Label(frame_step_one, text="shape factor")
shape_factor_cf_label.grid(row=10, column=0, padx=30, pady=10)
shape_factor_cf_value_label = Label(frame_step_one, text=str(shape_factor_cf))
shape_factor_cf_value_label.grid(row=10, column=1, padx=30, pady=10)

## step 5 - calculate projected area
# calculation
length_of_section_under_consideration_l = 1
projected_area_a = shape_factor_cf * length_of_section_under_consideration_l * equivalent_wind_diameter_de

# projected area label
projected_area_a_label = Label(frame_step_one, text="Projected area")
projected_area_a_label.grid(row=11, column=0, padx=30, pady=10)
projected_area_a_value_label = Label(frame_step_one, text=str(shape_factor_cf))
projected_area_a_value_label.grid(row=11, column=1, padx=30, pady=10)

# calculate wind load
wind_load_fv = design_wind_pressure_pz * projected_area_a

# wind load label
wind_load_fv_label = Label(frame_step_one, text="Wind load")
wind_load_fv_label.grid(row=12, column=0, padx=30, pady=10)
wind_load_fv_value_label = Label(frame_step_one, text=str(shape_factor_cf))
wind_load_fv_value_label.grid(row=12, column=1, padx=30, pady=10)

""" calculation of seismic loads """

# The vibration of the vessel is same as vibration of the cantilever. The relationship for natural frequency of such a system is derived by considering the motion of a weight suspended on the end of a completely elastic string.
column_weight_w = 1
column_height_h = 1
gravitational_accelaration_g = 9.80665
young_modulus_e = 1
interia_i = 1
time_period_t = (math.pi / 3.53) * math.sqrt(
    (column_weight_w * column_height_h ** 3) / young_modulus_e * gravitational_accelaration_g * interia_i)

## step 1 Seismic load calculation
frame_step_seismic_one = Frame(root, highlightbackground="black", highlightthickness=2)
frame_step_seismic_one.grid(row=0, column=1, ipadx=20, ipady=10, padx=20, pady=10)
step_seismic_one_label = Label(frame_step_seismic_one, text="Seismic load calculation")
step_seismic_one_label.grid(row=0, column=0)

# taking input label
column_weight_w_label = Label(frame_step_seismic_one, text="Column weight")
column_weight_w_label.grid(row=1, column=0, padx=30, pady=10)

column_height_h_label = Label(frame_step_seismic_one, text="Column height")
column_height_h_label.grid(row=2, column=0, padx=30, pady=10)

young_modulus_e_label = Label(frame_step_seismic_one, text="Young modulus")
young_modulus_e_label.grid(row=3, column=0, padx=30, pady=10)

interia_i_label = Label(frame_step_seismic_one, text="Interia")
interia_i_label.grid(row=4, column=0, padx=30, pady=10);

# taking input entry

column_weight_w_entry = Entry(frame_step_seismic_one)
column_weight_w_entry.grid(row=1, column=1, padx=30, pady=10)

column_height_h_entry = Entry(frame_step_seismic_one)
column_height_h_entry.grid(row=2, column=1, padx=30, pady=10)

# young modulus dropdown

young_modulus = StringVar()
young_modulus.set("Choose Metal")
young_modulus_e_dropdown = OptionMenu(frame_step_seismic_one,young_modulus,*young_modulus_data.keys())
young_modulus_e_dropdown.grid(row=3, column=1, padx=30, pady=10)

interia_i_entry = Entry(frame_step_seismic_one)
interia_i_entry.grid(row=4, column=1, padx=30, pady=10)

# time period label
time_period_t_label = Label(frame_step_seismic_one, text="Time period")
time_period_t_label.grid(row=5, column=0, padx=30, pady=10)
time_period_t_value_label = Label(frame_step_seismic_one, text=str(shape_factor_cf))
time_period_t_value_label.grid(row=5, column=1, padx=30, pady=10)

seismic_coefficient_c = 1
total_shear_load_cw = 1
position_x = column_height_h * 2 / 3

# taking input label
total_shear_load_cw_label = Label(frame_step_seismic_one, text="Total shear load")
total_shear_load_cw_label.grid(row=6, column=0, padx=30, pady=10)

total_shear_load_cw_entry = Entry(frame_step_seismic_one)
total_shear_load_cw_entry.grid(row=6, column=1, padx=30, pady=10)

# The shear load, Vs at any horizontal plane in the tower X meter down from top is given by

shear_load_vs_at_position_x = total_shear_load_cw * position_x * (
        2 * column_height_h - position_x) / column_height_h ** 2

# The bending moment Ms at any plane X resulting from the shear force above plane X is given by

bending_moment_ms_at_position_x = total_shear_load_cw * position_x ** 2 * (3 * column_height_h - position_x) / (
        3 * column_height_h ** 2)

# shear load label
shear_load_vs_at_position_x_label = Label(frame_step_seismic_one, text="Shear load(Vs)")
shear_load_vs_at_position_x_label.grid(row=7, column=0, padx=30, pady=10)
shear_load_vs_at_position_x_value_label = Label(frame_step_seismic_one, text=str(shape_factor_cf))
shear_load_vs_at_position_x_value_label.grid(row=7, column=1, padx=30, pady=10)

# bending moment label
bending_moment_ms_at_position_x_label = Label(frame_step_seismic_one, text="Bending moment(Ms)")
bending_moment_ms_at_position_x_label.grid(row=8, column=0, padx=30, pady=10)
bending_moment_ms_at_position_x_value_label = Label(frame_step_seismic_one, text=str(shape_factor_cf))
bending_moment_ms_at_position_x_value_label.grid(row=8, column=1, padx=30, pady=10)

# z factor dropdown
seismic_intensity = StringVar()
seismic_intensity.set("Choose Intensity")

# seismic intensity label
seismic_intensity_label = Label(frame_step_seismic_one, text="Seismic intensity")
seismic_intensity_dropdown = OptionMenu(frame_step_seismic_one, seismic_intensity, *seismic_intensity_data.keys())
seismic_intensity_label.grid(row=9, column=0, padx=30, pady=10)
seismic_intensity_dropdown.grid(row=9, column=1, padx=30, pady=10)

# i factor dropdown
building_type = StringVar()
building_type.set("Default")

# seismic intensity label
building_type_label = Label(frame_step_seismic_one, text="Building type")
building_type_dropdown = OptionMenu(frame_step_seismic_one, building_type, *building_type_data.keys())
building_type_label.grid(row=10, column=0, padx=30, pady=10)
building_type_dropdown.grid(row=10, column=1, padx=30, pady=10)

# r factor dropdown
building_frame_type = StringVar()
building_frame_type.set("Choose Building Frame type")

# seismic intensity label
building_frame_type_label = Label(frame_step_seismic_one, text="Building frame type")
building_frame_type_dropdown = OptionMenu(frame_step_seismic_one, building_frame_type, *building_frame_type_data.keys())
building_frame_type_label.grid(row=11, column=0, padx=30, pady=10)
building_frame_type_dropdown.grid(row=11, column=1, padx=30, pady=10)

zone_factor_z = 1
importance_factor_i = 1
response_factor_r = 1

# calculating Average response acceleration coefficient (Sa/g)
soil_types = ['Hard', 'Medium', 'Soft']
soil_type = StringVar()
soil_type.set("Choose soil type")

# seismic intensity label
soil_types_label = Label(frame_step_seismic_one, text="Soil type")
soil_types_dropdown = OptionMenu(frame_step_seismic_one, soil_type, *soil_types)
soil_types_label.grid(row=12, column=0, padx=30, pady=10)
soil_types_dropdown.grid(row=12, column=1, padx=30, pady=10)

average_response_accelaration_coefficient_sa_by_g = float()

if soil_type == soil_types[0]:
    if 0 <= time_period_t <= 0.1:
        average_response_accelaration_coefficient_sa_by_g = 1 + 15 * time_period_t
    elif 0.1 < time_period_t <= 0.4:
        average_response_accelaration_coefficient_sa_by_g = 2.5
    else:
        average_response_accelaration_coefficient_sa_by_g = 1 / time_period_t
elif soil_type == soil_types[1]:
    if 0 <= time_period_t <= 0.1:
        average_response_accelaration_coefficient_sa_by_g = 1 + 15 * time_period_t
    elif 0.1 < time_period_t <= 0.55:
        average_response_accelaration_coefficient_sa_by_g = 2.5
    else:
        average_response_accelaration_coefficient_sa_by_g = 1.36 / time_period_t
elif soil_type == soil_types[2]:
    if 0 <= time_period_t <= 0.1:
        average_response_accelaration_coefficient_sa_by_g = 1 + 15 * time_period_t
    elif 0.1 < time_period_t <= 0.67:
        average_response_accelaration_coefficient_sa_by_g = 2.5
    else:
        average_response_accelaration_coefficient_sa_by_g = 1.67 / time_period_t

horizontal_seismic_coefficient_ah = zone_factor_z * importance_factor_i * average_response_accelaration_coefficient_sa_by_g / (
        2 * response_factor_r)

# Calculate Design Seismic Base Shear(VB)
design_seismic_base_shear_vb = horizontal_seismic_coefficient_ah * column_weight_w

# Design Seismic Base Shear(VB) label
design_seismic_base_shear_vb_label = Label(frame_step_seismic_one, text="Shear load(Vs)")
design_seismic_base_shear_vb_label.grid(row=13, column=0, padx=30, pady=10)
design_seismic_base_shear_vb_value_label = Label(frame_step_seismic_one, text=str(shape_factor_cf))
design_seismic_base_shear_vb_value_label.grid(row=13, column=1, padx=30, pady=10)

# mainlooop
root.mainloop()
