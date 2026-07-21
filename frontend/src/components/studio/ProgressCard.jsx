export default function ProgressCard({ progress, status }) {

    return (

        <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

            <div className="flex justify-between mb-4">

                <h2 className="text-xl font-bold">

                    Progress

                </h2>

                <span className="text-cyan-400">

                    {status}

                </span>

            </div>

            <div className="w-full bg-zinc-800 rounded-full h-5">

                <div

                    className="bg-cyan-500 h-5 rounded-full transition-all duration-500"

                    style={{

                        width: `${progress}%`

                    }}

                />

            </div>

            <p className="mt-3 text-zinc-400">

                {progress}% Completed

            </p>

        </div>

    );

}