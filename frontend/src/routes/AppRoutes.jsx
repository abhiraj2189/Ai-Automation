import { Routes, Route } from "react-router-dom";

import Login from "../pages/Login";
import Register from "../pages/Register";
import Dashboard from "../pages/Dashboard";
import AIChat from "../pages/AIChat";
import Notes from "../pages/Notes";
import Favorites from "../pages/Favorites";
import Settings from "../pages/Settings";
import Research from "../pages/Research";
import Script from "../pages/Script";
import Scene from "../pages/Scene";
import Studio from "../pages/Studio";

import ProtectedRoute from "./ProtectedRoute";

export default function AppRoutes() {
  return (
    <Routes>
      {/* Public Routes */}
      <Route path="/" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route
  path="/research"
  element={
    <ProtectedRoute>
      <Research />
    </ProtectedRoute>
  }
/>
<Route
  path="/script"
  element={
    <ProtectedRoute>
      <Script />
    </ProtectedRoute>
    
  }
/>
<Route
  path="/scene"
  element={
    <ProtectedRoute>
      <Scene />
    </ProtectedRoute>
    
  }
/>

      {/* Protected Routes */}
      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        }
      />

      <Route
        path="/chat"
        element={
          <ProtectedRoute>
            <AIChat />
          </ProtectedRoute>
        }
      />

      <Route
        path="/notes"
        element={
          <ProtectedRoute>
            <Notes />
          </ProtectedRoute>
        }
      />

      <Route
        path="/favorites"
        element={
          <ProtectedRoute>
            <Favorites />
          </ProtectedRoute>
        }
      />

      <Route
        path="/settings"
        element={
          <ProtectedRoute>
            <Settings />
          </ProtectedRoute>
        }
      />
      <Route
    path="/studio"
    element={
        <ProtectedRoute>
            <Studio />
        </ProtectedRoute>
    }
/>
    </Routes>
  );
}