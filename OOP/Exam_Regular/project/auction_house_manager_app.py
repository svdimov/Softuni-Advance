
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector
from project.collectors.base_collector import BaseCollector
from project.artifacts.base_artifact import BaseArtifact

class AuctionHouseManagerApp:

    artifact_mapper = {"RenaissanceArtifact": RenaissanceArtifact, "ContemporaryArtifact": ContemporaryArtifact}
    collector_mapper = {'Museum':Museum,'PrivateCollector':PrivateCollector}
    def __init__(self):
        self.artifacts:list[BaseArtifact] = []
        self.collectors:list[BaseCollector] = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):

        if artifact_type not in self.artifact_mapper:
            raise ValueError("Unknown artifact type!")

        art = next((a for a in self.artifacts if a.name== artifact_name),None)
        if art:
            raise ValueError("{artifact_name} has been already registered!")

        artifact = self.artifact_mapper[artifact_type](artifact_name, artifact_price, artifact_space)
        self.artifacts.append(artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):

        if collector_type not in self.collector_mapper:
            raise ValueError("Unknown collector type!")


        coll = next((c for c in self.collectors if c.name == collector_name),None)
        if coll:
            raise ValueError(f"{collector_name} has been already registered!")

        collector = self.collector_mapper[collector_type](collector_name)
        self.collectors.append(collector)
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector = next((c for c in self.collectors if c.name == collector_name), None)
        if not collector:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)
        if not artifact:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required
        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."

    def remove_artifact(self, artifact_name: str):
        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)
        if not artifact:
            return "No such artifact."

        self.artifacts.remove(artifact)
        return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float):
        count = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                count += 1
        return f"{count} collector/s increased their available money."

    def get_auction_report(self):
        sold_count = sum(len(c.purchased_artifacts) for c in self.collectors)
        report = [
            "**Auction statistics**",
            f"Total number of sold artifacts: {sold_count}",
            f"Available artifacts for sale: {len(self.artifacts)}",
            "***",]


        sorted_collectors = [c.__str__() for c in self.collectors]


        report.extend(collector for collector in sorted_collectors)
        return "\n".join(report)


