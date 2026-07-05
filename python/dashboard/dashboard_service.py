from python.dashboard.dashboard_repository import DashboardRepository


class DashboardService:

    def get_dashboard(self, user):

        repo = DashboardRepository()

        return repo.get_stats(user["id"])