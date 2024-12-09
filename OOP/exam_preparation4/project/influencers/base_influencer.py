from abc import ABC, abstractmethod

from project.campaigns.base_campaign import BaseCampaign


class BaseInfluencer(ABC):

    def __init__(self, username: str, followers: int, engagement_rate: float,type_influencer):
        self.type_influencer = None
        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated: list[BaseCampaign] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: str):
        if value == '' or not value.strip():
            raise ValueError("Username cannot be empty or consist only of whitespace!")
        self.__username = value

    @property
    def followers(self):
        return self.__followers

    @followers.setter
    def followers(self, value):
        if value < 0:
            raise ValueError("Followers must be a non-negative integer!")
        self.__followers = value

    @property
    def engagement_rate(self):
        return self.__engagement_rate

    @engagement_rate.setter
    def engagement_rate(self, value):
        if not (0.0 <= value <= 5.0):
            raise ValueError("Engagement rate should be between 0 and 5.")
        self.__engagement_rate = value

    @abstractmethod
    def calculate_payment(self, campaign: BaseCampaign):
        pass

    @abstractmethod
    def reached_followers(self, campaign_type: str):
        pass

    def display_campaigns_participated(self):
        # if not self.campaigns_participated:
        #     return f"{self.username} has not participated in any campaigns."
        # for campaign in self.campaigns_participated:
        #     result = f"{campaign.type_campaign} :) {self.username} :) participated in the following campaigns:\n"
        #
        #     reached = self.reached_followers(campaign.type_campaign)
        #     result += (f"  - Campaign ID:"
        #                f" {campaign.campaign_id}, "
        #                f"Brand: {campaign.brand}, "
        #                f"Reached followers: {reached}\n")

            #
            # return result.strip()
        if not self.campaigns_participated:
            return f"{self.username} has not participated in any campaigns."

        result = [f"{self.__class__.__name__} :) {self.username} :) participated in the following campaigns:"]
        for campaign in self.campaigns_participated:
            reached_followers = self.reached_followers(type(campaign).__name__)
            result.append(
                f"  - Campaign ID: {campaign.campaign_id}, Brand: {campaign.brand}, Reached followers: {reached_followers}")
        return "\n".join(result)