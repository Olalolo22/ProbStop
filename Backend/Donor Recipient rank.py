from geopy.geocoders import Nominatim  # Install geopy library: pip install geopy



'''
A diadic function that calculates an approximate distance in Kilometres between 
  a potential donor and  recipient


  The function acccepts the follwoing parameters:
  *The address  of the recipient
  *The address of the donor
'''
def calculate_distance(recipient_address, donor_address):
  geolocator = Nominatim(user_agent="ProbStop")  
  recipient_location = geolocator.geocode(recipient_address)
  donor_location = geolocator.geocode(donor_address)

  if recipient_location and donor_location:
    recipient_lat = recipient_location.latitude
    recipient_lon = recipient_location.longitude
    donor_lat = donor_location.latitude
    donor_lon = donor_location.longitude

    # Haversine formula for distance calculation (replace if needed)
    from math import radians, sin, cos, acos

    R = 6371  # Earth's radius (in kilometers)
    dlat = radians(donor_lat - recipient_lat)
    dlon = radians(donor_lon - recipient_lon)
    a = sin(dlat/2) * sin(dlat/2) + cos(radians(recipient_lat)) * cos(radians(donor_lat)) * sin(dlon/2) * sin(dlon/2)
    c = 2 * acos(a)
    return R * c  # Distance in kilometers
  else:
    print(f"Location not found for either {recipient_address} or {donor_address}")
    return float('inf')  # Set a high value for addresses with location not found




def calculate_compatibility_and_rank_donors(recipient_id, num_donors=15, distance_weight=0.2):
  recipient = get_recipient_data(recipient_id)

  # Get all donor data (replace with efficient retrieval based on recipient criteria, if needed)
  all_donors = [get_donor_data(donor_id) for donor_id in get_all_donor_ids()]  # Replace with your retrieval logic

  # Calculate compatibility scores and distances for each donor
  ranked_donors = []
  for donor in all_donors:
    score = compatibility_score(recipient, donor)  # Assuming compatibility_score takes recipient and donor objects
    distance = calculate_distance(recipient.address, donor.address)
    weighted_score = (score * (1 - distance_weight)) + (distance * distance_weight)
    ranked_donors.append((donor.donor_id, score, distance, weighted_score))

  # Sort by weighted score (descending order)
  sorted_donors = sorted(ranked_donors, key=lambda item: item[3], reverse=True)

  # Return top N donors based on weighted score (compatibility and distance)
  return sorted_donors[:num_donors]

