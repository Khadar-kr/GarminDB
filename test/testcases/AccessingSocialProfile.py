import json
import requests


def get_profile_image_url(json_file_path):
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            # Assuming 'profileImageUrlLarge' is a key in the JSON
            profile_image_url = data.get('profileImageUrlLarge', None)
            return profile_image_url
    except FileNotFoundError:
        print(f"Error: File not found at {json_file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to parse JSON in {json_file_path}")
        return None


def is_url_accessible(url):
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        return response.status_code == 200
    except requests.RequestException:
        # If there's any exception during the request, consider the URL as not accessible
        return False


# Example usage
json_file_path = '/Users/nk/HealthData/FitFiles/social-profile.json'
# profile_image_url = get_profile_image_url(json_file_path)
#
# if profile_image_url:
#     print(f"Profile Image URL: {profile_image_url}")
#     if is_url_accessible(profile_image_url):
#         print("The URL is accessible.")
#     else:
#         print("The URL is not accessible.")
# else:
#     print("Unable to retrieve the profile image URL.")
