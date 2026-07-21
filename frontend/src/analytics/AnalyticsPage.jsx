import PageHeader from "../components/common/PageHeader";

import StatsCards from "./components/StatsCards";
import PerformanceChart from "./components/PerformanceChart";
import RecentJobs from "./components/RecentJobs";
import SystemStatus from "./components/SystemStatus";
import StorageCard from "./components/StorageCard";
import TopProjects from "./components/TopProjects";

export default function AnalyticsPage(){

return(

<div className="space-y-8">

<PageHeader

title="Analytics"

subtitle="AI Automation Performance Dashboard"

/>

<StatsCards/>

<div className="grid lg:grid-cols-2 gap-6">

<PerformanceChart/>

<SystemStatus/>

</div>

<div className="grid lg:grid-cols-2 gap-6">

<RecentJobs/>

<StorageCard/>

</div>

<TopProjects/>

</div>

);

}