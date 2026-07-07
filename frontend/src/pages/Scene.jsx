import { useState } from "react";
import MainLayout from "../layouts/MainLayout";
import { generateScene } from "../api/sceneApi";

export default function Scene() {

  const [script, setScript] = useState("");
  const [result, setResult] = useState([]);
  const [loading, setLoading] = useState(false);

  const generate = async () => {

    if (!script) return;

    setLoading(true);

    try {

      const data = await generateScene(script);

      setResult(data.scenes);

    } finally {

      setLoading(false);

    }

  };

  return (

    <MainLayout>

      <h1 className="text-4xl font-bold">
        Scene Generator
      </h1>

      <textarea
        rows={10}
        value={script}
        onChange={(e)=>setScript(e.target.value)}
        className="w-full mt-8 p-4 bg-zinc-900 rounded-xl"
        placeholder="Paste Script..."
      />

      <button
        onClick={generate}
        className="mt-6 bg-cyan-500 px-8 py-3 rounded-xl"
      >
        Generate Scene
      </button>

      <div className="mt-10 space-y-6">

        {
          loading
          ? "Generating..."
          : result.map((scene,index)=>(

            <div
              key={index}
              className="bg-zinc-900 rounded-xl p-6"
            >

              <h2 className="text-2xl font-bold">
                Scene {scene.scene}
              </h2>

              <p><b>Duration :</b> {scene.duration}</p>

              <p><b>Voice :</b> {scene.voice}</p>

              <p><b>Visual :</b> {scene.visual}</p>

              <p><b>Caption :</b> {scene.caption}</p>

              <p><b>Animation :</b> {scene.animation}</p>

              <p><b>Transition :</b> {scene.transition}</p>

            </div>

          ))
        }

      </div>

    </MainLayout>

  );

}