const steps = [

    "Research",

    "Script",

    "Voice",

    "Subtitle",

    "Assets",

    "Composer",

    "Completed"

];

export default function WorkflowTimeline({ progress }) {

    const current = Math.floor(progress / 15);

    return (

        <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

            <h2 className="text-xl font-bold mb-6">

                Workflow

            </h2>

            <div className="space-y-4">

                {

                    steps.map((step,index)=>(

                        <div

                            key={step}

                            className={`p-3 rounded-xl

                            ${

                                index<=current

                                ?

                                "bg-cyan-500 text-white"

                                :

                                "bg-zinc-800"

                            }`}

                        >

                            {step}

                        </div>

                    ))

                }

            </div>

        </div>

    );

}