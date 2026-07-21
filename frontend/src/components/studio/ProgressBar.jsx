export default function ProgressBar({

    progress = 0,

    stage = "Waiting..."

}) {

    return (

        <div className="bg-zinc-900 rounded-2xl border border-zinc-800 p-6">

            <div className="flex justify-between items-center mb-4">

                <h2 className="text-xl font-bold">

                    Progress

                </h2>

                <span className="text-cyan-400 font-bold">

                    {progress}%

                </span>

            </div>

            <div className="w-full h-5 bg-zinc-800 rounded-full overflow-hidden">

                <div
                    className="h-full bg-gradient-to-r from-cyan-500 to-blue-500 transition-all duration-500"
                    style={{

                        width: `${progress}%`

                    }}
                />

            </div>

            <div className="mt-4 text-zinc-400">

                {stage}

            </div>

        </div>

    );

}