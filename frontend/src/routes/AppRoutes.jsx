import { Routes, Route } from "react-router-dom";

import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import Studio from "../pages/Studio";
import Jobs from "../pages/Jobs";

export default function AppRoutes(){

    return(

        <Routes>

            <Route path="/" element={<Login/>}/>

            <Route path="/dashboard" element={<Dashboard/>}/>

            <Route path="/studio" element={<Studio/>}/>

            <Route path="/jobs" element={<Jobs/>}/>

        </Routes>

    );

}