import { Link, useNavigate } from "react-router-dom";

import {
    FaHome,
    FaRobot,
    FaStickyNote,
    FaStar,
    FaCog,
    FaSignOutAlt,
    FaSearch,
    FaPenNib,
    FaVideo,
    FaTasks,
} from "react-icons/fa";

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

                <nav className="space-y-5">

                    <Link
                        to="/dashboard"
                        className="flex items-center gap-3 hover:text-cyan-400 transition"
                    >
                        <FaHome />
                        Dashboard
                    </Link>

                    <Link
                        to="/chat"
                        className="flex items-center gap-3 hover:text-cyan-400 transition"
                    >
                        <FaRobot />
                        AI Chat
                    </Link>

                    <Link
                        to="/research"
                        className="flex items-center gap-3 hover:text-cyan-400 transition"
                    >
                        <FaSearch />
                        AI Research
                    </Link>

                    <Link
                        to="/script"
                        className="flex items-center gap-3 hover:text-cyan-400 transition"
                    >
                        <FaPenNib />
                        Script Generator
                    </Link>

                    <Link
                        to="/scene"
                        className="flex items-center gap-3 hover:text-cyan-400 transition"
                    >
                        <FaVideo />
                        Scene Generator
                    </Link>

                    <Link
                        to="/studio"
                        className="flex items-center gap-3 hover:text-cyan-400 transition"
                    >
                        <FaVideo />
                        AI Studio
                    </Link>

                    <Link
                        to="/jobs"
                        className="flex items-center gap-3 hover:text-cyan-400 transition"
                    >
                        <FaTasks />
                        AI Jobs
                    </Link>

                    <Link
                        to="/notes"
                        className="flex items-center gap-3 hover:text-cyan-400 transition"
                    >
                        <FaStickyNote />
                        Notes
                    </Link>

                    <Link
                        to="/favorites"
                        className="flex items-center gap-3 hover:text-cyan-400 transition"
                    >
                        <FaStar />
                        Favorites
                    </Link>

                    <Link
                        to="/settings"
                        className="flex items-center gap-3 hover:text-cyan-400 transition"
                    >
                        <FaCog />
                        Settings
                    </Link>

                </nav>

            </div>

            <button

                onClick={logout}

                className="mt-auto flex items-center justify-center gap-3 bg-red-600 hover:bg-red-700 transition rounded-xl py-3 font-semibold"

            >

                <FaSignOutAlt />

                Logout

            </button>

        </aside>

    );

}