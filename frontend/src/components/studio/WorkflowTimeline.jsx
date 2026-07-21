import {

FaCheckCircle,

FaSpinner

} from "react-icons/fa";

const steps=[

["script","Script"],

["voice","Voice"],

["subtitle","Subtitle"],

["assets","Assets"],

["render","Rendering"],

["completed","Completed"]

];

export default function WorkflowTimeline({

status

}){

return(

<div className="bg-zinc-900 rounded-2xl border border-zinc-800 p-8">

<h2 className="text-2xl font-bold mb-8">

Workflow Progress

</h2>

<div className="space-y-6">

{

steps.map(step=>(

<div

key={step[0]}

className="flex items-center justify-between"

>

<div>

<h3 className="font-semibold">

{step[1]}

</h3>

</div>

{

status?.[step[0]]

?

<FaCheckCircle className="text-green-400"/>

:

<FaSpinner className="animate-spin text-cyan-400"/>

}

</div>

))

}

</div>

</div>

);

}