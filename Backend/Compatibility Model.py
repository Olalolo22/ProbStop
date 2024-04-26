def compatibility_score(Donor, Recipient):
    ailment_score = calculate_ailment_score(Donor.nature_of_ailment, Donor.age, Recipient.age)
    bmi_score = calculate_bmi_score(Recipient.height, Recipient.weight, Donor.height, Donor.weight)
    hla_score = calculate_hla_score(Recipient.hla_typing, Donor.hla_typing)
    blood_group_score = calculate_blood_group_score(Recipient.blood_group, Donor.blood_group)
    
    ailment_weight = 0.3
    bmi_weight = 0.2
    hla_weight = 0.4
    blood_group_weight = 0.1

    weighted_sum = (ailment_score * ailment_weight) + (bmi_score * bmi_weight) + (hla_score * hla_weight) + (blood_group_score * blood_group_weight)


    if hla_score == 0 or blood_group_score == 0 or ailment_score == 0:
        return 0
    
    max_weighted_sum = ailment_weight * 10 + bmi_weight * 10 + hla_weight * 50 + blood_group_weight * 10
    normalized_score = (weighted_sum / max_weighted_sum) * 10

    return normalized_score

 
