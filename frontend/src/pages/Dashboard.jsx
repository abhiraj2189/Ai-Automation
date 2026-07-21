import {
    FaVideo,
    FaRobot,
    FaClock,
    FaCheckCircle,
    FaMicrochip,
    FaMemory,
    FaDatabase,
    FaFire
} from "react-icons/fa";

const cards = [

    {

        title:"Videos Generated",

        value:"0",

        icon:<FaVideo className="text-cyan-400 text-3xl"/>

    },

    {

        title:"Running Jobs",

        value:"0",

        icon:<FaRobot className="text-green-400 text-3xl"/>

    },

    {

        title:"Queue",

        value:"0",

        icon:<FaClock className="text-yellow-400 text-3xl"/>

    },

    {

        title:"Completed",

        value:"0",

        icon:<FaCheckCircle className="text-purple-400 text-3xl"/>

    }

];

export default function Dashboard(){

return(

<div className="space-y-8">

<div>

<h1 className="text-4xl font-bold">

Welcome Abhiraj 👋

</h1>

<p className="text-zinc-400 mt-2">

AI Automation Professional Dashboard

</p>

</div>

<div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

{

cards.map(card=>(

<div

key={card.title}

className="bg-zinc-900 rounded-2xl border border-zinc-800 p-6 hover:border-cyan-500 transition"

>

<div className="flex justify-between items-center">

<div>

<p className="text-zinc-400">

{card.title}

</p>

<h2 className="text-3xl font-bold mt-3">

{card.value}

</h2>

</div>

{card.icon}

</div>

</div>

))

}

</div>

<div className="grid lg:grid-cols-2 gap-8">

<div className="bg-zinc-900 rounded-2xl border border-zinc-800 p-6">

<h2 className="text-2xl font-bold mb-6">

System Monitor

</h2>

<div className="space-y-5">

<div>

<div className="flex justify-between">

<span>CPU Usage</span>

<span>0%</span>

</div>

<div className="bg-zinc-800 h-3 rounded-full">

<div className="bg-cyan-500 h-3 rounded-full w-0"/>

</div>

</div>

<div>

<div className="flex justify-between">

<span>RAM Usage</span>

<span>0%</span>

</div>

<div className="bg-zinc-800 h-3 rounded-full">

<div className="bg-green-500 h-3 rounded-full w-0"/>

</div>

</div>

<div>

<div className="flex justify-between">

<span>GPU Usage</span>

<span>0%</span>

</div>

<div className="bg-zinc-800 h-3 rounded-full">

<div className="bg-yellow-500 h-3 rounded-full w-0"/>

</div>

</div>

</div>

</div>

<div className="bg-zinc-900 rounded-2xl border border-zinc-800 p-6">

<h2 className="text-2xl font-bold mb-6">

Quick Actions

</h2>

<div className="grid gap-4">

<button className="bg-cyan-500 hover:bg-cyan-600 rounded-xl py-4">

Generate AI Video

</button>

<button className="bg-zinc-800 hover:bg-zinc-700 rounded-xl py-4">

Open AI Studio

</button>

<button className="bg-zinc-800 hover:bg-zinc-700 rounded-xl py-4">

View Jobs

</button>

<button className="bg-zinc-800 hover:bg-zinc-700 rounded-xl py-4">

Project Manager

</button>

</div>

</div>

</div>

<div className="grid lg:grid-cols-3 gap-6">

<div className="bg-zinc-900 rounded-2xl border border-zinc-800 p-6">

<div className="flex gap-4 items-center">

<FaMicrochip className="text-4xl text-cyan-400"/>

<div>

<h2 className="font-bold">

AI Engine

</h2>

<p className="text-zinc-400">

Online

</p>

</div>

</div>

</div>

<div className="bg-zinc-900 rounded-2xl border border-zinc-800 p-6">

<div className="flex gap-4 items-center">

<FaMemory className="text-4xl text-green-400"/>

<div>

<h2 className="font-bold">

Memory

</h2>

<p className="text-zinc-400">

Ready

</p>

</div>

</div>

</div>

<div className="bg-zinc-900 rounded-2xl border border-zinc-800 p-6">

<div className="flex gap-4 items-center">

<FaDatabase className="text-4xl text-yellow-400"/>

<div>

<h2 className="font-bold">

Database

</h2>

<p className="text-zinc-400">

Connected

</p>

</div>

</div>

</div>

</div>

<div className="bg-zinc-900 rounded-2xl border border-zinc-800 p-6">

<h2 className="text-2xl font-bold mb-6">

Recent Activity

</h2>

<div className="space-y-4">

<div className="flex gap-3 items-center">

<FaFire className="text-orange-400"/>

No Recent Jobs

</div>

</div>

</div>

</div>

);

}