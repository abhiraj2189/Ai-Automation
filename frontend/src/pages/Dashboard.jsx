import {
  FaVideo,
  FaRobot,
  FaClock,
  FaCheckCircle,
} from "react-icons/fa";

const cards = [
  {
    title: "Videos Generated",
    value: "0",
    icon: <FaVideo className="text-3xl text-cyan-400" />,
  },
  {
    title: "AI Jobs",
    value: "Idle",
    icon: <FaRobot className="text-3xl text-green-400" />,
  },
  {
    title: "Queue",
    value: "0",
    icon: <FaClock className="text-3xl text-yellow-400" />,
  },
  {
    title: "Completed",
    value: "0",
    icon: <FaCheckCircle className="text-3xl text-purple-400" />,
  },
];

export default function Dashboard() {
  return (
    <div className="space-y-8">

      <div>
        <h1 className="text-4xl font-bold">
          Welcome, Abhiraj 👋
        </h1>

        <p className="text-zinc-400 mt-2">
          AI Automation Control Center
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

        {cards.map((card) => (
          <div
            key={card.title}
            className="bg-zinc-900 rounded-2xl p-6 border border-zinc-800 hover:border-cyan-500 transition"
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
        ))}

      </div>

      <div className="bg-zinc-900 rounded-2xl p-8 border border-zinc-800">

        <h2 className="text-2xl font-bold mb-4">
          Quick Actions
        </h2>

        <div className="flex gap-4 flex-wrap">

          <button className="bg-cyan-500 hover:bg-cyan-600 px-6 py-3 rounded-xl font-semibold transition">
            Generate Video
          </button>

          <button className="bg-zinc-800 hover:bg-zinc-700 px-6 py-3 rounded-xl transition">
            AI Studio
          </button>

          <button className="bg-zinc-800 hover:bg-zinc-700 px-6 py-3 rounded-xl transition">
            View Projects
          </button>

        </div>

      </div>

    </div>
  );
}