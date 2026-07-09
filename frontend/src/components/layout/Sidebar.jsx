import { NavLink } from "react-router-dom";
import {
  FaHome,
  FaRobot,
  FaFolderOpen,
  FaCog,
} from "react-icons/fa";

const menus = [
  {
    title: "Dashboard",
    icon: <FaHome />,
    path: "/",
  },
  {
    title: "AI Studio",
    icon: <FaRobot />,
    path: "/studio",
  },
  {
    title: "Projects",
    icon: <FaFolderOpen />,
    path: "/projects",
  },
  {
    title: "Settings",
    icon: <FaCog />,
    path: "/settings",
  },
];

export default function Sidebar() {
  return (
    <aside className="w-64 bg-slate-900 border-r border-slate-800">
      <div className="text-2xl font-bold text-center py-6">
        🤖 AI Automation
      </div>

      <nav className="px-4">
        {menus.map((menu) => (
          <NavLink
            key={menu.path}
            to={menu.path}
            className={({ isActive }) =>
              `flex items-center gap-3 p-3 rounded-xl mb-2 transition ${
                isActive
                  ? "bg-blue-600"
                  : "hover:bg-slate-800"
              }`
            }
          >
            {menu.icon}
            {menu.title}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}