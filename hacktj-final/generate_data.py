import random
import statistics
import pandas as pd

with open('liver.txt', 'r') as file:
    # Read the content of the file
    liver_data = file.read()
    
with open('iron.txt', 'r') as file:
    # Read the content of the file
    iron_data = file.read()
    
with open('bmi.txt', 'r') as file:
    # Read the content of the file
    bmi_data = file.read()    



# Step 1: Extract SNPs and their weights into a dictionary
def extract_snps_and_weights(file_content):
    snp_dict = {}
    lines = file_content.split('\n')
    # print("LINES")
    # print(lines)
    for line in lines[1:]:  # Skip the first line (header)
        if line.startswith('rs'):
            parts = line.split()
            rs_id = parts[0]
            effect_weight = float(parts[5])
            snp_dict[rs_id] = effect_weight
    return snp_dict

# Step 2: Generate data for 20 people
def generate_person_data(snp_dict):
    people_data = []
    for num in range(20):
        person_data = {}
        for rs_id in snp_dict:
            # Randomly assign 0, 1, or 2 effective alleles for each SNP
            person_data[rs_id] = random.randint(0, 2)
        people_data.append(person_data)
    return people_data


def generate_final_csv(generated_csv, snp_dict): 
    
    df = pd.DataFrame(generated_csv)
    PGS_list = []
    for person in generated_csv: 
        pgs_score = 0 
        for snp in person: 
            pgs_score+=(snp_dict[snp] * person[snp])
        PGS_list.append(pgs_score)
    
    average_PGS = statistics.mean(PGS_list)
        
    PGS_high_low = []
    
    for index, person in enumerate(generated_csv): 
        if PGS_list[index] < average_PGS: 
            PGS_high_low.append("LOW")
        else: 
            PGS_high_low.append("HIGH")
            
    df["phenotype"] = PGS_high_low   
        
    return df
            

processed_liver = extract_snps_and_weights(liver_data)
processed_bmi = extract_snps_and_weights(bmi_data)
processed_iron = extract_snps_and_weights(iron_data)


print(processed_liver)

generated_liver = generate_person_data(processed_liver)
generated_bmi = generate_person_data(processed_bmi)
generated_iron = generate_person_data(processed_iron)

pgs_liver  = generate_final_csv(generated_liver, processed_liver) 

pgs_bmi  = generate_final_csv(generated_bmi, processed_bmi) 

pgs_iron  = generate_final_csv(generated_iron, processed_iron) 


# Save the DataFrame to CSV
pgs_liver.to_csv("liver_generated_data.csv", index=False) 

pgs_bmi.to_csv("bmi_generated_data.csv", index=False) 

pgs_iron.to_csv("iron_generated_data.csv", index=False) 


