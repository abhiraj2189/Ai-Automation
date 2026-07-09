import { useState } from "react";
import { FaMagic, FaVideo } from "react-icons/fa";
import { generateVideo } from "../api/studioApi";

export default function Studio() {
  const [topic, setTopic] = useState("");
  const [language, setLanguage] = useState("English");
  const [duration, setDuration] = useState("60");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!topic.trim()) {
      alert("Please enter a topic.");
      return;
    }

    try {
      setLoading(true);

      const data = await generateVideo(topic);

      console.log("Backend Response:", data);

      alert("Video generation started successfully!");

    } catch (error) {
      console.error(error);

      alert(
        error.response?.data?.detail ||
        "Backend Error! Check FastAPI server."
      );

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-8">

      <div>
        <h1 className="text-4xl font-bold">
          AI Studio 🎬
        </h1>

        <p className="text-zinc-400 mt-2">
          Generate AI Videos Automatically
        </p>
      </div>

      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8 space-y-6">

        <div>
          <label className="block mb-2 font-semibold">
            Video Topic
          </label>

          <input
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            placeholder="Enter video topic..."
            className="w-full p-4 rounded-xl bg-zinc-800 outline-none"
          />
        </div>

        <div className="grid md:grid-cols-2 gap-6">

          <div>
            <label className="block mb-2 font-semibold">
              Language
            </label>

            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
              className="w-full p-4 rounded-xl bg-zinc-800"
            >
              <option>English</option>
              <option>Hindi</option>
              <option>Hinglish</option>
            </select>
          </div>

          <div>
            <label className="block mb-2 font-semibold">
              Duration
            </label>

            <select
              value={duration}
              onChange={(e) => setDuration(e.target.value)}
              className="w-full p-4 rounded-xl bg-zinc-800"
            >
              <option value="30">30 Seconds</option>
              <option value="60">60 Seconds</option>
              <option value="120">2 Minutes</option>
            </select>
          </div>

        </div>

        <button
          onClick={handleGenerate}
          disabled={loading}
          className="bg-cyan-500 hover:bg-cyan-600 disabled:bg-zinc-700 px-8 py-4 rounded-xl flex items-center gap-3 font-bold transition"
        >
          <FaMagic />

          {loading ? "Generating..." : "Generate AI Video"}
        </button>

      </div>

      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">

        <h2 className="text-2xl font-bold mb-6 flex items-center gap-3">
          <FaVideo />
          Latest Video
        </h2>

        <div className="h-64 rounded-xl border border-dashed border-zinc-700 flex items-center justify-center text-zinc-500">
          Video Preview Coming Soon...
        </div>

      </div>

    </div>
  );
}