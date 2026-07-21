import { useContext } from "react";
import { ThemeContext } from "../ui/ThemeProvider";

import {
    FaBell,
    FaMoon,
    FaSun,
    FaSearch,
    FaCircle
} from "react-icons/fa";

export default function Navbar() {

    const { dark, toggleTheme } = useContext(ThemeContext);

    return (

        <header className="h-16 bg-zinc-900 border-b border-zinc-800 flex items-center justify-between px-8">

            {/* Left */}

            <div className="flex items-center gap-5">

                <h1 className="text-2xl font-bold text-cyan-400">

                    AI Automation

                </h1>

                <div className="hidden lg:flex items-center bg-zinc-800 rounded-xl px-4 py-2">

                    <FaSearch className="text-zinc-500"/>

                    <input

                        placeholder="Search..."

                        className="bg-transparent outline-none px-3 w-72"

                    />

                </div>

            </div>

            {/* Right */}

            <div className="flex items-center gap-6">

                <div className="flex items-center gap-2 text-green-400">

                    <FaCircle className="text-xs"/>

                    Backend Online

                </div>

                <button
                    onClick={toggleTheme}
                    className="hover:text-cyan-400 transition"
                >

                    {

                        dark

                        ?

                        <FaSun className="text-xl"/>

                        :

                        <FaMoon className="text-xl"/>

                    }

                </button>

                <button className="relative hover:text-cyan-400">

                    <FaBell className="text-xl"/>

                    <span

                        className="absolute -top-1 -right-1 bg-red-500 w-2 h-2 rounded-full"

                    />

                </button>

                <div className="flex items-center gap-3">

                    <img

                        src="https://ui-avatars.com/api/?name=Abhiraj"

                        className="w-10 h-10 rounded-full"

                    />

                    <div>

                        <p className="font-semibold">

                            Abhiraj

                        </p>

                        <p className="text-xs text-zinc-400">

                            Administrator

                        </p>

                    </div>

                </div>

            </div>

        </header>

    );

}