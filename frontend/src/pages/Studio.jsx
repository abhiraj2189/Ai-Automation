import { useState } from "react";
import { FaMagic } from "react-icons/fa";

import { generateVideo } from "../api/studioApi";
import useJobPolling from "../hooks/useJobPolling";

import ProgressCard from "../components/studio/ProgressCard";
import WorkflowTimeline from "../components/studio/WorkflowTimeline";
import LogsPanel from "../components/studio/LogsPanel";
import VideoPlayer from "../components/studio/VideoPlayer";

export default function Studio() {

    const [topic, setTopic] = useState("");

    const [language, setLanguage] = useState("English");

    const [duration, setDuration] = useState("60");

    const [loading, setLoading] = useState(false);

    const [jobId, setJobId] = useState(null);

    const [progress, setProgress] = useState(0);

    const [status, setStatus] = useState("Idle");

    const [logs, setLogs] = useState([]);

    const [videoUrl, setVideoUrl] = useState("");

    const handleGenerate = async () => {

        if (!topic.trim()) {

            alert("Please enter a topic.");

            return;

        }

        try {

            setLoading(true);

            setProgress(0);

            setStatus("Starting");

            setLogs([]);

            setVideoUrl("");

            const data = await generateVideo(

                topic,

                language,

                Number(duration)

            );

            console.log(data);

            setJobId(data.job_id);

        }

        catch (error) {

            console.error(error);

            alert(

                error.response?.data?.detail ||

                "Backend Error"

            );

        }

        finally {

            setLoading(false);

        }

    };

    useJobPolling(

        jobId,

        (job) => {

            setProgress(job.progress || 0);

            setStatus(job.status || "Running");

            setLogs(job.logs || []);

        },

        (job) => {

            setStatus("Completed");

            setProgress(100);

            setVideoUrl(job.video || "");

        }

    );

    const downloadVideo = () => {

        if (videoUrl) {

            window.open(videoUrl);

        }

    };

    const deleteVideo = () => {

        setVideoUrl("");

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

            <div className="bg-zinc-900 rounded-2xl border border-zinc-800 p-8 space-y-6">

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

                        <label className="block mb-2">

                            Language

                        </label>

                        <select

                            value={language}

                            onChange={(e)=>setLanguage(e.target.value)}

                            className="w-full p-4 rounded-xl bg-zinc-800"

                        >

                            <option>English</option>

                            <option>Hindi</option>

                            <option>Hinglish</option>

                        </select>

                    </div>

                    <div>

                        <label className="block mb-2">

                            Duration

                        </label>

                        <select

                            value={duration}

                            onChange={(e)=>setDuration(e.target.value)}

                            className="w-full p-4 rounded-xl bg-zinc-800"

                        >

                            <option value="30">

                                30 Seconds

                            </option>

                            <option value="60">

                                60 Seconds

                            </option>

                            <option value="120">

                                2 Minutes

                            </option>

                        </select>

                    </div>

                </div>

                <button

                    onClick={handleGenerate}

                    disabled={loading}

                    className="bg-cyan-500 hover:bg-cyan-600 disabled:bg-zinc-700 px-8 py-4 rounded-xl flex items-center gap-3 font-bold"

                >

                    <FaMagic />

                    {

                        loading

                        ?

                        "Generating..."

                        :

                        "Generate AI Video"

                    }

                </button>

            </div>

            <ProgressCard

                progress={progress}

                status={status}

            />

            <WorkflowTimeline

                progress={progress}

            />

            <LogsPanel

                logs={logs}

            />

            <VideoPlayer

                videoUrl={videoUrl}

                onDownload={downloadVideo}

                onDelete={deleteVideo}

            />

        </div>

    );

}