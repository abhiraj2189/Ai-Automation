export default function SectionCard({

title,

children

}){

return(

<div

className="

bg-zinc-900

border

border-zinc-800

rounded-2xl

p-6

"

>

<h2

className="

text-2xl

font-bold

mb-5

"

>

{title}

</h2>

{children}

</div>

);

}