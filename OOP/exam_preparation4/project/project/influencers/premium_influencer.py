from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    payment_percentage = 0.85

    def __init__(self,username: str, followers: int, engagement_rate: float):

        super().__init__(username,followers,engagement_rate,'PremiumInfluencer')

    def calculate_payment(self,campaign: BaseCampaign):
        payment = campaign.budget * self.payment_percentage
        return payment

    def reached_followers(self,campaign_type: str):

        if campaign_type == 'HighBudgetCampaign':
            high_budget  = int(self.followers * self.engagement_rate * 1.5)
            return high_budget

        else:
            if campaign_type == 'LowBudgetCampaign':
                low_budget = int(self.followers * self.engagement_rate * 0.8)
                return low_budget
