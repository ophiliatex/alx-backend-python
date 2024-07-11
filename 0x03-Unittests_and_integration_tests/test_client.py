#!/usr/bin/env python3
"""
Test cases for the client module
"""
import unittest
from unittest.mock import patch, PropertyMock

client = __import__("client")
utils = __import__("utils")
GithubOrgClient = client.GithubOrgClient
fixtures = __import__("fixtures")

from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for the client module
    """

    @patch("utils.get_json")
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    def test_org(self, org_name, mock_get_json):
        """
        Test cases for the client module
        Parameters
        ----------
        org_name
        mock_get_json

        Returns
        -------

        """
        mock_get_json.return_value = {"org": org_name}
        client_ = GithubOrgClient(org_name)
        result = client_.org()

        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, {'org': org_name})

    def test_public_repos_url(self):
        """
        Test cases for the client module
        Parameters
        ----------
        Returns
        -------

        """
        with patch.object(GithubOrgClient, "org", new_callable=property) as mock_org:
            mock_org.return_value = {"repos_url": "https://api.github.com/orgs/test_org/repos"}
            client_ = GithubOrgClient(org_name="test_org")
            result = client_.public_repos_url()

            expected_url = "https://api.github.com/orgs/test_org/repos"
            self.assertEqual(result, expected_url)

    @patch('utils.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that GithubOrgClient.public_repos returns the correct value
        """
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = test_payload

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"

            client = GithubOrgClient("test_org")
            result = client.public_repos()

            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/test_org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"license": {"key": "my_license"}}, "other_license", False),
        ({}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test that GithubOrgClient.has_license returns the correct value
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        "org_payload": fixtures.org_payload,
        "repos_payload": fixtures.repos_payload,
        "expected_repos": fixtures.expected_repos,
        "apache2_repos": fixtures.apache2_repos,
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test cases for the GithubOrgClient class
    """

    @classmethod
    def setUpClass(cls):
        """Setup class-level fixtures"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define the side effect for the mocked requests.get().json()
        def get_json(url):
            if url == "https://api.github.com/orgs/test_org":
                return cls.org_payload
            elif url == "https://api.github.com/orgs/test_org/repos":
                return cls.repos_payload
            return None

        cls.mock_get.return_value.json.side_effect = get_json

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method"""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license filter"""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(license="apache-2.0"), self.apache2_repos)
