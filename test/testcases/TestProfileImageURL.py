import unittest
from AccessingSocialProfile import get_profile_image_url, is_url_accessible


class TestProfileImageURL(unittest.TestCase):

    def test_profile_image_url_accessibility(self):
        json_file_path = '/Users/nk/HealthData/FitFiles/social-profile.json'
        profile_image_url = get_profile_image_url(json_file_path)

        self.assertIsNotNone(profile_image_url, "Profile image URL NOT FOUND.")
        self.assertTrue(is_url_accessible(profile_image_url), "Profile image URL is not accessible.")


if __name__ == '__main__':
    unittest.main()
