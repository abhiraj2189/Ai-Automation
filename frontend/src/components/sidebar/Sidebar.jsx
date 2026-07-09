import { Link, useNavigate } from "react-router-dom";
import {
  FaHome,
  FaRobot,
  FaStickyNote,
  FaStar,
  FaCog,
  FaSignOutAlt,
} from "react-icons/fa";
import { FaSearch } from "react-icons/fa";
import { FaPenNib } from "react-icons/fa";
import { FaVideo } from "react-icons/fa";


export default function Sidebar() {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <aside className="w-72 bg-zinc-900 border-r border-zinc-800 p-6 flex flex-col">

      <div>
        <h1 className="text-3xl font-bold text-cyan-400 mb-10">
          AI Automation
        </h1>

        <nav className="space-y-4">

          <Link
            className="flex items-center gap-3 hover:text-cyan-400"
            to="/dashboard"
          >
            <FaHome />
            Dashboard
          </Link>

          <Link
            className="flex items-center gap-3 hover:text-cyan-400"
            to="/chat"
          >
            <FaRobot />
            AI Chat
          </Link>

          <Link
            className="flex items-center gap-3 hover:text-cyan-400"
            to="/notes"
          >
            <FaStickyNote />
            Notes
          </Link>

          <Link
            className="flex items-center gap-3 hover:text-cyan-400"
            to="/favorites"
          >
            <FaStar />
            Favorites
          </Link>

          <Link
            className="flex items-center gap-3 hover:text-cyan-400"
            to="/settings"
          >
            <FaCog />
            Settings
          </Link>

          <Link
  className="flex gap-3 items-center hover:text-cyan-400"
  to="/research"
>
  <FaSearch />
  AI Research
</Link>
<Link
  className="flex items-center gap-3 hover:text-cyan-400"
  to="/script"
>
  <FaPenNib />
  Script Generator
</Link>
          <Link
  className="flex items-center gap-3 hover:text-cyan-400"
  to="/scene"
>
  <FaVideo />
  Scene Generator
</Link>
<Link
    to="/studio"
    className="flex items-center gap-3 hover:text-cyan-400"
>
    <FaVideo />
    AI Studio
</Link>

        </nav>
      </div>

      <button
        onClick={logout}
        className="mt-auto flex items-center gap-3 bg-red-600 hover:bg-red-700 p-3 rounded-lg transition"
      >
        <FaSignOutAlt />
        Logout
      </button>

    </aside>
  );
}