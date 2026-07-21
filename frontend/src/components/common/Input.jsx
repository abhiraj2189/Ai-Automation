export default function Input({

label,

...props

}){

return(

<div>

<label className="block mb-2">

{label}

</label>

<input

{...props}

className="

w-full

p-4

rounded-xl

bg-zinc-800

outline-none

border

border-zinc-700

focus:border-cyan-500

"

/>

</div>

);

}