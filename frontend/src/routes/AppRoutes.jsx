import { Routes, Route } from "react-router-dom";

import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import Studio from "../pages/Studio";
import Jobs from "../pages/Jobs";
import ChatPage from "../chat/ChatPage";
import ProjectsPage from "../projects/ProjectsPage";
import AnalyticsPage from "../analytics/AnalyticsPage";

export default function AppRoutes(){

    return(

        <Routes>

            <Route path="/" element={<Login/>}/>

            <Route path="/dashboard" element={<Dashboard/>}/>

            <Route path="/studio" element={<Studio/>}/>

            <Route path="/jobs" element={<Jobs/>}/>

            <Route path="/chat" element={<ChatPage />} />

            <Route path="/projects" element={<ProjectsPage />} />

            <Route path="/analytics" element={<AnalyticsPage />} />
        </Routes>

    );

}