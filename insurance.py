import csv
import analysis

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

with open("resources/insurance.csv") as insurance_file:
    insurance_dict = csv.DictReader(insurance_file)
    for row in insurance_dict:
        ages.append(int(row['age']))
        sexes.append(row['sex'])
        bmis.append(float(row['bmi']))
        num_children.append(int(row['children']))
        smoker_statuses.append(row['smoker'])
        regions.append(row['region'])
        insurance_charges.append(float(row['charges']))
        

def analyze():
    print("The average age of a person getting a U.S. Medical Insurance is", analysis.average_age(ages), ".")
    print("The majority of individual getting a U.S.Medical Insurance is from", analysis.majority_individuals(regions), "region.")
    smokers_average, non_smokers_average, difference = analysis.smokers_vs_nonsmokers_costs(smoker_statuses, insurance_charges)
    print("The average charges for an insurance of a smoker are", smokers_average)
    print("The average charges for an insurance of a non-smoker are", non_smokers_average)
    print("On average, a non-smoker pays", difference, "less than a smoker for availing a U.S.Medical Insurance")
    print("The average age of people having atleast 1 child buying U.S.Medical Insurance is:", analysis.age_of_parents(ages, num_children))
    

analyze()