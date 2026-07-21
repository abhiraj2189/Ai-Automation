import {

LineChart,

Line,

XAxis,

YAxis,

Tooltip,

ResponsiveContainer

} from "recharts";

const data=[

{day:"Mon",value:0},

{day:"Tue",value:0},

{day:"Wed",value:0},

{day:"Thu",value:0},

{day:"Fri",value:0},

{day:"Sat",value:0},

{day:"Sun",value:0}

];

export default function PerformanceChart(){

return(

<div className="bg-zinc-900 rounded-2xl p-6">

<h2 className="text-xl font-bold mb-5">

Weekly Performance

</h2>

<div style={{height:300}}>

<ResponsiveContainer>

<LineChart data={data}>

<XAxis dataKey="day"/>

<YAxis/>

<Tooltip/>

<Line

type="monotone"

dataKey="value"

stroke="#06b6d4"

strokeWidth={3}

/>

</LineChart>

</ResponsiveContainer>

</div>

</div>

);

}