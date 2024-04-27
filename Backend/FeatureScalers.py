import math
import Donor as Donor
import Recipient as Recipient


'''
A triadic function that calulates a score that reflects how compatible a user and donor would be considering age 
of both donor and recipient as well as any ailments the donor may possess

The function accepts the following parameters
*The nature of the ailment of the donor  if any
*The age of the donor
*The age of the recipient

Metricises the Degree of the ailment of the donor 
The Ailment would ultimately fall in one of the highlighted categories which are associated with Various Scores
The Scores capture the Nature of the Ailment the Donor suffers from and descend as they become more serious 




'''

def calculate_ailment_score(recipient_nature_of_ailment, donor_age, recipient_age):

  # Define a dictionary of nature of ailment scores (case-insensitive)
  ailment_nature_scores = {
      'genetic': 10,
      'congenital': 8,
      'acquired': 6,
      'autoimmune': 4,
      'malignant': 2,
      'N/A': 0
  }

  # Define age difference thresholds and scores
  age_diff_thresholds = [5, 10, 15, 20]
  age_diff_scores = [10, 8, 6, 4, 2]

  # Calculate age difference between donor and recipient
  age_difference = abs(donor_age - recipient_age)

  # Assign score based on the lowercased nature of ailment
  nature_of_ailment_score = ailment_nature_scores.get(recipient_nature_of_ailment.lower(), 0)

  # Calculate a combined score based on ailment nature and age difference
  # Here, a higher score signifies better compatibility

  # Option 1: Weighted Average (adjust weights as needed)
  combined_score = (0.7 * nature_of_ailment_score) + (0.3 * age_diff_scores[min(len(age_diff_scores) - 1, age_difference // age_diff_thresholds[0])])

  
  return combined_score
    
    



'''
A multiadic function that calculates a BMI compatability metric between a potential donor and recipient
The function accpets the following as parameters

The function makes use of a helper function calculate_bmi to find the BMI value of each person in the pair
* The height and weight of the recipient
* The height and weight of the  propsective Donor


'''

def calculate_bmi(height, weight):
  # Convert height from cm to meters
  height_m = height / 100

  # Calculate BMI using the formula: weight (kg) / (height (m))^2
  bmi = weight / (height_m ** 2)
  return bmi

def calculate_bmi_score(recipient_height, recipient_weight, donor_height, donor_weight):
  # Calculate BMI for recipient and donor
  recipient_bmi = calculate_bmi(recipient_height, recipient_weight)
  donor_bmi = calculate_bmi(donor_height, donor_weight)

  # Define a threshold for acceptable BMI difference (adjust as needed)
  acceptable_diff = 2

  # Calculate the absolute difference between BMIs
  bmi_diff = abs(recipient_bmi - donor_bmi)

  # Score penalty based on the difference from the ideal (0 difference)
  score_penalty = min(bmi_diff / acceptable_diff, 1)  # Clamp to 1 for large differences

  # Assign a score based on the penalty (0 = perfect match, 1 = high difference)
  bmi_score = (1 - score_penalty) * 10

  return bmi_score



'''
A diadic function that produces a metric that reflects the degree of compatability of
potential donors and recipients based on HLA (Human Leukocyte Antigen)

The function accepts the following  as parameters :

* The HLA Typing of the donor
* The HLA Typing of the recipient

'''

def calculate_hla_score(recipient_hla, donor_hla):
    # Check if input strings are None or empty
    if recipient_hla is None or donor_hla is None or not recipient_hla or not donor_hla:
        return 0

    # Convert input strings to lists of tuples
    recipient_hla = [tuple(allele.split(':')) for allele in recipient_hla.split(',')]
    donor_hla = [tuple(allele.split(':')) for allele in donor_hla.split(',')]

    # Check for full match
    if sorted(recipient_hla) == sorted(donor_hla):
        return 50

    # Check for haplotype match
    recipient_haplotypes = set([tuple(sorted(recipient_hla[:len(recipient_hla) // 2])),
                                tuple(sorted(recipient_hla[len(recipient_hla) // 2:]))])
    donor_haplotypes = set([tuple(sorted(donor_hla[:len(donor_hla) // 2])),
                            tuple(sorted(donor_hla[len(donor_hla) // 2:]))])

    if len(recipient_haplotypes.intersection(donor_haplotypes)) > 0:
        return 40

    # Check for antigen match
    antigen_match_score = 0
    for recipient_allele, donor_allele in zip(recipient_hla, donor_hla):
        if recipient_allele[0] == donor_allele[0]:
            antigen_match_score += 10
            
    return antigen_match_score




score = calculate_hla_score('A*24:02, B*18:01' , 'A*24:02, B*18:01')

print(score)







'''
 A diadic function that determines the blood group compatability between  Potential Donors and Recipients

 The function accepts the following parameters :
* The blood group of the Donor
* The blood group of the Recipient


'''
def calculate_blood_group_score(recipient_blood_group, donor_blood_group):
    # Define a dictionary of compatible blood groups
    compatible_groups = {
        'O+': ['O+', 'O-'],
        'O-': ['O-', 'O+', 'A-', 'B-', 'AB-'],
        'A+': ['A+', 'A-', 'O+', 'O-'],
        'A-': ['A-', 'O-'],
        'B+': ['B+', 'B-', 'O+', 'O-'],
        'B-': ['B-', 'O-'],
        'AB+': ['AB+', 'AB-', 'A+', 'A-', 'B+', 'B-', 'O+', 'O-'],
        'AB-': ['AB-', 'A-', 'B-', 'O-']
    }

    # Check if the recipient and donor blood groups are compatible
    if donor_blood_group in compatible_groups[recipient_blood_group]:
        # Assign a score based on the degree of compatibility
        if recipient_blood_group == donor_blood_group:
            return 10  # Identical blood groups
        elif (recipient_blood_group[-1] == '-' and donor_blood_group[-1] == '+') or \
             (recipient_blood_group[-1] == '+' and donor_blood_group[-1] == '-'):
            return 8  # Compatible with antigen mismatch
        else:
            return 6  # Compatible with different antigen types
    else:
        return 0  # Incompatible blood groups


