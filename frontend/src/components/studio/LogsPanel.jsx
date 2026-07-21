export default function LogsPanel({ logs }) {

    return (

        <div className="bg-black rounded-2xl border border-zinc-800 p-6">

            <h2 className="text-xl font-bold mb-5">

                Live Logs

            </h2>

            <div className="h-72 overflow-auto font-mono text-green-400 space-y-2">

                {

                    logs.length===0

                    ?

                    <p>No Logs Yet...</p>

                    :

                    logs.map((log,index)=>(

                        <div key={index}>

                            {log}

                        </div>

                    ))

                }

            </div>

        </div>

    );

}