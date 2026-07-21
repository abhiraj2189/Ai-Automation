import { FaDownload, FaTrash } from "react-icons/fa";

export default function VideoPlayer({

    videoUrl,

    onDownload,

    onDelete

}) {

    return (

        <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

            <h2 className="text-2xl font-bold mb-5">

                Generated Video

            </h2>

            {

                videoUrl

                ?

                <>

                    <video

                        controls

                        className="rounded-xl w-full"

                        src={videoUrl}

                    />

                    <div className="flex gap-4 mt-6">

                        <button

                            onClick={onDownload}

                            className="bg-cyan-500 px-6 py-3 rounded-xl flex items-center gap-2"

                        >

                            <FaDownload/>

                            Download

                        </button>

                        <button

                            onClick={onDelete}

                            className="bg-red-600 px-6 py-3 rounded-xl flex items-center gap-2"

                        >

                            <FaTrash/>

                            Remove

                        </button>

                    </div>

                </>

                :

                <div className="h-72 rounded-xl border-2 border-dashed border-zinc-700 flex items-center justify-center text-zinc-500">

                    Video Preview will appear here...

                </div>

            }

        </div>

    );

}