import { Link } from "react-router-dom";
import {
  FaHome,
  FaRobot,
  FaStickyNote,
  FaStar,
  FaCog,
} from "react-icons/fa";

export default function Sidebar() {
  return (
    <aside className="w-72 bg-zinc-900 border-r border-zinc-800 p-6">

      <h1 className="text-3xl font-bold text-cyan-400 mb-10">
        AI Automation
      </h1>

      <nav className="space-y-4">

        <Link className="flex gap-3 items-center hover:text-cyan-400" to="/dashboard">
          <FaHome />
          Dashboard
        </Link>

        <Link className="flex gap-3 items-center hover:text-cyan-400" to="/chat">
          <FaRobot />
          AI Chat
        </Link>

        <Link className="flex gap-3 items-center hover:text-cyan-400" to="/notes">
          <FaStickyNote />
          Notes
        </Link>

        <Link className="flex gap-3 items-center hover:text-cyan-400" to="/favorites">
          <FaStar />
          Favorites
        </Link>

        <Link className="flex gap-3 items-center hover:text-cyan-400" to="/settings">
          <FaCog />
          Settings
        </Link>

      </nav>

    </aside>
  );
}