import { useState } from "react";
import MainLayout from "../layouts/MainLayout";
import { research } from "../api/researchApi";

export default function Research() {

  const [topic, setTopic] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const generateResearch = async () => {

    if (!topic) return;

    setLoading(true);

    try {

      const data = await research(topic);

      setResult(data.research);

    } catch (err) {

      console.log(err);

    } finally {

      setLoading(false);

    }

  };

  return (

    <MainLayout>

      <h1 className="text-4xl font-bold">
        AI Research
      </h1>

      <div className="mt-8 flex gap-4">

        <input
          className="flex-1 bg-zinc-800 p-4 rounded-xl"
          placeholder="Research Topic..."
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
        />

        <button
          onClick={generateResearch}
          className="bg-cyan-500 px-8 rounded-xl"
        >
          Research
        </button>

      </div>

      <div className="mt-8 bg-zinc-900 rounded-xl p-6 whitespace-pre-wrap">

        {loading ? "Researching..." : result}

      </div>

    </MainLayout>

  );

}