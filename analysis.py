

def average_age(ages):
    return sum(ages)/len(ages)

def majority_individuals(regions):
    return max(regions)

def smokers_vs_nonsmokers_costs(smoker_status, costs):
    smokers_count = 0
    non_smokers_count = 0
    smokers_cost = 0
    non_smokers_cost = 0
    for status in range(len(smoker_status)):
        if smoker_status[status] == 'yes':
            smokers_count += 1
            smokers_cost += costs[status]
        else:
            non_smokers_count += 1
            non_smokers_cost += costs[status]
    
    smokers_average = smokers_cost / smokers_count
    non_smokers_average = non_smokers_cost / non_smokers_count
    
    return smokers_average, non_smokers_average, smokers_average - non_smokers_average

def age_of_parents(ages, num_children):
    ages_sum = 0
    ages_count = 0
    for i in range(len(num_children)):
        if num_children[i] > 0:
            ages_sum += ages[i]
            ages_count += 1
            
    return ages_sum / ages_count