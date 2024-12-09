from unittest import TestCase,main
from project.social_media import SocialMedia

class TestSocialMedia(TestCase):
    def setUp(self):
        """Set up a common SocialMedia instance for tests."""
        self.s = SocialMedia("testuser", "Instagram", 100, "photo")

    def test_initialization(self):
        """Test the proper initialization of the SocialMedia object."""
        self.assertEqual(self.s._username, "testuser")
        self.assertEqual(self.s.platform, "Instagram")
        self.assertEqual(self.s.followers, 100)
        self.assertEqual(self.s._content_type, "photo")
        self.assertEqual(self.s._posts,[])
        self.assertEqual(self.s._validate_and_set_platform(self.s.platform),None)
    def test_platform(self):
        self.assertEqual(self.s._validate_and_set_platform(self.s.platform), None)

    def test_follower_negative_num(self):
        with self.assertRaises(ValueError) as ex:
            self.s.followers = -2
        self.assertEqual("Followers cannot be negative.",str(ex.exception))

    def test_platform_validation(self):
        """Test validation of allowed platforms."""
        with self.assertRaises(ValueError) as ex:
                self.s.platform = "Facebook"
        self.assertEqual(f"Platform should be one of ['Instagram', 'YouTube', 'Twitter']",str(ex.exception))





    def test_create_post(self):
        """Test the creation of a new post."""
        response = self.s.create_post("My first post!")
        self.assertEqual(response, "New photo post created by testuser on Instagram.")
        self.assertEqual(len(self.s._posts), 1)
        self.assertEqual(self.s._posts[0]['content'], "My first post!")

    def test_like_post(self):
        """Test liking a post."""
        self.s.create_post("Test post")
        response = self.s.like_post(0)
        self.assertEqual(response, "Post liked by testuser.")
        self.assertEqual(self.s._posts[0]['likes'], 1)

        # Test liking a post until it reaches the max likes
        for _ in range(10):
            self.s.like_post(0)
        response = self.s.like_post(0)
        self.assertEqual(response, "Post has reached the maximum number of likes.")
        self.assertEqual(self.s._posts[0]['likes'], 10)

    def test_like_post_invalid_index(self):
        """Test liking a post with an invalid index."""
        response = self.s.like_post(99)
        self.assertEqual(response, "Invalid post index.")

    def test_comment_on_post(self):
        """Test adding a comment to a post."""
        self.s.create_post("Test post")
        response = self.s.comment_on_post(0, "This is a great post!")
        self.assertEqual(response, "Comment added by testuser on the post.")
        self.assertEqual(len(self.s._posts[0]['comments']), 1)
        self.assertEqual(self.s._posts[0]['comments'][0]['comment'], "This is a great post!")

    def test_comment_on_post_too_short(self):
        """Test commenting with a comment that's too short."""
        self.s.create_post("Test post")
        response = self.s.comment_on_post(0, "Short")
        self.assertEqual(response, "Comment should be more than 10 characters.")
        self.assertEqual(len(self.s._posts[0]['comments']), 0)

    def test_comment_on_post_invalid_index(self):
        """Test commenting on a post with an invalid index."""
        with self.assertRaises(IndexError):
            self.s.comment_on_post(99, "This is a valid comment!")

if __name__ == "__main__":
    main()
