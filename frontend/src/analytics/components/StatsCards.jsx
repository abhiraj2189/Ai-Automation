export default function StatsCards(){

const cards=[

["Videos","0"],

["Jobs","0"],

["Success","100%"],

["Render Time","0 sec"]

];

return(

<div className="grid md:grid-cols-2 xl:grid-cols-4 gap-6">

{

cards.map(card=>(

<div

key={card[0]}

className="bg-zinc-900 rounded-2xl p-6"

>

<p className="text-zinc-400">

{card[0]}

</p>

<h2 className="text-4xl font-bold mt-3">

{card[1]}

</h2>

</div>

))

}

</div>

);

}