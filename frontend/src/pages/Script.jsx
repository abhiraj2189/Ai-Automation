import { useState } from "react";
import MainLayout from "../layouts/MainLayout";
import { generateScript } from "../api/scriptApi";

export default function Script() {

  const [topic, setTopic] = useState("");
  const [script, setScript] = useState("");
  const [loading, setLoading] = useState(false);

  const generate = async () => {

    if (!topic) return;

    setLoading(true);

    try {

      const data = await generateScript(topic);

      setScript(data.script);

    } catch (e) {

      console.log(e);

    } finally {

      setLoading(false);

    }

  };

  return (

    <MainLayout>

      <h1 className="text-4xl font-bold">
        AI Script Generator
      </h1>

      <div className="flex gap-4 mt-8">

        <input
          className="flex-1 bg-zinc-800 p-4 rounded-xl"
          placeholder="Topic..."
          value={topic}
          onChange={(e)=>setTopic(e.target.value)}
        />

        <button
          onClick={generate}
          className="bg-cyan-500 px-8 rounded-xl"
        >
          Generate
        </button>

      </div>

      <div className="bg-zinc-900 rounded-xl mt-8 p-6 whitespace-pre-wrap">

        {loading ? "Generating..." : script}

      </div>

    </MainLayout>

  );

}