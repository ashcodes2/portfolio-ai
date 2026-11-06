import json

from profile_schema import CandidateProfile

# Read JSON file
with open("candidate_profile.json", "r") as file:
    profile_data = json.load(file)

# Validate using Pydantic
candidate = CandidateProfile.model_validate(profile_data)

print("Profile validated successfully!")
print(candidate.personal_info.name)
print(candidate.technical_skills.languages)