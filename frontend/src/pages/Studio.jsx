import { useState } from "react";
import MainLayout from "../layouts/MainLayout";
import { generateProject } from "../api/studioApi";

export default function Studio() {
  const [topic, setTopic] = useState("");

  const [loading, setLoading] = useState(false);

  const [research, setResearch] = useState("");
  const [script, setScript] = useState("");
  const [scenes, setScenes] = useState([]);

  const generate = async () => {
    if (!topic.trim()) return;

    try {
      setLoading(true);

      const result = await generateProject(topic);

      setResearch(result.data.research);
      setScript(result.data.script);
      setScenes(result.data.scenes);
    } catch (err) {
      console.error(err);
      alert("Generation Failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <MainLayout>
      <div className="space-y-6">

        <h1 className="text-3xl font-bold">
          AI Studio
        </h1>

        <div className="flex gap-4">

          <input
            className="flex-1 p-3 rounded-xl bg-zinc-900"
            placeholder="Enter Topic..."
            value={topic}
            onChange={(e)=>setTopic(e.target.value)}
          />

          <button
            onClick={generate}
            className="bg-cyan-500 px-6 rounded-xl"
          >
            {loading ? "Generating..." : "Generate"}
          </button>

        </div>

        {/* Research */}

        <div className="bg-zinc-900 rounded-xl p-5">

          <h2 className="font-bold text-cyan-400 mb-3">
            Research
          </h2>

          <pre className="whitespace-pre-wrap">
            {research}
          </pre>

        </div>

        {/* Script */}

        <div className="bg-zinc-900 rounded-xl p-5">

          <h2 className="font-bold text-cyan-400 mb-3">
            Script
          </h2>

          <pre className="whitespace-pre-wrap">
            {script}
          </pre>

        </div>

        {/* Scene */}

        <div className="bg-zinc-900 rounded-xl p-5">

          <h2 className="font-bold text-cyan-400 mb-3">
            Scene JSON
          </h2>

          <pre className="overflow-auto whitespace-pre-wrap">
            {JSON.stringify(scenes, null, 2)}
          </pre>

        </div>

      </div>
    </MainLayout>
  );
}