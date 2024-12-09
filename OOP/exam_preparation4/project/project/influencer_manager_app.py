from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.campaigns.base_campaign import BaseCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    influencer_dict = {'StandardInfluencer': StandardInfluencer,
                       'PremiumInfluencer': PremiumInfluencer}
    campaign_dict = {'HighBudgetCampaign': HighBudgetCampaign,
                     'LowBudgetCampaign': LowBudgetCampaign}

    def __init__(self):
        self.influencers:list[BaseInfluencer] = []
        self.campaigns:list[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        inf = next((f for f in self.influencers if f.username == username), None)
        if influencer_type not in self.influencer_dict:
            return f"{influencer_type} is not an allowed influencer type."
        if inf:
            return f"{username} is already registered."
        influencer = self.influencer_dict[influencer_type](username, followers, engagement_rate)
        self.influencers.append(influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if any(camp.campaign_id == campaign_id for camp in self.campaigns):
            return f"Campaign ID {campaign_id} has already been created."

        campaign_class = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}.get(campaign_type)
        if not campaign_class:
            return f"{campaign_type} is not a valid campaign type."

        campaign = campaign_class(campaign_id, brand, required_engagement)
        self.campaigns.append(campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = next((inf for inf in self.influencers if inf.username == influencer_username), None)
        campaign = next((camp for camp in self.campaigns if camp.campaign_id == campaign_id), None)

        if not influencer:
            return f"Influencer '{influencer_username}' not found."
        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)
        if payment > 0.0:
            campaign.budget -= payment
            campaign.approved_influencers.append(influencer)
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        return {
            campaign: sum(inf.reached_followers(campaign.type_campaign) for inf in campaign.approved_influencers)
            for campaign in self.campaigns if campaign.approved_influencers
        }

    def influencer_campaign_report(self, username: str):
        influencer = next((inf for inf in self.influencers if inf.username == username), None)
        return influencer.display_campaigns_participated() if influencer else ""

    def campaign_statistics(self):
        campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))
        result = ["$$ Campaign Statistics $$"]
        for campaign in campaigns:
            total_reached_followers = sum(
                inf.reached_followers(type(campaign).__name__) for inf in campaign.approved_influencers
            )
            result.append(
                f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, "
                f"Total budget: ${campaign.budget:.2f}, Total reached followers: {total_reached_followers}"
            )
        return "\n".join(result)




manager = InfluencerManagerApp()

# Register influencers
print(manager.register_influencer("PremiumInfluencer", "JohnDoe", 50000, 4.2))
print(manager.register_influencer("StandardInfluencer", "JaneSmith", 10000, 3.5))
print(manager.register_influencer("PremiumInfluencer", "JohnDoe", 80000, 4.2))
print(manager.register_influencer("InvalidInfluencer", "JohnDoe", 50000, 4.2))
print(manager.register_influencer("StandardInfluencer", "AliceJohnson", 20000, 3.8))
print(manager.register_influencer("PremiumInfluencer", "OliviaBennett", 80000, 4.5))
print(manager.register_influencer("PremiumInfluencer", "DanielRodriguez", 90000, 4.8))
print(manager.register_influencer("PremiumInfluencer", "EmilyTurner", 1000000, 5.0))
#
# Create campaigns
print(manager.create_campaign("LowBudgetCampaign", 1, "TechGurus", 4.0))
print(manager.create_campaign("HighBudgetCampaign", 2, "FashionTrendz", 3.0))
print(manager.create_campaign("LowBudgetCampaign", 1, "FashionTrendz", 3.0))
print(manager.create_campaign("LowBudgetCampaign", 3, "QuantumFusion", 3.0))
print(manager.create_campaign("InvalidCampaign", 4, "FoodieDelights", 2.5))

# Participate in campaigns
print(manager.participate_in_campaign("JohnDoe", 1))
print(manager.participate_in_campaign("JaneSmith", 2))
print(manager.participate_in_campaign("AliceJohnson", 2))
print(manager.participate_in_campaign("AliceJohnson", 1))
print(manager.participate_in_campaign("NonExistentInfluencer", 1))
print(manager.participate_in_campaign("AliceJohnson", 3))
print(manager.participate_in_campaign("JohnDoe", 2))
print(manager.participate_in_campaign("JaneSmith", 4))
print(manager.participate_in_campaign("JaneSmith", 1))
print(manager.participate_in_campaign("OliviaBennett", 3))
print(manager.participate_in_campaign("DanielRodriguez", 3))
print(manager.participate_in_campaign("EmilyTurner", 3))

# Print influencer campaign reports and campaign statistics
print(manager.influencer_campaign_report("JohnDoe"))
print(manager.influencer_campaign_report("JaneSmith"))
print(manager.campaign_statistics())
