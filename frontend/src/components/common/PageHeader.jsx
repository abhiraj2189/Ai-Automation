export default function PageHeader({

title,

subtitle

}){

return(

<div>

<h1 className="text-4xl font-bold">

{title}

</h1>

<p className="text-zinc-400 mt-2">

{subtitle}

</p>

</div>

);

}